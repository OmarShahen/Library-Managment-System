
from LibrarySystem import library_system

if __name__ == '__main__':

    libraryObject = library_system()
    

    while(True):

        print("1.Admin login")
        print("2.Librarian login")
        print("0.Exit")
        choice = int(input("Choose option: "))

        if choice == 1:
            adminName = input("Enter Admin Name: ")
            adminPassword = input("Enter Admin Password: ")
            libraryObject.admin_login(adminName,adminPassword)

        elif choice == 2: 
            librarianName = input("Enter Librarian Name: ")
            librarianPassword = input("Enter Librarian Password: ")
            libraryObject.librarian_login(librarianName,librarianPassword)
            
        elif choice == 0:
            break
        
        else:

            print("There is no other option")
    
    
    
    