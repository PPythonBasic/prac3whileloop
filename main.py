# นำข้อมูลจากโจทย์ก่อนหน้ามาหรือสร้างใหม่เองก็ได้ ตัวอย่างเช่น
list_data = [{"name":"a"},{"name":"b"}, ...................]

# ทำการ while loop ตัวอย่างเช่น แก้ไขให้รันได้ปกติ
while    :
    name_user = input("Enter name: ")
    if name_user == True:
        for i in range(len(list_data)):
            if list_data[i]["name"] == name_user:
                print(list_data[i])
                break
    break