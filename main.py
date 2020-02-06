# ---------------
# Date: 7/19/2018
# Place: Biella/Torino
# Author: EscVM & TArt
# Project: OID v4
# ---------------

"""
OID v4 Downloader
Download specific classes of the huge online dataset Open Image Dataset.
Licensed under the MIT License (see LICENSE for details)
------------------------------------------------------------
Usage:
refer to README.md file
"""
from sys import exit
from textwrap import dedent
from data_modules.parser import *
from data_modules.utils import *
from data_modules.downloader import *
from data_modules.show import *
from data_modules.csv_downloader import *
from data_modules.bounding_boxes import *
from data_modules.image_level import *


ROOT_DIR = ''
DEFAULT_OID_DIR = os.path.join(ROOT_DIR, 'OID')

if __name__ == '__main__':
    print("i am the main page")
    #args = parser_arguments()

    """ if args.command == 'downloader_ill':
        image_level(args, DEFAULT_OID_DIR)
    else:
        bounding_boxes_images(args, DEFAULT_OID_DIR) """
