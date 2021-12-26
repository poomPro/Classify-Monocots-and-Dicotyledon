from keras.models import load_model
import numpy as np
import tensorflow as tf
import pathlib
# Load the model
model = load_model('Prediction-of-Monocots-and-Dicotyledon.h5')

test_leaf_url = "./Test_leaf"
test_leaf = pathlib.Path(test_leaf_url)

image_count = len(list(test_leaf.glob('*.jpg')))
print(image_count)

for i in range(1, (image_count + 1)):
    #The variable holds the image address to test.
    leaf_picture = "./Test_leaf/" + str(i) + ".jpg"

    #Loads an image into PIL format.
    img = tf.keras.utils.load_img(
        leaf_picture, target_size=(180, 180)
    )
    #Converts a PIL Image instance to a Numpy array.
    img_array = tf.keras.utils.img_to_array(img) 
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    #Create a variable to store the class name.
    classNames  = ["Dicotyledon","Monocotyledon"]
    #ทำนายข้อมูลที่ได้รับมาตามโมเดลที่ใช้
    prediction = model.predict(img_array)
    score = tf.nn.softmax(prediction[0])
    print(score)

    #สร้างตัวแปรมาเก็บชื่อคลาสที่ได้จากการทำนายโดยใช้ฟังก์ชั่น np.argmax ส่งคืนค่าดัชนีที่สูงที่สุดมา
    score_Class=classNames[np.argmax(score)]
    print(score_Class)
    #แสดงผลลัพ
    if(score_Class=='Monocotyledon'):
        print(
        "ภาพนี้น่าจะเป็นของภาพพืชในประเภทใบเลี้ยงเดี่ยว({}), ที่ค่าความเชื่อมัน {:.2f} เปอร์เซ็นต์."
        .format(score_Class, 100 * np.max(score))
    )
    else: print(
        "ภาพนี้น่าจะเป็นของภาพพืชในประเภทใบเลี้ยงคู่({}), ที่ค่าความเชื่อมัน {:.2f} เปอร์เซ็นต์."
        .format(score_Class, 100 * np.max(score))
    )    