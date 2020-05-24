from admin import admin
from book import book
from Librarian import librarian
from student import student
class library_system:

    def __init__(self):
        self.librarian_list = []
        self.book_list = []
        self.student_list = []
        self.issued_books_list = []
        self.admin = admin()

        self.librarian_list.append(librarian("Omar","Shahen77","Omar@gmail.com","Moustafa Kamel","Alexandria","01065630331"))
        self.librarian_list.append(librarian("Ahmed","Ahmed77","Ahmed@gmail.com","Smouha","Alexandria","01006615471"))
        self.librarian_list.append(librarian("Youssef","Youssef77","Youssef@gmail.com","Abo 2ER","Cairo","01111185001"))

        self.book_list.append(book("The 10X Rule","Grant Cardone","VIP",7))
        self.book_list.append(book("The 5 AM Club","Robin Sharma","VIP",5))
        self.book_list.append(book("Power of habbit","Reda","VIP",1))
    
    def add_librarian(self,name,password,email,address,city,contact):
        librarianObject = librarian(name,password,email,address,city,contact)
        self.librarian_list.append(librarianObject)
        print('Added Successfully')
    
    def view_librarians(self):
        for i in self.librarian_list:
            print(i)
    
    def delete_librarian(self,librarianID):

        print("Entered Method")
        i = 0
        found = False
        while(i < len(self.librarian_list)):
            print("Entered loop")
            if self.librarian_list[i].get_ID() == librarianID:
                print("Found")
                del self.librarian_list[i]
                print("Deleted Successfully")
                found = True
                return
            i += 1
        if found == False:
            print("This ID does not Exist")
        

    def add_book(self,bookName,bookAuthor,bookPublisher,bookQuantity):

        bookObj = book(bookName,bookAuthor,bookPublisher,bookQuantity)
        self.book_list.append(bookObj)
        print('Book is added Successfully')
    
    def view_books(self):

        for book in self.book_list:
            print(book)

    def issue_book(self,bookName,studentID,studentName,studentContact):
        found = False
        studentObject = student(studentName,studentName,studentContact)
        self.student_list.append(studentObject)
        for book in self.book_list:
            if book.get_book_name() == bookName:
                if book.get_book_quantity() == 0:
                    print("Sorry, All copies are Issued")
                    return
                found = True
                book.set_studentIssue(studentObject)
                book.decrement_book_quantity()
                self.issued_books_list.append(book)
                print('Book Issued Successfully')

        if found == False:
            print("Not Found")

    def view_issued_books(self):
        for i in self.issued_books_list:
            print(i.get_book_name(), " " , i.get_studentIssue().get_student_name())
            



    def admin_login(self,inputAdminName,inputAdminPassword):
        if inputAdminName != self.admin.get_name() or inputAdminPassword != self.admin.get_password():
            print('Access Denied')
            return
        
        while(True):
        
            print("1.Add Librarian")
            print("2.View Librarian")
            print("3.Delete Librarian")
            print("4.Logout")
            choice = int(input("Choose Option: "))
            if choice == 1:
                librarianName = input("Name: ")
                librarianPassword = input("Password: ")
                librarianEmail = input("Email: ")
                librarianAddress = input("Address: ")
                librarianCity = input("City: ")
                librarianContactNo = input("Contact Number: ")
                self.add_librarian(librarianName,librarianPassword,librarianEmail,librarianAddress,librarianCity,librarianContactNo)

            elif choice == 2:
                print("Librarian List:-")
                self.view_librarians()
            
            elif choice == 3:
                librarianID = int(input("Librarian ID: "))
                self.delete_librarian(librarianID)
            
            elif choice == 4:
                return
    
    def librarian_login(self,input_librarian_name,input_librarian_password):


        validName = False
        validPassword = False

        for names in self.librarian_list:
            if names.get_name() == input_librarian_name:         
                validName = True
                break
      
        if validName == False:
            print('This Name doesnot Exist')
            return
       
        for passwords in self.librarian_list:
            if passwords.get_password() == input_librarian_password:
                validPassword = True
                break
  
        if validPassword == False:
            print('Wrong Password')
            return
      
        if validPassword == True and validName == True:
            print('Successful Login')
        #   After Checking Validation
        
        while(True):

            print('1.Add Book')
            print('2.View Books')
            print('3.Issue Book')
            print('4.View Issued')
            print('5.Return Book')
            print('6.Logout')

            choice = int(input('Choose Option: '))

            if choice == 1:

                bookName = input("Book Name: ")
                bookAuthor = input("Book Author: ")
                bookPublisher = input("Book Publisher: ")
                bookQuantity = int(input("Book Quantity: "))
                self.add_book(bookName,bookAuthor,bookPublisher,bookQuantity)
            
            elif choice == 2:

                self.view_books()
            
            elif choice == 3:

                bookName = input("Book Name: ")
                studentName = input("Student Name: ")
                studentID = int(input("Student ID: "))
                studentContact = input("Student Contact: ")
                self.issue_book(bookName,studentID,studentName,studentContact)
            
            elif choice == 4:
                self.view_issued_books()
            


            elif choice == 6:
                break



            
        



    



    

    



        






        





