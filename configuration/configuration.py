import os
currdir = os.getcwd()
# Default Download Variriable 
option = "downloader" # witch Option will be running in OIDv4 tool
Name_dataset = "Custom_data" # Name of your folder Dataset
classe = ['Canoe'] # Witch Classes will be Downloaded to see availabel classe ['Apple','Orange']
type_of_Data = 'train' # witch dataset did you wont to Downloaded e.g:['train', 'test', 'validation', 'all']
Quantty = 4 # How many File did you wont
class_name =  'Class_4_'+ Name_dataset +'.txt'
class_file_classes= class_name +'_classes.txt'

"""
    Confguration to convert Darknet To Keras to keras model
"""
config_path = # Path to Darknet cfg file.
weights_path_to_for_convertion = os.path.join(currdir '../weights/')  #Path to Darknet weights file
output_path_converted_darknet_to_keras = os.path.join(currdir '../Models/Models_O')  # Path to output Keras model file
weights_only = True # save converted model as Keras weights file only or  instead of model file false.
store_true = True # Plot generated Keras model and save as image False if not .