"""

save in to a csv-File all needed parameter thal will deeing use to train a model 
and also the accuracy of model

"""
import os
import io
import pandas as pd
from configuration import configuration as data_config


def to_csv(Last_Model,annotations,file_classe,Classes_number, anchors, log_dir):
    
    data = [{'Last Model':Last_Model,'annotations': annotations,'file_classe':file_classe,'Classes_number': Classes_number, 'anchors':anchors, 'log_dir':log_dir}]     
    df = pd.DataFrame(data, columns=['Last Model','annotations','file_classe','Classes_number', 'anchors', 'log_dir']) 
    if not os.path.exists(data_config.csv_path):
        try:
            df.to_csv(data_config.csv_path, mode='a', header=True)
        except OSError as exc:
            #if exc.errno != errno.ENOENT:
            raise
    else:
        df.to_csv(data_config.csv_path, mode='a', header=False)