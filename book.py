class book:

    def __init__(self,book_name,book_author,book_publisher,book_quantity):
        
        self.book_name = book_name
        self.book_author = book_author
        self.book_publisher = book_publisher
        self.book_quantity = book_quantity
    
    def set_book_name(self,book_name):
        self.book_name = book_name
    def get_book_name(self):
        return self.book_name
    
    def set_book_author(self,book_author):
        self.book_author = book_author
    def get_book_author(self):
        return self.book_author
    
    def set_book_publisher(self,book_publisher):
        self.book_publisher = book_publisher
    def get_book_publisherr(self):
        return self.book_publisher
    
    def set_book_quantity(self,book_quantity):
        self.book_quantity = book_quantity
    def get_book_quantity(self):
        return self.book_quantity
    
    def decrement_book_quantity(self):
        self.book_quantity -= 1
    def increment_book_quantity(self):
        self.book_quantity += 1
    
    def set_studentIssue(self,student):
        self.student_issue = student
    def get_studentIssue(self):
        return self.student_issue
    
    def __str__(self):
        return  self.book_name + " " + self.book_author + " " + self.book_publisher + " " + str(self.book_quantity)
    


    

