""" for the custom model we will use data from Dataset V5 
"""
# read given data from DatasetV5 and save It if not exit on Disk
# Convert the downlowded data into Xml File
# Convert in to Yolo3 readable file

import os
from os import path
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
from modules.utils import bcolors as bc


DEFAULT_OID_DIR = os.path.join(os.getcwd(), 'Data/'+data_config.Name_dataset+'/OID')

if __name__ == '__main__':

    
    print("Default dir is {}".format(DEFAULT_OID_DIR))

    if path.isdir(DEFAULT_OID_DIR):
        print (bc.WARNING + 'A Directory with the name {} alredy exits'.format(data_config.Name_dataset) + bc.ENDC )
        print(bc.INFO + 'Maybe the  data you wont already be downloaded' + bc.ENDC)
        print(bc.INFO + 'When no please  change the value of Name_dataset in to the configuration/download_data.py' + bc.ENDC)
        print(bc.INFO + ' Answer (y)yes if you won to train with the downloaded dataset (n)no to Exit '+ bc.ENDC)
        answer = input(bc.OKGREEN + 'Continue:' + bc.ENDC)
        if (answer.lower()== "yes" or answer.lower() == "y"):
            print("Comtinue..")
            args = parser_arguments()
            if args.command == 'downloader_ill':
                image_level(args, DEFAULT_OID_DIR)
            else:
                bounding_boxes_images(args, DEFAULT_OID_DIR)
    else:
        print(bc.INFO + 'A Directory with the name _{}_ will be create in to a directory named Data in you project'.format(data_config.Name_dataset) + bc.ENDC)
        args = parser_arguments()
        if args.command == 'downloader_ill':
            image_level(args, DEFAULT_OID_DIR)
        else:
            bounding_boxes_images(args, DEFAULT_OID_DIR)