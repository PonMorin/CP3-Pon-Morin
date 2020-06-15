class Customer:
    name = ""
    lastname = ""
    age = 0

    def addcart(self):
        print("Added to ",self.name,self.lastname,"'s Carts")

customer1 = Customer()
customer1.name = "P"
customer1.lastname = "M"
customer1.addcart()

customer2 = Customer()
customer2.name = "Chon"
customer2.lastname = "Ct"
customer2.addcart()

customer3 = Customer()
customer3.name = "Game"
customer3.lastname = "Thi"
customer3.addcart()

customer4 = Customer()
customer4.name = "Gunn"
customer4.lastname = "Vi"
customer4.addcart()
