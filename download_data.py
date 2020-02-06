""" for the custom model we will use data from Dataset V5 
"""
# read given data from DatasetV5 and save It if not exit on Disk
# Convert the downlowded data into Xml File
# Convert in to Yolo3 readable file

import os
from sys import exit
from textwrap import dedent
from modules.parser import *
from modules.utils import *
from modules.downloader import *
from modules.show import *
from modules.csv_downloader import *
from modules.bounding_boxes import *
from modules.image_level import *
from configuration import download_data as data_config


DEFAULT_OID_DIR = os.path.join(os.getcwd(), 'Data/OID')

if __name__ == '__main__':
    print("i am the main page")
    print(data_config.option)
    
    print("Default dir is {}".format(DEFAULT_OID_DIR))
    args = parser_arguments()
    if args.command == 'downloader_ill':
        image_level(args, DEFAULT_OID_DIR)
    else:
        bounding_boxes_images(args, DEFAULT_OID_DIR)
