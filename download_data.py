""" 
for the custom model we will use data from Dataset V5 
"""
# read given data from DatasetV5 and save It if not exit on Disk
# Convert the downlowded data into Xml File
# Convert in to Yolo3 readable file

import os
from os import path
import modules.parser as pars
import modules.utils
import modules.downloader
import modules.show
import modules.csv_downloader
import modules.bounding_boxes as bounding
import modules.image_level as  imageLevel
from configuration import configuration as data_config
from modules.utils import bcolors as bc
from modules import oid_to_pascal_voc_xml as oxml
#from modules import convert

DEFAULT_OID_DIR = os.path.join(os.getcwd(), 'Data/' + data_config.Name_dataset + '/OID')


def do_conversion_file(oid_directory):
    print(bc.HEADER + 'Dataset archtectur for Pascalvoc will be generate'+ bc.ENDC)
    print(bc.INFO + 'Foreach image file a xml file be ceate'+ bc.ENDC)
    oxml.oid_to_pascal_voc_xml(oid_directory)
    print(bc.HEADER + 'Necesary File to train Yolo model will be generate'+ bc.ENDC)
    print(bc.INFO + ' two text file will create in to your train directory'+ bc.ENDC)
    # convert Voc-Format file to yolov3
    import modules.voc_to_YOLOv3
    # reset the current directry as default directory
    os.chdir(os.getcwd())


def download_default_weight_keras():
    # check configuration else alert
    print(bc.HEADER + 'Convert Darknet to keras'+ bc.ENDC)
    print(bc.INFO + 'Check weights file '+ bc.ENDC)
    # check if weight else download from repository
    # e.g https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests
    print(bc.INFO + 'run Convertor'+ bc.ENDC)
    # run convertor
    pass

def downloader(args):
    load = False
    if path.isdir(DEFAULT_OID_DIR):
        print (bc.WARNING + 'A Directory with the name {} alredy exits'.format(data_config.Name_dataset) + bc.ENDC )
        print(bc.INFO + 'Maybe the  data you wont already be downloaded' + bc.ENDC)
        print(bc.INFO + 'When no please  change the value of Name_dataset in to the configuration/download_data.py' + bc.ENDC)
        print(bc.INFO + ' Answer (y)yes if you won to Overwritte the existing dataset (n)no to Exit '+ bc.ENDC)
        answer = input(bc.OKGREEN + 'Continue:' + bc.ENDC)
        if (answer.lower()== "yes" or answer.lower() == "y"):
            load = True
    else:
        load = True
        print(bc.INFO + 'A Directory with the name _{}_ will be create in to a directory named Data in you project'.format(data_config.Name_dataset) + bc.ENDC)
    
    if(load):
        if args.command == 'downloader_ill':
            imageLevel.image_level(args, DEFAULT_OID_DIR)
            do_conversion_file(DEFAULT_OID_DIR)
        else:
            bounding.bounding_boxes_images(args, DEFAULT_OID_DIR)
            do_conversion_file(DEFAULT_OID_DIR)