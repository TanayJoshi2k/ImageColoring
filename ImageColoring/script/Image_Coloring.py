import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import argparse

os.chdir(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))

### Create a dir to store o/p images
output_dir = 'output'
if output_dir not in os.listdir():
    os.makedirs(output_dir)

parser = argparse.ArgumentParser()
parser.add_argument('input_path', help="Argument for image path")
args = parser.parse_args()


print(os.getcwd())

model = tf.keras.models.load_model('./model/color.h5')
try:
    test = cv2.imread(args.input_path)
    og_dim_x, og_dim_y = test.shape[0], test.shape[1]
    ### change image format from BGR -> LAB
    test = cv2.cvtColor(test, cv2.COLOR_BGR2LAB) 

    ### resize to (224, 224, 3)
    test = cv2.resize(test, (224, 224)) 

    pred = np.zeros((224, 224, 3))

    ### copy the L channel 
    pred[:, :, 0] = test[:, :, 0] 

    ### predict the AB channels
    AB = model.predict(test[:, :, 0].reshape(1, 224, 224, 1))
    AB = AB*128

    ### copy the predicted AB channels
    pred[:, :, 1:] = AB 

    ### convert to float32 dtype and convert back to RGB format
    pred = np.float32(pred) 
    pred = cv2.cvtColor(pred, cv2.COLOR_LAB2RGB)

    ### Save the image in the output folder
    plt.figure(figsize=(5, 6), dpi=50)
    plt.imshow(pred)
    plt.show()
    save_as_file_name, extension = os.path.split(args.input_path)[-1].split(".")
    extension = '.' + extension
    print(save_as_file_name, extension)
    plt.savefig(os.path.join('output', save_as_file_name + extension))

except Exception as e:
    print(e)
