# single node ubuntu server to host docker engine for DockerOperator

IMAGE_NAME = "bento/ubuntu-20.04"
K8S_NAME = "docker-rocks"
MASTERS_NUM = 1
MASTERS_CPU = 2 
MASTERS_MEM = 2048

IP_BASE = "192.168.60."

VAGRANT_DISABLE_VBOXSYMLINKCREATE=1

Vagrant.configure("2") do |config|
    config.ssh.insert_key = false

    (1..MASTERS_NUM).each do |i|      
        config.vm.define "dckr-m-#{i}" do |master|
            master.vm.box = IMAGE_NAME
            master.vm.network "private_network", ip: "#{IP_BASE}#{i + 10}"
            master.vm.hostname = "dckr-m-#{i}"
            master.vm.provider "virtualbox" do |v|
                v.memory = MASTERS_MEM
                v.cpus = MASTERS_CPU
            end            
            master.vm.provision "ansible" do |ansible|
                ansible.playbook = "roles/k8s.yml"
                #Redefine defaults
                ansible.extra_vars = {
                    k8s_cluster_name:       K8S_NAME,                    
                    k8s_master_admin_user:  "vagrant",
                    k8s_master_admin_group: "vagrant",
                    k8s_master_apiserver_advertise_address: "#{IP_BASE}#{i + 10}",
                    k8s_master_node_name: "dckr-m-#{i}",
                    k8s_node_public_ip: "#{IP_BASE}#{i + 10}"
                }                
            end
        end
    end
    config.vm.provision "shell", inline: <<-SHELL
     apt-get update
     apt-get upgrade -y
     apt-get install -y apt-transport-https ca-certificates curl software-properties-common
     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
     add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
     apt-get update
     apt-cache policy docker-ce
     apt-get install -y docker-ce
     systemctl enable docker
     systemctl start docker
     systemctl status docker
     apt-get install -y openssh-server
     systemctl enable ssh
     systemctl start ssh
     systemctl status ssh
  SHELL
end
