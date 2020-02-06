#!/usr/bin/env python3

import boto3
import time
import random
import string
import argparse
from pathlib import Path
import sys

# Define cmdline arguments
parser = argparse.ArgumentParser(
    description='Create a new AMI using a UserData script',
)
parser.add_argument('ami',
    help='Base AMI',
)
parser.add_argument('userdata',
    type=Path,
    help='UserData script',
)
parser.add_argument('key',
    help='SSH key name',
)
parser.add_argument('-t','--instance-type',
    default='t3.micro',
    help='Instance type for running update',
)
parser.add_argument('-n','--ami-name',
    help='New AMI name. Default is random alpha string',
)
parser.add_argument('-i','--inspect',
    action='store_true',
    help='Launch a instance of the new AMI to inspect',
)
parser.add_argument('--ip',
    help='Assign elastic IP to instance for inspection',
)
args = parser.parse_args()

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

# Verify Arguments
response = client.describe_images(Owners=['self'])
cur_image_names = set([image['Name'] for image in response['Images']])
if args.ami_name:
    if args.ami_name in cur_image_names:
        msg = f'AMI name {args.ami_name} is taken. Select another.'
        exit(msg)
else:
    while True:
        args.ami_name = ''.join([random.choice(string.ascii_lowercase) for _ in range(5)])
        if args.ami_name not in cur_image_names:
            break

# Launch instance
instance_args = {
    'ImageId': args.ami,
    'InstanceType': args.instance_type,
    'MaxCount': 1,
    'MinCount': 1,
    'UserData': args.userdata.read_text(),
    'KeyName': args.key
}
response = client.run_instances(**instance_args)
instance_id = response['Instances'][0]['InstanceId']
instance = ec2.Instance(instance_id)
print(f'{instance.id} starting', file=sys.stderr)
instance.wait_until_running()
print(f'{instance.id} running', file=sys.stderr)
instance.wait_until_stopped()
print(f'{instance.id} stopped', file=sys.stderr)

# Create AMI
response = client.create_image(
    InstanceId = instance.id,
    Name = args.ami_name
)
print(f'Creating image: {args.ami_name}', file=sys.stderr)
image_id = response['ImageId']
while True:
    image = ec2.Image(image_id)
    if image.state == 'available':
        break
print(f'AMI: {image.id}')
instance.terminate()

# Create inspection image
if args.inspect:
    del instance_args['UserData']
    instance_args['ImageId'] = image.id
    response = client.run_instances(**instance_args)
    inspection_id = response['Instances'][0]['InstanceId']
    print(f'Inspection Instance: {inspection_id}')
    inspection = ec2.Instance(inspection_id)
    inspection.wait_until_running()
    if args.ip:
        client.associate_address(
            AllocationId = args.ip,
            InstanceId = inspection.id,
        )
    print(f'Inspection IP: {inspection.public_ip_address}')