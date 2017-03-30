# Virtual_Datera

Deploys a datera cluster in a hypervisor environment using vagrant. 

<b>Prerequisites:</b><br />
Vagrant: https://www.vagrantup.com/downloads.html

<b>Export environment variables:</b><br />
export DATERA_USERNAME="datera_username"<br />
export DATERA_PASSWORD="datera_password"

<b>Download the Datera vbox image:</b><br />
Contact support@datera.io to obtain the image<br />

| Platform | Prerequisites | Setup Instructions |
--- | --- | ---
| KVM | vagrant-libvirt: https://github.com/vagrant-libvirt/vagrant-libvirt | vagrant box add vagrant-Datera_vbox.box --name DateraOS-vagrant |
VirtualBox| N/A |vagrant box add DaterOS-vagrant.box --name DaterOS-vagrant |

<b>Deploying cluster:</b><br />
vagrant up

<b>Destroy cluster:</b><br />
vagrant destroy

<b>Logg into cluster:</b><br />
vagrant ssh "vmname"
