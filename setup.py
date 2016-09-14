from setuptools import setup

setup(name='resolv-ec2',
    version='0.1',
    description='Get the public DNS name of a running EC2 instance.',
    url='http://github.com/smaato/resolv-ec2',
    author='Daniel Roschka',
    author_email='daniel@smaato.com',
    license='MIT',
    scripts=['resolv-ec2'],
    zip_safe=False,
    install_requires=['boto3'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)
