sudo apt-get install python3-pip
sudo apt-get install git -y
sudo apt-get install vim -y
pip3 install -r requirements.txt
mv lenovo_x230.pub ~/.ssh/authorized_keys
sudo cp aircho.service /etc/systemd/system
sudo systemctl enable aircho.service
