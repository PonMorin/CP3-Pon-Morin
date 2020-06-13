from tkinter import *

def LeftClickButton(event):
    aswer = float(textboxWeight.get()) / ((float(textboxHight.get())/100)**2)

    if aswer < 18.5:
        labelBMI.configure(text = "ผอมเกินไป")

    elif 18.5 <= aswer < 22.9:
        labelBMI.configure(text = "น้ำหนักปกติ เหมาะสม")

    elif 23 <= aswer < 24.9:
        labelBMI.configure(text = "น้ำหนักเกิน")

    elif 25 <= aswer < 29.9:
        labelBMI.configure(text = "อ้วน")

    elif aswer > 30:
        labelBMI.configure(text = "อ้วนมาก")



    labelresult.configure(text = float(textboxWeight.get()) / ((float(textboxHight.get())/100)**2))

window = Tk()

labelHight = Label(window,text = "ส่วนสูง (cm)")
labelHight.grid(row = 0 , column = 0)
textboxHight = Entry(window)
textboxHight.grid(row = 0 , column = 1)

labelWeight = Label(window,text = "น้ำหนัก (kg)")
labelWeight.grid(row = 1 , column = 0)
textboxWeight = Entry(window)
textboxWeight.grid(row = 1 , column = 1)

calculateButton = Button(window,text = "คำนวณ")
calculateButton.bind("<Button-1>",LeftClickButton)
calculateButton.grid(row = 2 , column = 0)

labelBMI = Label(window,text = "BMI")
labelBMI.grid(row = 2 , column = 1)

labelresult = Label(window,text = "BMI")
labelresult.grid(row = 3 , column = 1)

window.mainloop()
