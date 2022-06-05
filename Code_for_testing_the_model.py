from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
model = load_model("C:/Users/HP/Desktop/EDA/model_vgg16.h5")
img = image.load_img("C:/Users/HP/Desktop/EDA/Data/val/Cofield/a_0_9509.jpg",target_size=(224,224))
x = image.img_to_array(img)
x = np.expand_dims(x,axis=0)
img_data = preprocess_input(x)
classes = model.predict(img_data)