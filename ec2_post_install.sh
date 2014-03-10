# update system

sudo apt-get update

# get git going

sudo apt-get -y install git

git config --global user.name "kmcintyre"
git config --global user.email kebin70@gmail.com

# Get boto via pip

sudo apt-get -y install python-setuptools python-lxml python-qt4 python-qt4reactor python-opencv libav-tools xvfb
sudo easy_install pip
sudo pip install boto --upgrade
sudo pip install beautifulsoup4
sudo pip install pyvirtualdisplay
sudo easy_install autobahn



if [[ `twistd --version` =~ .*13.1.0* ]]
then
    echo 'Twisted installed'
else
    echo 'Install Twisted'
    sudo apt-get -y install gcc python-dev
	wget http://twistedmatrix.com/Releases/Twisted/13.1/Twisted-13.1.0.tar.bz2
	bunzip2 Twisted-13.1.0.tar.bz2
	tar -xvf Twisted-13.1.0.tar
	
	cd Twisted-13.1.0
	sudo python setup.py install
	cd ..    
	sudo rm -rf Twisted-13.1.0 Twisted-13.1.0.tar
fi

if [ ! -d "6998159"]; then
	https://gist.github.com/6998159.git
fi	

if [ ! -d "gardenpath" ]; then
	# less than perfect
	git clone https://github.com/kmcintyre/gardenpath.git
	cd gardenpath
	sudo python ./setup.py install
	cd ..
fi	

# get scewpt and setup PYTHONPATH
if [ ! -d "scewpt" ]; then
	git clone https://github.com/kmcintyre/scewpt.git
fi
cd scewpt
export PYTHONPATH=`pwd`

echo ''
echo ''
echo 'Rewrite DNS'
echo ''
echo ''

# python scripts/route53_mx_record.py


echo ''
echo ''
echo 'Ready to start - python pyscewpt/start.py'
echo ''
echo ''

# start scewpt mail server

#sudo apt-get -y install python-qt4 python-qt4reactor python-lxml xvfb python-imaging ttf-freefont libicu48
#sudo apt-get install python-pip
#sudo apt-get install xserver-xephyr
#sudo apt-get install tightvncserver
#sudo pip install pyvirtualdisplay
#sudo pip install redis
#sudo apt-get install python-pythonmagick
