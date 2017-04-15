#!/usr/bin/env python2.7
# written by Arif Ahmed (arifch2009@gmail.com)


import docker



client = docker.from_env()


print "List of the contaienrs"
print client.containers.list()
print "Total running containers are: "+ str(len(client.containers.list()))




