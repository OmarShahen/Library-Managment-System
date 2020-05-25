class student:

    def __init__(self,student_name,student_ID,student_contact):
        self.student_name = student_name
        self.student_ID = student_ID
        self.student_contact = student_contact
    
    def set_student_name(self,name):
        self.student_name = name
    
    def get_student_name(self):
        return self.student_name
    
    def set_student_ID(self,id):
        self.student_ID = id
    
    def get_student_ID(self):
        return self.student_ID
    
    def set_student_contact(self,contact):
        self.student_contact = contact
    def get_student_contact(self):
        return self.student_contact
    
    def __str__(self):
        return self.student_name + " " + str(self.student_ID)

