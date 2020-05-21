from person import person
from librarian import librarian
from book import book


if __name__ == '__main__':
    
    print("Running")
    libObj1 = person("Omar","Shahen77")
    libObj2 = person("Reda","Reda200")
    obj = librarian("Omar","Shahen88","omarReda@gmail.com","MoustafaKamel","Alexandria",1065630331)
    bookObj = book("@Omar","The 10X Rule","Grant Cardonr","Dale",7)

    print(bookObj)
    print(obj.get_email())
    
    
    
    