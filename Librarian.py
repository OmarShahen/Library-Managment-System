from person import person
class librarian(person):

    idCounter = 1
    
    
    def __init__(self,name,password,email,address,city,contactNo):
              
        super().__init__(name,password)
        self.id = librarian.idCounter 
        self.email = email
        self.address = address
        self.city = city
        self.contactNo = contactNo
        librarian.idCounter += 1
    
    def get_ID(self):
        return self.id
    
    def __str__(self):
        return self.name + " " + self.email + " " + self.address + " " + self.city + " " + str(self.contactNo)+ " " + str(self.id)

    
    
        
    