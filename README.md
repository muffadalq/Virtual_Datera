# Virtual_Datera

This project contains the files needed to deploy a 3-node datera cluster in a hypervisor environment. It includes:<br />

1) vagrantfile for the hypervisor environment<br />
2) The create_init_file.py script that gets called as a provisioner once the VM is deployed<br />

<b>Prerequisites:</b><br />
Vagrant: https://www.vagrantup.com/downloads.html

<b>Export environment variables:</b><br />
export DATERA_USERNAME="datera_username"<br />
export DATERA_PASSWORD="datera_password"

<b>Download the Datera vbox image:</b><br />
Contact support@datera.io to obtain the image

|Platform|Prerequisites|Setup Instructions|
|KVM|vagrant-libvirt: https://github.com/vagrant-libvirt/vagrant-libvirt| vagrant box add vagrant-Datera_vbox.box --name DateraOS-vagrant|
VirtualBox|N/A|vagrant box add DaterOS-vagrant.box --name DaterOS-vagrant|

<b>Deploying a Datera cluster:</b><br />
vagrant up

<b>Destroying a Datera cluster:</b><br />
vagrant destroy

<b>Logging into Datera cluster:</b><br />
vagrant ssh "vmname"
