menulist = []

def ShowBill():                               #ฟังชั่นแสดงใบเสร็จ
    text = "ลุงแจมเจ้าเก่า"
    print(text.center(20,("-")))
    for i in range(len(menulist)):            #วนloop ตามจำนวนขนาดของเมนู
        print(menulist[i][0],menulist[i][1])

def total():
    print("-----------------")
    Sum = 0
    for j in range(len(menulist)):
        Sum += (menulist[j][1])
    print("Total = ",Sum)
    print("Thank you")



while True:                                  #loop กรอกเมนู และ ราคา
    menuname = input("Enter Menu: ")
    if menuname.lower() == "exit":
        break
    else:
        menuprice = int(input("Price: "))
        menulist.append([menuname,menuprice])

ShowBill()
total()
