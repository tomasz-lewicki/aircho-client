# smog-client-2
Code for a client for an air quality sensor web application

Client code for raspberry pi.
It runs as a linux service and periodically sends air quality data as a POST requests to the server.

To run it:
```
sudo cp aircho.service /etc/systemd/system
sudo systemctl restart aircho.service
```
