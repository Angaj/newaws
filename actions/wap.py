#!/usr/bin/env python
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
import boto3
import urllib3
from st2common.runners.base_action import Action

urllib3.disable_warnings()
ec2 = boto3.resource('ec2')

class MyEchoAction(Action):
	def run(self,ImageId,InstanceType,KeyName):
		# create a new EC2 instance
		instances = ec2.create_instances(
			ImageId=ImageId,
			MinCount=1,
			MaxCount=1,
			InstanceType=InstanceType,
			KeyName=KeyName
 )
