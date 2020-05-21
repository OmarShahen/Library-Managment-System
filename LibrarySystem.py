from admin import admin
from book import book
from librarian import librarian
class library_system:

    def __init__(self):
        self.librarian_list = []
        self.book_list = []
        self.admin = admin()
    
    def add_librarian(self,name,password,email,address,city,contact):
        librarianObject = librarian(name,password,email,address,city,contact)
        self.librarian_list.append(librarianObject)
    
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
            

            

            elif choice == 0:
                return 
    

    



        






        





