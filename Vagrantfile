VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  # aptのパッケージをキャッシュするVagrantプラグインvagrant-cachierがあれば使う
  # vagrant plugin install vagrant-fabric
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box 
  end

  # ゲストOS
  (1..1).each do |num|
    config.vm.define :"host#{num}" do | x |
      ip   = "172.28.128.#{100+num}"
      name = "host#{num}"
      x.vm.network :private_network, ip: ip, virtualbox__intnet: "vagrant" #, type: "dhcp"
      x.vm.network :forwarded_port, guest: "80", host: "#{8000+num}"
      x.vm.hostname = name
      #config.vm.synced_folder "/path/to/host", "/path/to/guiest", type: "rsync", rsync__exlude: [".git/"]
    end
  end
end

