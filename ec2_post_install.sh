sudo apt-get update
sudo apt-get -y install git

# Get boto via pip

sudo apt-get -y install python-setuptools python-lxml python-qt4 python-qt4reactor python-opencv libav-tools xvfb
sudo easy_install pip
sudo pip install boto --upgrade
sudo pip install pyvirtualdisplay



if [[ `twistd --version` =~ .*13.2.0* ]]
then
    echo 'Twisted installed'
else
    echo 'Install Twisted'
    sudo apt-get -y install gcc python-dev
	wget http://twistedmatrix.com/Releases/Twisted/13.2/Twisted-13.2.0.tar.bz2
	bunzip2 Twisted-13.2.0.tar.bz2
	tar -xvf Twisted-13.2.0.tar
	
	cd Twisted-13.2.0
	sudo python setup.py install
	cd ..    
	sudo rm -rf Twisted-13.2.0 Twisted-13.2.0.tar
fi
