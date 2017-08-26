#!/usr/bin/env python3

"""
sbx_to_sb2.py

 Copyright (c) 2017 Alan Yorinks All right reserved.

 Python Banyan is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
# convert all files with an sbx extension to sb2
# this is a workaround for a bug in the Scratch 2 editor on Raspberry pi

import glob
import os
import sys


def sbx_to_sb2():
    user = os.listdir("/home")
    pth = '/home/' + user[0]

    for filename in glob.iglob(os.path.join(pth, '*.sbx')):
        os.rename(filename, filename[:-4] + '.sb2')
        print('Renamed {} to {}'.format(filename, filename[:-4] + '.sb2'))

if __name__ == "__main__":
    try:
        sbx_to_sb2()
    except KeyboardInterrupt:
        sys.exit(0)
