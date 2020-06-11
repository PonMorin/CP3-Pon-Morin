menulist = []
Pricelist = []

def ShowBill():                               #ฟังชั่นแสดงใบเสร็จ
    text = "ลุงแจมเจ้าเก่า"
    print(text.center(20,("-")))
    for i in range(len(menulist)):            #วนloop ตามจำนวนขนาดของเมนู
        print(menulist[i],Pricelist[i])

def total():                                  #ฟังชั่นคิดเงินรวม
    print("-----------------")
    Sum = 0
    for j in Pricelist:                       #loop บวกราคาตามlistสินค้า
        Sum += j
    print("Total ",Sum)
    print("Thank you")



while True:                                  #loop กรอกเมนู และ ราคา
    menuname = input("Enter Menu: ")
    if menuname.lower() == "exit":
        break
    else:
        menuprice = int(input("Price: "))
        menulist.append(menuname)
        Pricelist.append(menuprice)

ShowBill()
total()
