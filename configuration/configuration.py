import os
currdir = os.getcwd()

# Default Download Variriable 
option = "downloader" # witch Option will be runnig  with trun command ['test','train']
command = "downloader" # witch Option will be running in OIDv4 tool 'downloader', 'visualizer' or 'downloader_ill'
Name_dataset = "Custom_data" # Name of your folder Dataset e.g Custom_data_[calsse_names]

classe = ['Canoe'] # Witch Classes will be Downloaded to see availabel classe ['Apple','Orange']
type_of_Data = 'train' # witch dataset did you wont to Downloaded e.g:['train', 'test', 'validation', 'all']
Quantty = 50 # How many File did you wont
annotation_file =  'Class_4_'+ Name_dataset +'.txt'
class_file_classes= annotation_file[:-4]+'_classes.txt'

"""
    Confguration to convert Darknet To Keras to keras model
"""
weight_url = "https://pjreddie.com/media/files/yolov3.weights" # url for default weight to use is weight wasn't given
config_path = os.path.join(os.getcwd(), 'configuration/models/yolov3.cfg') # Path to Darknet cfg file.
weights_path_model_to_convert = os.path.join(currdir, 'Weights/yolov3.weights')  #Path to Darknet weights file
output_path_converted_darknet_to_keras = os.path.join(currdir, 'Models/Models_O/yolov3_mO.h5')  # Path to output Keras model file. it will be give as input model for train and test 
#weights_only = True # save converted model as Keras weights file only or  instead of model file false.
store_true = True # Plot generated Keras model and save as image False if not .

"""
    Confguration to to Train Model
"""
annotation_path = os.path.join(os.getcwd(), 'Data/' + Name_dataset + '/OID/Dataset/' + annotation_file)
# Use coco classes if you test the downloaded modle insteat of you custon model
classes_file_path = os.path.join(os.getcwd(), 'configuration/models/coco_classes.txt')
# classes_file_path = os.path.join(os.getcwd(), 'Data/' + Name_dataset + '/OID/Dataset/' + class_file_classes)
anchors_path = os.path.join(os.getcwd(), 'configuration/models/yolo_anchors.txt') 
log_dir = os.path.join(os.getcwd(), 'log/' + Name_dataset + '/000/') 
trained_model = os.path.join(os.getcwd(), 'Models/Models_OT/'+ Name_dataset + '/custom_model_OT.h5')

"""
    configuration for test 
        "model_path": output of convert 
        "anchors_path": the same that were used to train
        "classes_path": the same that were used to train
"""
# if test model its not given
model_path = trained_model
score = 0.3
iou = 0.45
model_imga_size  =  (416, 416)
gpu_num = 1



