import argparse
from configuration import configuration as data_config


def parser_arguments():
    '''
    Manage the input from the terminal.
    :return: parser
    '''
    
    parser = argparse.ArgumentParser(description='Run Option')

    parser.add_argument("option",
                        metavar="<option> 'train', 'test', 'download'.",
                        help="'train', 'test', 'download'.")
    
    # Options for downloader 
    parser.add_argument("--command",
                        metavar="<command> 'downloader', 'visualizer' or 'ill_downloader'.",
                        help="'downloader', 'visualizer' or 'ill_downloader'.",
                        default=data_config.command)
    parser.add_argument('--Dataset', required=False,
                        metavar="/path/to/OID/csv/",
                        help='Directory of the OID dataset folder')
    parser.add_argument('-y', '--yes', required=False, action='store_true',
                        #metavar="Yes to download missing files",
                        help='ans Yes to possible download of missing files')
    parser.add_argument('--classes', required=False, nargs='+',
                        metavar="list of classes",
                        help="Sequence of 'strings' of the wanted classes",
                        default=data_config.classe)
    parser.add_argument('--type_csv', required=False, choices=['train', 'test', 'validation', 'all'],
                        metavar="'train' or 'validation' or 'test' or 'all'",
                        help='From what csv search the images',
                        default=data_config.type_of_Data)

    parser.add_argument('--sub', required=False, choices=['h', 'm'],
                        metavar="Subset of human verified images or machine generated (h or m)",
                        help='Download from the human verified dataset or from the machine generated one.')

    parser.add_argument('--image_IsOccluded', required=False, choices=['0', '1'],
                        metavar="1 or 0",
                        help='Optional characteristic of the images. Indicates that the object is occluded by another object in the image.')
    parser.add_argument('--image_IsTruncated', required=False, choices=['0', '1'],
                        metavar="1 or 0",
                        help='Optional characteristic of the images. Indicates that the object extends beyond the boundary of the image.')
    parser.add_argument('--image_IsGroupOf', required=False, choices=['0', '1'],
                        metavar="1 or 0",
                        help='Optional characteristic of the images. Indicates that the box spans a group of objects (min 5).')
    parser.add_argument('--image_IsDepiction', required=False, choices=['0', '1'],
                        metavar="1 or 0",
                        help='Optional characteristic of the images. Indicates that the object is a depiction.')
    parser.add_argument('--image_IsInside', required=False, choices=['0', '1'],
                        metavar="1 or 0",
                        help='Optional characteristic of the images. Indicates a picture taken from the inside of the object.')

    parser.add_argument('--multiclasses', required=False, default='0', choices=['0', '1'],
                        metavar="0 (default) or 1",
                        help='Download different classes separately (0) or together (1)')

    parser.add_argument('--n_threads', required=False, metavar="[default 20]",
                        help='Num of the threads to use')

    parser.add_argument('--noLabels', required=False, action='store_true',
                        help='No labels creations')

    parser.add_argument('--limit', required=False, type=int, default=data_config.Quantty,
                        metavar="integer number",
                        help='Optional limit on number of images to download')
    
    # Argument for convertion of the Darknet to keras
    parser.add_argument(
        '--config_path',
        required=False,
        default=data_config.config_path,
        help='Path to Darknet cfg file.')
    parser.add_argument(
        '--weights_path',
        required=False,
        default=data_config.weights_path_model_to_convert,
        help='Path to Darknet weights file.')
    parser.add_argument(
        '--output_path',
        required=False,
        default=data_config.output_path_converted_darknet_to_keras,
        help='Path to output Keras model file.')
    parser.add_argument(
        '-p',
        '--plot_model',
        required=False,
        help='Plot generated Keras model and save as image.',
        action='store_true')
    parser.add_argument(
        '-w',
        '--weights_only',
        required=False,
        help='Save as Keras weights file instead of model file.',
        action='store_true')

    # Option for test model
    parser.add_argument('--convert', required=False, action='store_true',
                        #metavar="Yes to download missing files",
                        help='ans Yes to test from given weigth: the model config will be convert to keras model')

    parser.add_argument(
        '--model_path', type=str,
        required=False,
        default=data_config.model_path,
        help='Path to output Keras model file.'
    )

    parser.add_argument(
        '--anchors_path', type=str,
        default=data_config.anchors_path,
        help='path to anchor definitions, default '
    )

    parser.add_argument(
        '--classes_list', type=str,
        default=data_config.classes_file_path,
        help='path to class definitions, default'
    )

    parser.add_argument(
        '--gpu_num',
        type=int,
        default= data_config.gpu_num,
        help='Number of GPU to use, default ')
    parser.add_argument(
        '--score',
        type=float,
        default= data_config.score,
        help='Number of GPU to use, default ')
    
    parser.add_argument(
        '--iou',
        type=float,
        default= data_config.iou,
        help='Number of GPU to use, default ')
    
    parser.add_argument(
        '--image_size',
        type=tuple,
        default= data_config.model_imga_size,
        help='Number of GPU to use, default')

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str,required=False,default='./path2your_video',
        help = "Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default="",
        help = "[Optional] Video output path"
    )
    return parser.parse_args()
