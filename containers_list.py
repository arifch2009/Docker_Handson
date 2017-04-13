#!/usr/bin/env python2.7

import docker
client = docker.from_env()


print "List of the contaienrs"
print client.containers.list()
print "Total running containers are: "+ str(len(client.containers.list()))

print "List of images"
for x in client.images.list():
	print x
print "Total number of images are: "+ str(len(client.images.list()))



