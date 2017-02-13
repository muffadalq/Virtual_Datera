# -*- mode: ruby -*-
# vi: set ft=ruby :
#
# needed to work around a product bug
$script = <<SCRIPT
echo I am provisioning...
ip addr del `ifconfig | grep netB2 -A 1 | grep inet | awk '{print $2}'`/24 dev netB2
ip addr del `ifconfig | grep netB1 -A 1 | grep inet | awk '{print $2}'`/24 dev netB1
SCRIPT

Vagrant.configure("2") do |config|
   config.vm.define "vm1" do |vm1|
	  vm1.vm.box = "vagrant-Datera_vbox"
	  vm1.ssh.username = ENV['DATERA_USERNAME']
	  vm1.ssh.password = ENV['DATERA_PASSWORD']
	  vm1.ssh.pty = true
	  vm1.vm.network :private_network, ip: '172.16.211.254', type: "dhcp"
	  vm1.vm.network :private_network, ip: '172.17.211.254', type: "dhcp"
	  vm1.vm.network :private_network, ip: '192.168.100.254', type: "dhcp"
	  vm1.vm.network :private_network, ip: '192.168.110.254', type: "dhcp"
	  vm1.vm.synced_folder ".", "/vagrant_data", disabled: true, owner: "root", group: "root"

	  # provisioner
	  vm1.vm.provision "shell", path: "create_init_file.py"
	  # create vm profile
	  vm1.vm.provider "virtualbox" do |domain|
	     domain.cpus = 2
	     domain.memory = 2048
	     domain.customize ['createmedium', '--filename', './data1.vdi', '--size', 10 * 1024]
	     domain.customize ['storageattach', :id, '--storagectl', 'SATA', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', './data1.vdi']
	     #domain.customize ['createmedium', '--filename', './data2.vdi', '--size', 10 * 1024]
	     #domain.customize ['storageattach', :id, '--storagectl', 'SATA', '--port', 2, '--device', 0, '--type', 'hdd', '--medium', './data2.vdi']
	     #domain.customize ['createmedium', '--filename', './data3.vdi', '--size', 10 * 1024]
	     #domain.customize ['storageattach', :id, '--storagectl', 'SATA', '--port', 3, '--device', 0, '--type', 'hdd', '--medium', './data3.vdi']
             domain.gui = true
	   end
   end
   config.vm.define "vm2" do |vm2|
	  vm2.vm.box = "vagrant-Datera_vbox"
	  vm2.ssh.username = ENV['DATERA_USERNAME']
	  vm2.ssh.password = ENV['DATERA_PASSWORD']
	  vm2.ssh.pty = true
	  vm2.vm.network :private_network, ip: '172.16.211.254', type: "dhcp"
	  vm2.vm.network :private_network, ip: '172.17.211.254', type: "dhcp"
	  vm2.vm.network :private_network, ip: '192.168.100.254', type: "dhcp"
	  vm2.vm.network :private_network, ip: '192.168.110.254', type: "dhcp"
	  vm2.vm.synced_folder ".", "/vagrant_data", disabled: true, owner: "root", group: "root"

	  # provisioner
	  vm2.vm.provision "shell",
            inline: "echo DateraVM > /var/datera/conf/CLUSTERNAME"
          vm2.vm.provision "shell",
            inline: $script
	  # create vm profile
	  vm2.vm.provider "virtualbox" do |domain|
	     domain.cpus = 2
	     domain.memory = 2048
	     domain.customize ['createmedium', '--filename', './data1_2.vdi', '--size', 10 * 1024]
	     domain.customize ['storageattach', :id, '--storagectl', 'SATA', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', './data1_2.vdi']
	     #domain.customize ['createmedium', '--filename', './data2_2.vdi', '--size', 10 * 1024]
	     #domain.customize ['storageattach', :id, '--storagectl', 'SATA', '--port', 2, '--device', 0, '--type', 'hdd', '--medium', './data2_2.vdi']
	     #domain.customize ['createmedium', '--filename', './data3_2.vdi', '--size', 10 * 1024]
	     #domain.customize ['storageattach', :id, '--storagectl', 'SATA', '--port', 3, '--device', 0, '--type', 'hdd', '--medium', './data3_2.vdi']
             domain.gui = true
	   end
   end
   config.vm.define "vm3" do |vm3|
	  vm3.vm.box = "vagrant-Datera_vbox"
	  vm3.ssh.username = ENV['DATERA_USERNAME']
	  vm3.ssh.password = ENV['DATERA_PASSWORD']
	  vm3.ssh.pty = true
	  vm3.vm.network :private_network, ip: '172.16.211.254', type: "dhcp"
	  vm3.vm.network :private_network, ip: '172.17.211.254', type: "dhcp"
	  vm3.vm.network :private_network, ip: '192.168.100.254', type: "dhcp"
	  vm3.vm.network :private_network, ip: '192.168.110.254', type: "dhcp"
	  vm3.vm.synced_folder ".", "/vagrant_data", disabled: true, owner: "root", group: "root"

	  # provisioner
	  vm3.vm.provision "shell",
            inline: "echo DateraVM > /var/datera/conf/CLUSTERNAME"
          vm3.vm.provision "shell",
            inline: $script
	  # create vm profile
	  vm3.vm.provider "virtualbox" do |domain|
	     domain.cpus = 2
	     domain.memory = 2048
	     domain.customize ['createmedium', '--filename', './data1_3.vdi', '--size', 10 * 1024]
	     domain.customize ['storageattach', :id, '--storagectl', 'SATA', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', './data1_3.vdi']
	     #domain.customize ['createmedium', '--filename', './data2_3.vdi', '--size', 10 * 1024]
	     #domain.customize ['storageattach', :id, '--storagectl', 'SATA', '--port', 2, '--device', 0, '--type', 'hdd', '--medium', './data2_3.vdi']
	     #domain.customize ['createmedium', '--filename', './data3_3.vdi', '--size', 10 * 1024]
	     #domain.customize ['storageattach', :id, '--storagectl', 'SATA', '--port', 3, '--device', 0, '--type', 'hdd', '--medium', './data3_3.vdi']
             domain.gui = true
	   end
   end
end
