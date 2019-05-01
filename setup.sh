#sudo apt-get install git -y
#remember to enable serial0 on raspberry pi
#PROD/DEV
#pip3 install virtualenv
#pip3 install rpi_ws281x adafruit-circuitpython-neopixel


export NODE_ID=1
export URI=https://aircho-new.herokuapp.com/measurements/
export LOG_PATH=~/logs/
export PBAY_DEV='/dev/ttyUSB0'
export PMS_DEV='/dev/serial0'
export PMS_BUF_SIZE=300 #that is about 5 minutes
export DEBUG=True
