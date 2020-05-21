class librarian:
    
    
    def __init__(self,name,password,email,address,city,contactNo):
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.city = city
        self.contactNo = contactNo
    
    
    def set_name(self,name):
        self.name = name  
    def get_name(self):
        return self.name
    
    def set_password(self,password):
        self.password = password
    def get_password(self):
        return self.password
    
    def set_email(self,email):
        self.email = email
    def get_emai(self):
        return self.email
    
    def set_address(self,address):
        self.address = address
    def get_address(self):
        return self.address
    
    def set_city(self,city):
        self.city = city
    def get_city(self):
        return self.city
    
    def set_contactNo(self,contactNo):
        self.contactNo = contactNo
    def get_contactNo(self):
        return self.contactNo
    
    
    def __str__(self):
        return self.name + " " + self.email + " " + self.address + " " + self.city + " " + str(self.contactNo)
    
        
        
    
    
    
    
    
    
    
    