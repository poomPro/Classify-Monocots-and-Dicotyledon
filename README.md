# Classify-Monocots-and-Dicotyledon.

เป็น model ที่สร้างขึ้นโดยการใช้ Deep Learning /AI เพื่อใช้ในการทำนายแบ่งแยกระหว่างพืชใบเลี้ยงเดี่ยวและพืชใบเลี้ยงคู่
Dataset มีข้อมูลรูปภาพโดยข้อมูลแบ่งเป็น Monocotyledonหรือพืชใบเลี้ยงเดี่ยว และ Dicotyledon ใบเลี้ยงคู่
โดยใช้เทคนิคการประมวลผลภาพดิจิทัล รูปภาพจะได้รับการประมวลผลล่วงหน้าก่อน จากนั้นจึงดึงคุณลักษณะตามรูปร่าง สี และพื้นผิวออกจากภาพที่ประมวลผล
ชุดข้อมูลถูกสร้างขึ้นโดยใช้คุณลักษณะที่แยกออกมาเพื่อฝึกและทดสอบ model รูปแบบที่ใช้เป็นเวกเตอร์สนับสนุนเครื่องลักษณนามและก็สามารถที่จะจำแนกประเภทที่มีความถูกต้อง 80.05%
ตัวอย่างข้อมูล

![Screenshot (208)](https://user-images.githubusercontent.com/96648859/147384704-a39379f3-561c-49b5-845e-fcd657f39f67.png)
# Dataset
dataset ที่ใช้ คือ Dataset_Leaf ซึ่งใน folder จะประกอบด้วยโฟลเดอร์แยก 2 folder คือ Monocotyledon (ใบเลี้ยงเดี่ยว ) และ Dicotyledon (ใบเลี้ยงคู่) ที่มีภาพใบแต่ละประเภท ประเภทละ 200 รูป
# Colab

- สร้างโฟลเดอร์ในไดรฟ์ ชื่อ Project นำโฟลเดอร์ Dataset_leaf และ Test_leaf อัปโหลดใส่ในโฟลเดอร์ Project ที่สร้างไว้ในไดรฟ์

![image](https://user-images.githubusercontent.com/95160825/147400035-0e2b1651-437e-4b0d-b061-d0b06e8d22eb.png)

- นำไฟล์ในโฟลเดอร์ Colab ไปอัปโหลดใส่ในโฟลเดอร์ Project ที่สร้างไว้ในไดรฟ์

![image](https://user-images.githubusercontent.com/95160825/147400074-877a02ab-2f44-4811-9110-b7e20d4617a0.png)

- ทำการเปิดไฟล์ create_model.ipynb และทำการเชื่อมต่อกับไดรฟ์ โดยกดที่หมายเลข 1 และ 2 ตามภาพด้านล่าง

![image](https://user-images.githubusercontent.com/95160825/147400207-eafd2c15-836a-48bc-b0de-156f9adf26d5.png)

- Copy Path ของโฟลเดอร์ Dataset_leaf มาใส่ในตัวแปร datasetUrl

![image](https://user-images.githubusercontent.com/95160825/147400176-3ac09a28-0328-4168-9c6e-4749e19972e7.png)

![image](https://user-images.githubusercontent.com/95160825/147400180-aa479d3e-920c-4d6d-b5ca-5175574e3fa3.png)

- ทำการ Run Program เมื่อเสร็จก็จะได้ไฟล์ Model ตามภาพด้านล่าง

![image](https://user-images.githubusercontent.com/95160825/147400343-40fc6a62-b55f-47e7-831f-e645e5c1d7fd.png)

- ดาวน์โหลดไฟล์ Prediction-of-Monocots-and-Dicotyledon.h5

![image](https://user-images.githubusercontent.com/95160825/147400361-bbddb0aa-f6c1-416b-b902-4d39216a806c.png)

- นำไฟล์ Prediction-of-Monocots-and-Dicotyledon.h5 อัปโหลดใส่ในโฟลเดอร์ Project ที่สร้างไว้ในไดรฟ์

![image](https://user-images.githubusercontent.com/95160825/147400527-d9107344-2b48-43b5-b7a3-63ad6e0d4078.png)

- ทำการเปิดไฟล์ test_model.ipynb และทำการเชื่อมต่อกับไดรฟ์ โดยกดที่หมายเลข 1 และ 2 ตามภาพด้านล่าง

![image](https://user-images.githubusercontent.com/95160825/147400207-eafd2c15-836a-48bc-b0de-156f9adf26d5.png)

- ใส่ Path ของไฟล์ Prediction-of-Monocots-and-Dicotyledon.h5 ตามภาพ

![image](https://user-images.githubusercontent.com/95160825/147400479-e28fa720-280c-4b63-91e6-b85bf0b89661.png)

- Copy Path ของโฟลเดอร์ test_leaf มาใส่ในตัวแปร test_leaf_url ตามภาพ

![image](https://user-images.githubusercontent.com/95160825/147400511-e7109067-be64-42c9-b98d-4ecfc3e4ad5d.png)

- ใส่ Path ในส่วนด้านหน้าเป็น Path เดียวกันกับ Path ของ โฟลเดอร์ test_leaf ตามภาพ

![image](https://user-images.githubusercontent.com/95160825/147400589-5d1af438-f506-4e66-aa6a-23f44118b717.png)

- กด Run

# การใช้งานบน editor บนเครื่องที่ติดตั้ง python

กรณีนี้เป็นการใช้ไฟล์ create_model.py และ predict.py ในการรัน สามารถ คัดลอกที่อยู่ของไฟล์ dataset มาใส่ใน dataset_url ของโค้ดไฟล์ create_model.pyได้เลย ดังรูปด้านล่างนี้

![Screenshot (200)](https://user-images.githubusercontent.com/96648859/147384793-a7718638-76e5-488b-9e4c-6b0a656d83ed.png)

  โดยจะทำการสร้างmodel โดยการ ใช้ไฟล์ create_model.py และได้ไฟล์ model ที่นามสกุลไฟล์.h5 มา จากนั้น
จากนั้นใช้ไฟล์  predict.py ในการทำนายรูปที่ต้องการโดยการโหลด model ที่ได้จากการสร้างมา 

ดังรูปด้านล่างนี้

![Screenshot (201)](https://user-images.githubusercontent.com/96648859/147384950-ca13a2f2-5c34-4484-a147-9dad4e354d26.png)


ในไฟล์ predict.py ทำการ Copy ที่อยู่ไฟล์มา ใส่ leaf_picture = "ที่อยู่ของไฟล์"

![Screenshot (209)](https://user-images.githubusercontent.com/96648859/147385122-979024d8-8553-4ab1-95af-4f96c7dd944c.png)

# installed
tensorflow -> https://pypi.org/project/tensorflow/

numpy -> https://pypi.org/project/numpy/

matplotlib -> https://pypi.org/project/matplotlib/



# อ้างอิง

https://www.tensorflow.org/tutorials/images/classification#create_a_dataset






