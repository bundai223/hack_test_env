# coding:utf8
# fab -i [sshの秘密鍵] -u [ユーザ名] -H [ホスト名] [タスク]
# fabfile.py で実行する内容を設定（ポートにも注意）

from fabric.api import *
from fabric.api import *
import fabric.contrib.files as F
import role

env.use_ssh_config = True

@task
@roles('host')
def setup_host():
    run("echo 'NO OPERATION.'")
    #sudo("echp 'NO OPERATION.'", warn_only=False)
    #put("/path/to/hostside", "/path/to/guestside", use_sudo=False)

    put('~/repos/github.com/bundai223/hack_setup/ubuntu', '~/')
    sudo('~/ubuntu/nginx.conf', '/etc/init/')
    sudo('sh ~/scripts/install_hhvm.sh')
    sudo('sh ~/scripts/install_nginx.sh')

# hosts追記
def append_hosts():
    with file("hosts_appends", 'r') as fp:
        hosts = fp.read()
        F.append("/etc/hosts", hosts, use_sudo=True)

