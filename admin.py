from person import person
class admin(person):

    def __init__(self,admin_name = "admin",admin_password = "admin123"):
        super().__init__(admin_name,admin_password)
        self.admin_name = admin_name
        self.admin_password = admin_password
    
    



