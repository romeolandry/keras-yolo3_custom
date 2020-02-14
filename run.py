"""
    The run file schould render the needed commando 
"""
import os
from os import path
import modules.parser as pars

if __name__ == "__main__":
    args = pars.parser_arguments()
    
    if args.option == 'train':
        print("train option was choosed")
    if args.option == 'downloader':
        import download_data as d
        d.downloader(args)
    if args.option == 'export':
        print("export model to ONNX")