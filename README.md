# Classify-monocots-and-pairs-from-leaves.

เป็น model ที่สร้างขึ้นโดยการนใช้ Deep Learning /AI เพื่อใช้ในการทำนายแบ่งแยกระหว่างพืชใบเลี้ยงเดี่ยวและพืชใบเลี้ยงคู่
Dataset มีข้อมูลรูปภาพ=แบ่งเป็นMonocotyledon หรือพืชใบเลี้ยงเดี่ยว และ Dicotyledon  ใบเลี้ยงคู่
โดยใช้เทคนิคการประมวลผลภาพดิจิทัล รูปภาพจะได้รับการประมวลผลล่วงหน้าก่อน จากนั้นจึงดึงคุณลักษณะตามรูปร่าง สี และพื้นผิวออกจากภาพที่ประมวลผล

ชุดข้อมูลถูกสร้างขึ้นโดยใช้คุณลักษณะที่แยกออกมาเพื่อฝึกและทดสอบโมเดล รูปแบบที่ใช้เป็นเวกเตอร์สนับสนุนเครื่องลักษณนามและก็สามารถที่จะจำแนกประเภทที่มีความถูกต้อง 90.05%
ตัวอย่างข้อมูล

![Screenshot (208)](https://user-images.githubusercontent.com/96648859/147384704-a39379f3-561c-49b5-845e-fcd657f39f67.png)

# Dataset.
กรณีRun ใน google colab สามารถอัปโหลดโฟเดอไปไว้ใน google drive ได้เลยและทำการเชื่อมต่อ google colab กับ google drive

![Screenshot (203)](https://user-images.githubusercontent.com/96648859/147382457-54b053af-7ddb-4dd7-a30b-adb3c1ef0a22.png)


เมื่อเชื่อมต่อเสร็จหลังจากนั้นก็กดเข้าfolderที่ชื่อว่า drive ->MyDrive ก็จะปรากฏไฟล์ต่างๆภายในdrive เลือกไฟล์ที่อัปโหลดไว้copy path มาวางใน โค้ดส่วนของdatasetURL

![Screenshot (197)](https://user-images.githubusercontent.com/96648859/147384738-d6dfaf68-389f-480a-8d4b-ff12e5a778e9.png)

กรณีใช้ไฟล์ create_model.py และ predict.py ในการรัน สามารถ คัดลอกที่อยู่ของไฟล์ มาใส่ใน dataset_url ของโค้ดได้เลย

![Screenshot (200)](https://user-images.githubusercontent.com/96648859/147384793-a7718638-76e5-488b-9e4c-6b0a656d83ed.png)

