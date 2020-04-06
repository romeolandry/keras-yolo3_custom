# Keras-yolo3_custom
1  - install requirement

 active you enviorement and run 

    pip install -r requirement.txt

2- run download to download needed dataset

    python run.py download --limit 5000 --classes Boat Canoe --type_csv all
3- run train option to train

    - first run conver  with -w 
        
        python run.py convert -w --weights_path [path_to_file ] --output_path [path to save keras model]

    - and then run train

        python run.py train

if you already convert the model just run

    python run.py train --weights_path [path to file ] --output_path [path to save keras model]

4- run test 

    python run.py test --input [input video] --output [optional_output]

    if image 

    python run.py test --image



