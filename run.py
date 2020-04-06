"""
    The run file schould render the needed commando 
"""
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import os
from os import path
import modules.parser as pars
import download_data as dd
import modules.convert as conv_to_keras
import train as tr
import yolo_video as test

if __name__ == "__main__":
    args = pars.parser_arguments()

    if args.option == 'convert':
        conv_to_keras.run_convertor(args)
    if args.option == 'train':
        print("train option was choosed")
        tr.train()
    if args.option == 'download':
        dd.downloader(args)
    if args.option == 'test':
        test.test_yolo3(args)
        print("test yolo model")