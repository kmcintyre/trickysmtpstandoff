trickysmtpstandoff
==================

3 way smtp tls listener - Is most complex behavior option in first guy shot in a seris failure?

all listening on port declared for smtp traffic.  The base case is number of guns (smtp connections) equal to n-1.  Mexican standoff.

Experiment.  All participants open single smtp connectin to each other and listen on port 25 for message.  We're on.

Any message (not connection - may add participants?) is kill switch, existing connections included.

Any message is passed to other participants who die likewise to same message delivered and so on.

Ruels:  

1) a message to die could later be changed to I'm white-listed or I'm black-listed...just read the message right?  You only get the message when you're shot.
2) a loss of connection is an psuedo message
3) logic can be applied to TLS connection.  1 smtp connection gets 1 TLS connection.
4) messaging can be inverted and heartbeat created.  Messages must flow...booh!

Let's never send a message keeps TLS alive forever.  Disconnection is dead-mans declaration of not working pre-wired with a tricky fire-off.

HEAVEN'S WHY?

In a 3 participant stand-off we test scenarios that lay groundwork for services (two tiered system) with hugely complex behaviors.









