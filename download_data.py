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
from modules import oid_to_pascal_voc_xml as oxml

DEFAULT_OID_DIR = os.path.join(os.getcwd(), 'Data/'+data_config.Name_dataset+'/OID')
do_train = False

def do_conversion (oid_directory):
    print(bc.HEADER + 'Dataset archtectur for Pascalvoc will be generate'+ bc.ENDC)
    print(bc.INFO + 'Foreach image file a xml file be ceate'+ bc.ENDC)
    oxml.oid_to_pascal_voc_xml(oid_directory)
    print(bc.HEADER + 'Necesary File to train Yolo model will be generate'+ bc.ENDC)
    print(bc.INFO + ' two text file will create in to your train directory'+ bc.ENDC)
    from modules import voc_to_YOLOv3
    # reset the current directry as default directory

    os.chdir(os.getcwd())

if __name__ == '__main__':

    
    print("Default dir is {}".format(DEFAULT_OID_DIR))

    if path.isdir(DEFAULT_OID_DIR):
        print (bc.WARNING + 'A Directory with the name {} alredy exits'.format(data_config.Name_dataset) + bc.ENDC )
        print(bc.INFO + 'Maybe the  data you wont already be downloaded' + bc.ENDC)
        print(bc.INFO + 'When no please  change the value of Name_dataset in to the configuration/download_data.py' + bc.ENDC)
        print(bc.INFO + ' Answer (y)yes if you won to train with the downloaded dataset (n)no to Exit '+ bc.ENDC)
        answer = input(bc.OKGREEN + 'Continue:' + bc.ENDC)
        if (answer.lower()== "yes" or answer.lower() == "y"):
            # Convert downloaded data into pascal Voc data compatibale xml-file
            do_conversion(DEFAULT_OID_DIR)
            do_train = True
    else:
        print(bc.INFO + 'A Directory with the name _{}_ will be create in to a directory named Data in you project'.format(data_config.Name_dataset) + bc.ENDC)
        args = parser_arguments()
        if args.command == 'downloader_ill':
            image_level(args, DEFAULT_OID_DIR)
            do_conversion(DEFAULT_OID_DIR)
            do_train = True
        else:
            bounding_boxes_images(args, DEFAULT_OID_DIR)
            do_conversion(DEFAULT_OID_DIR)
            do_train = True

    if do_train:
        print(bc.HEADER + 'The training will startted '+ bc.ENDC)