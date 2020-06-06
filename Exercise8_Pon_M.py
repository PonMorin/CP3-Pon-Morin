Username = input("ใส่Usernameของคุณ: ")
password = input("ใส่passwordของคุณ: ")

if Username == "LOL" and password == "1234":
    print("เข้าสู่ระบบ")
    print("----CATKIN SHOP----")
    
    print("0.ไม่ต้องการซื้อ")
    print("1.Book 120 THB")
    print("2.Water 7 THB")
    print("3.Headphone 6500 THB")
    print("4.Calculator 1500 THB")

    select = int(input("กรุณาใส่เลขที่ต้องการซื้อ :"))
    if select == 1:
        num1 = int(input("ใส่จำนวณที่ต้องการ: "))
        print("ราคาทั้งหมด: ",120*num1)
        print("Thank you")
    
    elif select == 2:
        num2 = int(input("ใส่จำนวณที่ต้องการ: "))
        print("ราคาทั้งหมด: ",7*num2)
        print("Thank you")

    elif select == 3:
        num3 = int(input("ใส่จำนวณที่ต้องการ: "))
        print("ราคาทั้งหมด: ",6500*num3)
        print("Thank you")

    elif select == 4:
        num4 = int(input("ใส่จำนวณที่ต้องการ: "))
        print("ราคาทั้งหมด: ",1500*num4)
        print("Thank you")
    
    elif select == 0:
        print("Thank you")
