from setuptools import setup
import os
from subprocess import call

call(["pip3", "install", "git+https://github.com/dpallot/simple-websocket-server.git"])

user = os.listdir("/home")
user = '/home/' + user[0] + '/'
print(user)

setup(
    name='s2-pi',
    version='1.4',
    packages=['s2_pi'],
    # install_requires=['simple-websocket-server'],
    # dependency_links=["pip3 install git+https://github.com/dpallot/simple-websocket-server.git"],


    data_files=[(user, ['s2_pi/s2_pi.js'])],

    entry_points={
            'console_scripts': ['s2pi = s2_pi.s2_pi:run_server']
        },
    url='https://github.com/MrYsLab/s2-pi',
    license='GNU General Public License v3 (GPLv3)',
    author='Alan Yorinks',
    author_email='MisterYsLab@gmail.com',
    description='Creating Scratch 2 Extensions For The Raspberry Pi',
    keywords=['Raspberry Pi', 'Scratch 2', 'Extensions'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Other Environment',
            'Intended Audience :: Education',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.4',
            'Topic :: Education',
            'Topic :: Software Development',
        ],
)
