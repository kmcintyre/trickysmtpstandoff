from zope.interface import implements

from email import parser

from twisted.internet import reactor, defer, error
from twisted.mail import smtp
from twisted.web import server, resource

import json

import time

heartbeat = None

class MessageDelivery:
    implements(smtp.IMessageDelivery)

    def receivedHeader(self, helo, origin, recipients):
        print 'receivedHeader'

    def validateFrom(self, helo, origin):
        print "validateFrom:", helo, origin
        return origin

    def validateTo(self, user):
        if user.dest.local == "heartbeat":
            return lambda: HeartbeatMessage()
        raise smtp.SMTPBadRcpt(user)

class HeartbeatMessage:
    implements(smtp.IMessage)
    
    def lineReceived(self, line):
        pass
    
    def eomReceived(self):
        print "New message received:"
        heartbeat = time.gmtime()
        return defer.succeed(None)
    
    def connectionLost(self):
        self.lines = None

class SMTPProtocol(smtp.ESMTP):

    def connectionMade(self):
        print 'connectionMade'
        smtp.ESMTP.connectionMade(self)

    def state_COMMAND(self, line):
        line = line.strip()
        parts = line.split(None, 1)
        if parts:
            method = self.lookupMethod(parts[0]) or self.do_UNKNOWN
            if len(parts) == 2:
                method(parts[1])
            else:
                method('')
        else:
            self.sendSyntaxError()

    def connectionLost(self, reason):
        #print 'connectionLost'
        if not reason.check(error.ConnectionDone):
            print 'connectionLost', reason
        smtp.SMTP.connectionLost(self, reason)

    def do_SCRB(self, url):
        if self.factory.postman and self.factory.postman.scribe:
            self.scrb = url
            self.sendCode(250, 'SCRB:' + url)
        else:
            self.sendCode(451, 'Scribe Not Enabled')

    def do_NEXT(self, nxt):
        if self.factory.postman and self.factory.postman.scribe:
            self.next = nxt
            self.sendCode(250, 'NEXT:' + nxt)
        else:
            self.sendCode(451, 'Next Not Enabled')

    def do_WSPP(self, nxt):
        if self.factory.postman and self.factory.postman.scribe:
            self.next = nxt
            self.sendCode(250, 'NEXT:' + nxt)
        else:
            self.sendCode(451, 'Next Not Enabled')

    def do_QUIT(self, rest):
        self.sendCode(221, 'Bye')
        self.transport.loseConnection()

class HeartBeat(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return heartbeat

class SMTPServerFactory(smtp.SMTPFactory):
    protocol = SMTPProtocol

    def __init__(self, portal = None):
        smtp.SMTPFactory.__init__(self, portal)

    def buildProtocol(self, addr):
        print 'buildProtocol:', addr.host
        p = smtp.SMTPFactory.buildProtocol(self, addr.host)
        p.host = 'localhost'
        p.delivery = MessageDelivery()
        p.canStartTLS = False
        return p

if __name__ == '__main__':

    smtpFactory = SMTPServerFactory()
    reactor.listenTCP(25, smtpFactory)
    
    site = server.Site(HeartBeat())
    reactor.listenTCP(80, site)
    print 'start SMTP and HTTP'
    reactor.run()
