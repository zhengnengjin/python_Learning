#__author: ZhengNengjin
#__date: 2018/9/30

import configparser

# config = configparser.ConfigParser()
#
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
#
# with open('example.ini', 'w') as configfile:
# 	config.write(configfile)
#
# '''写完了读出来'''
# print(config.sections())
# print(config.defaults())
#
# config['DEFAULT']['Compression']
# 'bitbucket.org' in config
#
# for key in config['bitbucket.org']:
# 	print(key)
#
# config['bitbucket.org']['ForwardX11']
#
# '''configparser增删改查语法'''
# # [section1]
# k1 = v1
# k2: v2
#
# # [section2]
# k1 = v1
#
# import ConfigParser
#
# config = ConfigParser.ConfigParser()
# config.read('i.cfg')

# ########## 读 ##########
secs = config.sections()
print(secs)
options = config.options('group2')
print(options)

item_list = config.items('group2')
print(item_list)

val = config.get('group1','key')
val = config.getint('group1','key')

# ########## 改写 ##########
# sec = config.remove_section('group1')
# config.write(open('i.cfg', "w"))

# sec = config.has_section('wupeiqi')
# sec = config.add_section('wupeiqi')
# config.write(open('i.cfg', "w"))


# config.set('group2','k1',11111)
# config.write(open('i.cfg', "w"))

# config.remove_option('group2','age')
# config.write(open('i.cfg', "w"))

