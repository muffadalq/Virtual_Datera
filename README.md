# Virtual_Datera

This project contains the files needed to deploy a 3-node datera cluster in a hypervisor environment. It includes:

1) vagrantfile for the hypervisor environment
2) The create_init_file.py script that gets called as a provisioner once the VM is deployed

Prerequisites:
VirtualBox, Vagrant

Tested Versions:
Virtualbox 5.1.6, Vagrant 1.8.6

Instructions:

Export environment variables:
export DATERA_USERNAME="datera_username"
export DATERA_PASSWORD="datera_password"

Download the Datera vbox image

Add the Datera vbox image in your vagrant environment
vagrant box add vagrant-Datera_vbox.box --name vagrant-Datera_vbox

Deploying a Datera cluster
vagrant up

Destroying a Datera cluster
vagrant destroy

Logging into Datera cluster
vagrant ssh <vmname>
