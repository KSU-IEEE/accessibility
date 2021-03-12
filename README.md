This repo contains things documents and applications that are not directly related to the competion  

## services   
A useful tool is to create a startup service on an ubuntu based server or embedded computer (like a pi). There is an example of a bash script used for launching a service in `bash/example_service.sh` and then an example service to run that script in `services/example_service.service`. You should make your own and replace whatever variables you need to. 

After writing the service and bash scripts, you should do the following: 
```BASH 
# move bash to the bin directory
$ sudo cp <bash-script>.sh /usr/bin/<bash-schript>.sh
$ sudo chmod +x /usr/bin/<bash-script>.sh

# move service into systemd
sudo cp <myservice>.service /etc/systemd/system/<myservice>.service
sudo chmod 644 /etc/systemd/system/<myservice>.service

# enable service to be used at boot 
sudo systemctl enable myservice

```
To test your service or stop and start it, you can use the commands:
```BASH
sudo systemctl status myservice
sudo systemctl start myservcie
sudo systemctl stop myservice
sudo systemctl restart myservice
```