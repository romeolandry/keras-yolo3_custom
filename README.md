# Keras-yolo3_custom
1  - install requirement

 active you enviorement and run 

    pip install -r requirement.txt

2- run download to download needed dataset

    python run.py download --limit 5000 --classes Boat Canoe --type_csv all
3- run train option to train

launch train option  with --convert parameter to create the keras model throught yolo configuration

    python run.py train --convert --weights_path [path to file ] --output_path [path to save keras model] 

if you already convert the model just run

    python run.py train --weights_path [path to file ] --output_path [path to save keras model]

4- run test 

    python run.py test --input [input video] --output [optional_output]

    if image 

    python run.py test --image



