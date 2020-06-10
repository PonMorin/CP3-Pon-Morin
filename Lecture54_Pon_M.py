def LoginSection():
    Username = input("ใส่Usernameของคุณ: ")
    password = input("ใส่passwordของคุณ: ")
    if Username == "LOL" and password == "1234":
        return Showmenu()
    elif Username != "LOL" and password != "1234":
        return LoginSection()

def Showmenu():
    print("----CATKIN SHOP----")
    print("1.Vat Calculator")
    print("2.Price Calculator")
    return menuSelect()

def menuSelect():
    menu = int(input("ใส่เลขMenu: "))
    if menu == 1:
        return Vatcal(int(input("กรุณาใส่ตัวเลข : ")))
    
    elif menu == 2:
        return PriceCal()
        

def Vatcal(totalprice):
    vat = 7
    result = totalprice+((totalprice*vat)/100)
    return result

def PriceCal():
    cost = int(input("ใส่ราคาสินค้าที่จะคำนวณ :"))
    cost2 = int(input("ใส่ราคาสินค้าที่จะคำนวณชิ้นที่2 :"))
    return Vatcal(cost + cost2)

print(LoginSection())
