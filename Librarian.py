from person import person
class librarian(person):
    
    
    def __init__(self,name,password,email,address,city,contactNo):
        
        
        super().__init__(name,password)
        self.email = email
        self.address = address
        self.city = city
        self.contactNo = contactNo
    
    
        
    