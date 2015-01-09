# coding:utf8
# 
from fabric.api import *

# 
# テストの接続先をaws上の端末に設定するタスク
# 
@task
def vagrant():
    """ 接続先をvagrantに設定するタスク """

    env.user = 'vagrant'
    env.hostsfile = 'hosts_aws'
    env.key_filename = '~/.vagrant.d/insecure_private_key'
    env.roledefs = {
            'host': [
                '127.0.0.1:2222',
                ],
            }

