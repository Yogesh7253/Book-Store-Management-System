class Book:
    def __init__(self,ID,name,editon,publisher,price):
        self.ID = ID
        self.name = name
        self.edition = editon
        self.publisher = publisher
        self.price = price

    def __str__(self):
        return f"ID : {self.ID} \nName : {self.name} \nEdition : {self.edition} \nPublisher : {self.publisher} \nPrice : {self.price}"

    def set_ID(self,ID):
        self.ID = ID

    def get_ID(self):
        return self.ID
    
    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name 
    
    def set_edition(self,edition):
        self.edition = edition

    def get_edition(self):
        return self.edition
    
    def set_publisher(self,publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher
    
    def set_price(self,price):
        self.price = price

    def get_price(self):
        return self.price




        