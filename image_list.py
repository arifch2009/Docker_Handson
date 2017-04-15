#!/usr/bin/env python2.7
# written by Arif Ahmed (arifch2009@gmail.com)


import docker



client = docker.from_env()

print "List of images"
for x in client.images.list():
	print x
print "Total number of images are: "+ str(len(client.images.list()))

