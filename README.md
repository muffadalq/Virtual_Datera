# Virtual_Datera

This project contains the files needed to deploy a 3-node datera cluster in a hypervisor environment. It includes:<br />

1) vagrantfile for the hypervisor environment<br />
2) The create_init_file.py script that gets called as a provisioner once the VM is deployed<br />

Prerequisites:<br />
VirtualBox, Vagrant

Tested Versions:<br />
Virtualbox 5.1.6, Vagrant 1.8.6<br />

<b>Instructions:</b>

Export environment variables:<br />
export DATERA_USERNAME="datera_username"<br />
export DATERA_PASSWORD="datera_password"

Download the Datera vbox image:<br />
Contact support@datera.io to obtain the image

Add the Datera vbox image in your vagrant environment:<br />
vagrant box add vagrant-Datera_vbox.box --name DaterOS-vagrant<br />

Deploying a Datera cluster:<br />
vagrant up

Destroying a Datera cluster:<br />
vagrant destroy

Logging into Datera cluster:<br />
vagrant ssh "vmname"
