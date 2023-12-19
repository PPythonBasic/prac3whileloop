- นำตัวแปร list_person มาทำในลักษณะเดิมแต่มีการใช้ While Loop 
- เพื่อรับข้อมูลเข้ามาจากผู้ใช้งานใช้ในการค้นหาชื่อที่ต้องการค้นหาหากผู้ใช้งานไม่กรอกจะให้กรอกจนกว่าจะมีข้อมูล เช่น

```py
list_data = [{"name":"a"},{"name":"b"}]
while True:
    name_user = input("Enter name: ")
    if name_user == True:
        for i in range(len(list_data)):
            if list_data[i]["name"] == name_user:
                print(list_data[i])
                break
    break
```

ลองปรับเอาไปใช้กับโค้ดคุณ
