# Classify-monocots-and-pairs-from-leaves.

เป็น model ที่สร้างขึ้นโดยการนใช้ Deep Learning /AI เพื่อใช้ในการทำนายแบ่งแยกระหว่างพืชใบเลี้ยงเดี่ยวและพืชใบเลี้ยงคู่
Dataset มีข้อมูลรูปภาพ แบ่งเป็นMonocotyledon หรือพืชใบเลี้ยงเดี่ยว และ Dicotyledon  ใบเลี้ยงคู่
โดยใช้เทคนิคการประมวลผลภาพดิจิทัล รูปภาพจะได้รับการประมวลผลล่วงหน้าก่อน จากนั้นจึงดึงคุณลักษณะตามรูปร่าง สี และพื้นผิวออกจากภาพที่ประมวลผล
ชุดข้อมูลถูกสร้างขึ้นโดยใช้คุณลักษณะที่แยกออกมาเพื่อฝึกและทดสอบ model รูปแบบที่ใช้เป็นเวกเตอร์สนับสนุนเครื่องลักษณนามและก็สามารถที่จะจำแนกประเภทที่มีความถูกต้อง 80.05%
ตัวอย่างข้อมูล

![Screenshot (208)](https://user-images.githubusercontent.com/96648859/147384704-a39379f3-561c-49b5-845e-fcd657f39f67.png)

# Dataset.
dataset ที่ใช้ คือ Dataset_Leaf สามารถดาวน์โหลดได้ที่นี้ ซึ่งในfolder จะประกอบด้วยโฟลเดอร์แยก 2 folder คือ Monocotyledon (ใบเลี้ยงเดี่ยว ) และ Dicotyledon (ใบเลี้ยงคู่) ที่มีภาพใบแต่ละประเภท ประเภทละ 200 รูป

กรณีRun ใน google colab สามารถอัปโหลด folder ไปไว้ใน google drive ได้เลยและทำการเชื่อมต่อ google colab กับ google drive

![Screenshot (203)](https://user-images.githubusercontent.com/96648859/147382457-54b053af-7ddb-4dd7-a30b-adb3c1ef0a22.png)


เมื่อเชื่อมต่อเสร็จหลังจากนั้นก็กดเข้า folder ที่ชื่อว่า drive ->MyDrive ก็จะปรากฏไฟล์ต่างๆภายในdrive เลือกไฟล์ที่อัปโหลดไว้copy path มาวางใน โค้ดส่วนของdatasetURL สามารถใช้งานได้เลย

![Screenshot (197)](https://user-images.githubusercontent.com/96648859/147384738-d6dfaf68-389f-480a-8d4b-ff12e5a778e9.png)

กรณีใช้ไฟล์ create_model.py และ predict.py ในการรัน สามารถ คัดลอกที่อยู่ของไฟล์ มาใส่ใน dataset_url ของโค้ดไฟล์ create_model.pyได้เลย

![Screenshot (200)](https://user-images.githubusercontent.com/96648859/147384793-a7718638-76e5-488b-9e4c-6b0a656d83ed.png)

# การใช้งานบน editor บนเครื่องที่ติดตั้ง python
  จะทำการสร้างmodel โดยการ ใช้ไฟล์ create_model.py และได้ไฟล์ model ที่นามสกุลไฟล์.h5 มา จากนั้น
จากนั้นใช้ไฟล์  predict.py ในการทำนายรูปที่ต้องการโดยการโหลด model ที่ได้จากการสร้างมา 

![Screenshot (201)](https://user-images.githubusercontent.com/96648859/147384950-ca13a2f2-5c34-4484-a147-9dad4e354d26.png)


# การ prediction
ใน google colab ทำการcopy path ของ รูปใบไม้ที่ต้องการที่ได้ทำการอัปโหลดไว้

![Screenshot (209)](https://user-images.githubusercontent.com/96648859/147385027-a6d074af-a442-41ac-87eb-04698efad786.png)

ในที่เป็นไฟล์นามสกุล .py ลักษณะคล้ายกันทำการก็อปปี้ที่อยู่ไฟล์มา ใส่ leaf_picture = "ที่อยู่ของไฟล์"

![Screenshot (209)](https://user-images.githubusercontent.com/96648859/147385122-979024d8-8553-4ab1-95af-4f96c7dd944c.png)

# installed
tensorflow -> https://pypi.org/project/tensorflow/

numpy -> https://pypi.org/project/numpy/

matplotlib -> https://pypi.org/project/matplotlib/



# อ้างอิง

https://www.tensorflow.org/tutorials/images/classification#create_a_dataset






