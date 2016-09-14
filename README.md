# Overview

This repository contains a python script which will return the public DNS name
of an EC2 instance. To specify the EC2 instance you can use one of instance id,
private IP, public IP, private DNS name or the value of a "Name" tag attached to
the instance.

# Installation & Usage

* Clone this repository and enter the directory you cloned it into.

* Install the script using pip: ```pip install .```

* Call the script with `--help` to get all options:
```
foo@bar:~$ resolv-ec2 --help
usage: resolv-ec2 [-h] [--aws-access-key-id AWS_ACCESS_KEY_ID]
                  [--aws-secret-access-key AWS_SECRET_ACCESS_KEY]
                  [--profile PROFILE_NAME] [--region REGION_NAME]
                  instance

Get the public DNS name of a running EC2 instance.

positional arguments:
  instance              A unique identifier identifying the EC2 instance.

optional arguments:
  -h, --help            show this help message and exit
  --aws-access-key-id AWS_ACCESS_KEY_ID
                        Specify a value here if you want to use a different
                        AWS_ACCESS_KEY_ID than configured in the AWS CLI.
  --aws-secret-access-key AWS_SECRET_ACCESS_KEY
                        Specify a value here if you want to use a different
                        AWS_SECRET_ACCESS_KEY than configured in the AWS CLI.
  --profile PROFILE_NAME
                        The AWS CLI profile to use. Defaults to the default
                        profile.
  --region REGION_NAME  The AWS region to connect to. Defaults to the one
                        configured for the AWS CLI.
```

* If the script isn't available the location where `pip` installed it into,
might not be in your `$PATH`. Try ```export PATH=$PATH:~/.local/bin```

* Example uses:
```
foo@bar:~$ resolv-ec2 testhost1
ec2-54-86-1-2.compute-1.amazonaws.com

foo@bar:~$ resolv-ec2 i-01234567890abcdef
ec2-54-86-1-2.compute-1.amazonaws.com

foo@bar:~$ resolv-ec2 ip-10-1-2-3
ec2-54-86-1-2.compute-1.amazonaws.com

foo@bar:~$ resolv-ec2 ip-10-1-2-3.ec2.internal
ec2-54-86-1-2.compute-1.amazonaws.com

foo@bar:~$ resolv-ec2 54.86.1.2
ec2-54-86-1-2.compute-1.amazonaws.com

foo@bar:~$ resolv-ec2 ec2-54-86-1-2
ec2-54-86-1-2.compute-1.amazonaws.com

foo@bar:~$ resolv-ec2 ec2-54-86-1-2.compute-1.amazonaws.com
ec2-54-86-1-2.compute-1.amazonaws.com

foo@bar:~$ ssh $(resolv-ec2 i-01234567890abcdef)
```

# Contribution

Pull Requests are welcome!
