"""
    The run file schould render the needed commando 
"""
import os
from os import path
import modules.parser as pars
import download_data as dd
import modules.convert as conv_to_keras
import train as tr

if __name__ == "__main__":
    args = pars.parser_arguments()
    
    if args.option == 'train':
        print("train option was choosed")
        conv_to_keras.run_convertor(args)
        tr.train()
    if args.option == 'downloader':
        dd.downloader(args)
    if args.option == 'export':
        print("export model to ONNX")