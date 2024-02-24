import numpy as np
import pandas as pd
from PIL import Image
import cv2
from flask import Flask, jsonify, request
from sklearn.model_selection import train_test_split
X = np.load('image.npz')
X = X['arr_0']
y = pd.read_csv("labels.csv")
y = y["labels"]

classes = ["A","B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
n_classes = len(classes)


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=9, train_size=3500, test_size=500)


scaled_X_train = X_train/255.0
scaled_X_test = X_test/255.0



def get_alphabet(image):

    #opening  
    #image
    im_pil = Image.open(image)
    alph_image = im_pil.convert('L')

    alph_image_resized = alph_image.resize((28,28), Image.ANTIALIAS)

    #setting minimum and max pixel
    pixel_filter = 20
    min_pixel = np.percentile(alph_image_resized, pixel_filter)
    alph_image_resized_inverted_scaled = np.clip(alph_image_resized-min_pixel, 0, 255)
    max_pixel = np.max(alph_image_resized)

    # inverting for proper recognition
    alph_image_resized_inverted_scaled = np.asarray(alph_image_resized_inverted_scaled)/max_pixel

    # converting 2 array and predicting the alphabet
    test_sample = np.array(alph_image_resized_inverted_scaled).reshape(1,660)
    test_pred = train_test_split.predict(test_sample)
    return test_pred[0]




def predict_data():
  image = cv2.imdecode(np.fromstring(request.files.get("alphabet").read(), np.uint8), cv2.IMREAD_UNCHANGED)
  image = request.files.get("alphabet")
  alphabet = get_alphabet(image)
  return jsonify({
    "alphabet_predicted": alphabet
  }), 200

predict_data()