# Virtual_Datera

Deploys a datera cluster in a hypervisor environment using vagrant. 

<b>Prerequisites:</b><br />
Vagrant: https://www.vagrantup.com/downloads.html<br />
VM requirements: 2 vCPU and 4GB ram per datera node
Hypervisor: Currently, KVM and VirtualBox are supported

Following the steps below to set up your environment:

1) <b>Cloning Repo:</b><br />
git clone https://github.com/mufaddalq/Virtual_Datera.git

2) <b>Export environment variables:</b><br />
export DATERA_USERNAME="datera_username"<br />
export DATERA_PASSWORD="datera_password"

3) <b>Download the Datera vbox image:</b><br />
Contact support@datera.io to obtain the image

| Hypervisor | Vagrant Plugin Needed | Add datera image to vagrant |
--- | --- | ---
| KVM | vagrant-libvirt: https://github.com/vagrant-libvirt/vagrant-libvirt | vagrant box add vagrant-Datera_vbox.box --name DateraOS-vagrant |
VirtualBox| None |vagrant box add DaterOS-vagrant.box --name DaterOS-vagrant |

Note: If a default Vagrantfile exists in your current directory, please rename or remove that file.

4) <b>Deploying cluster:</b><br />
vagrant up

5) <b>Destroy cluster:</b><br />
vagrant destroy

6) <b>Logg into cluster:</b><br />
vagrant ssh "vmname"
