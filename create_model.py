import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import pathlib

#Create a path to the file where the Dataset
dataset_url = "C:/Users/Windows10/Documents/testL/Dataset_leaf"
data_dir = pathlib.Path(dataset_url)

#Count the images that are found with the jpg extension.
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

#The variable determines the aspect ratio of the image.
batch_size = 32
img_height = 180
img_width = 180
#สร้างตัวแปรเก็บค่าใช้สร้างเทรนโมเดลโดยการแบ่งข้อมูล2อย่าง train และ validation
#ตัวแปรไว้ใช้เก็บข้อมูลในการเทรนประมาณ80%ของข้อมูล
train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)
#ตัวแปรไว้ใช้เก็บข้อมูลไว้ใช้ทดสอบประมาณ 20% ของข้อมูล
val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)  

#Used to display the class name that contains
classNames = train_ds.class_names
print(classNames)


#พลอตรูปออกมาแสดงตัวอย่างของรูปภาพ
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(classNames[labels[i]])
    plt.axis("off")

#แสดงรูปร่างของรูปภาพ
"""for image_batch, labels_batch in train_ds:
  print(image_batch.shape)
  print(labels_batch.shape)
  break  """
  #image_batch=(32, 180, 180, 3)This is a batch of 32 images of shape 180x180x3
  # labels_batch.shape = (32,)Is a tensor of the shape (32,)

#
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

normalization_layer = layers.Rescaling(1./255)

normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
print(np.min(first_image), np.max(first_image))

#Create the model
num_classes = len(classNames)
model = Sequential([
  layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])

#Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

#ดูเลเยอทั้งหมดของโมเดล
model.summary()

#Train the model
epochs=20
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)  
#save model to file .h5
model.save('my_Model.h5')

#Create a graph of data loss and values. The accuracy that the trend has shown
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs_range = range(epochs)
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

