import os
currdir = os.getcwd()

# Default Download Variriable 
command = "downloader" # witch Option will be running in OIDv4 tool 'downloader', 'visualizer' or 'downloader_ill'
Name_dataset = "Custom_data" # Name of your folder Dataset e.g Custom_data_[calsse_names]
classe = ['Canoe'] # Witch Classes will be Downloaded to see availabel classe ['Apple','Orange']
type_of_Data = 'train' # witch dataset did you wont to Downloaded e.g:['train', 'test', 'validation', 'all']
Quantty = 4 # How many File did you wont

"""
    Confguration to convert Darknet To Keras to keras model
"""
weight_url = "https://pjreddie.com/media/files/yolov3.weights" # link for default weight to use
config_path = os.path.join(currdir, './configuration/models/yolov3.cfg') # Path to Darknet cfg file.
weights_path_model_to_convert = os.path.join(currdir, './Weights/yolov3.weights')  #Path to Darknet weights file
output_path_converted_darknet_to_keras = os.path.join(currdir, './Models/Models_O/yolov3_mO.h5')  # Path to output Keras model file
#weights_only = True # save converted model as Keras weights file only or  instead of model file false.
store_true = True # Plot generated Keras model and save as image False if not.

"""
    Confguration for train 
"""
anchors_path = os.path.join(currdir, './configuration/models/yolo_anchors.txt')
annotation_file =  'Class_4_'+ Name_dataset +'.txt'
classes_file = 'Class_4_'+ Name_dataset +'_classes.txt'
annotation_path = os.path.join(currdir, './Data/' + Name_dataset +'/OID/Dataset/' + annotation_file)
classes_file_path = os.path.join(currdir, './Data/' + Name_dataset +'/OID/Dataset/' + classes_file)
log_dir = 'logs/' + 'Custom_data' + '/'
weight_model_yolov3 = os.path.join(currdir, './Models/Models_O/yolov3_mO.h5')
weight_model_tiny_yolov3 = os.path.join(currdir, './Models/Models_O/tiny_yolov3_mO.h5')