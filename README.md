# Virtual_Datera

This project contains the files needed to deploy a 3-node datera cluster in a hypervisor environment. It includes:<br />

1) vagrantfile for the hypervisor environment<br />
2) The create_init_file.py script that gets called as a provisioner once the VM is deployed<br />

<b>Prerequisites:</b><br />
VirtualBox, Vagrant

<b>Tested Versions:</b><br />
Virtualbox 5.1.6, Vagrant 1.8.6<br />

<b>Instructions:</b>

<b>Export environment variables:</b><br />
export DATERA_USERNAME="datera_username"<br />
export DATERA_PASSWORD="datera_password"

<b>Download the Datera vbox image:</b><br />
Contact support@datera.io to obtain the image

<b>Add the Datera vbox image in your vagrant environment:</b><br />
vagrant box add vagrant-Datera_vbox.box --name DaterOS-vagrant<br />

<b>Deploying a Datera cluster:</b><br />
vagrant up

<b>Destroying a Datera cluster:</b><br />
vagrant destroy

<b>Logging into Datera cluster:</b><br />
vagrant ssh "vmname"
