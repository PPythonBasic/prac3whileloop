# นำข้อมูลจากโจทย์ก่อนหน้ามาหรือสร้างใหม่เองก็ได้ ตัวอย่างเช่น
list_person = list_person = [
    {"name": "Andy", "age": 19, "year_born": 2004, "nick_name": "andy"},
    {"name": "Jane", "age": 24, "year_born": 1999, "nick_name": "jane"},
    {"name": "Ten", "age": 18, "year_born": 2004, "nick_name": "ten"},
    {"name": "Eve", "age": 21, "year_born": 2002, "nick_name": "eve"},
    {"name": "Charlie", "age": 18, "year_born": 2005, "nick_name": "charlie"},
    {"name": "Grace", "age": 25, "year_born": 1998, "nick_name": "grace"},
    {"name": "Deam", "age": 19, "year_born": 2004, "nick_name": "deam"},
    {"name": "Jame", "age": 18, "year_born": 2005, "nick_name": "jame"},
    {"name": "Mark", "age": 19, "year_born": 2004, "nick_name": "mark"},
    {"name": "Ohm", "age": 19, "year_born": 2004, "nick_name": "ohm"}]

# ทำการ while loop ตัวอย่างเช่น แก้ไขให้รันได้ปกติ
while True:
    name_user = input("Enter name: ")
    if name_user == True:
        for i in range(len(list_person)):
            if list_person[i]["name"] == name_user:
                print(list_person[i])
                break
            
                
        break

    
   
        