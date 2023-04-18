#my assignment
class Author:
    list_of_authors = []
    def __init__(self, author= {}) -> None:
        self.author = author
        self.list_of_authors.append(self.author)
    def listAuthors(self):
        print(self.list_of_authors)
class Book(Author):
    all_book = []
    def __init__(self, mybook={}) -> None:
        self.mybook = mybook
        self.all_book.append(self.mybook)
    def printBook(self):
        print(self.mybook)
    def listAllBooks(self):
        print(self.all_book)
    def removeBook(self, name=''):
        for i in self.all_book:
            if str(i["name"]) == str(name):                
                self.all_book.remove(i)
        print(self.all_book)
    def searchForBook(self, txt=''):
        s = []
        x = ''
        for i in self.all_book:
            if str(i["name"]) == str(txt) or str(i["date"])== str(txt):
                s.append(i)
                # break
            else:
                x = f'Book with details {txt} not found...'
                # break
        
        if len(s):
            print(s)
        else:
            print(x)

class FictionBook(Book):
    def __init__(self, mybook={}) -> None:
        super().__init__(mybook)
        self.mybook["type"] = "fiction"
class NonFictionBook(Book):
    def __init__(self, mybook={}) -> None:
        super().__init__(mybook)
        
        self.mybook["type"] = "non-fiction"
        
class Inventory(FictionBook, NonFictionBook):
    def __init__(self, mybook={}, typ='') -> None:
        super().__init__(mybook)
        if typ==str('f'):
            mybook['type'] = 'fiction'
        else:
            mybook['type'] =  'non-fiction'




inventory = Inventory({"name":"mill", "date":"8039403"}, "f")  
def menu():
    global inventory;
    print("######     menu      #####")
    print("Press 1 to Add a book")
    print("Press 2 to List books")
    print("Press 3 to search for a book")
    print("press 4 to delete a book")
    print("press 5 to display menu")
    print("press 6 to exit")
    print("-------------------------------------------------")
    x = input("Enter you choice:\t")
    if x == "1":
        name = input("Enter Name:\t")
        isbn = input("Enter ISBN:\t")
        typ = input("Enter Types:\t")
        date = input("Enter Date:\t")

        inventory = Inventory({"name": name, "date":date, "isbn":isbn}, typ)
        # write_to_file(str(inventory))
        menu()
    elif x == "2":
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        inventory.listAllBooks()
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        menu()
    elif x == "3":
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        p = input("Type name or date or isbn for book to search: \t")
        inventory.searchForBook(p)
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        menu()
    elif x == "4":
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        b = input("Enter book to be delete:\t")
        inventory.removeBook(b)
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        menu()
    elif x=="5":
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        menu()
    else:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        print("You exited bye!...")
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        exit()
# def write_to_file(txt):
#     file1 = open('books.txt', 'w')
#     file1.writelines(txt)
#     file1.close()
if __name__ == "__main__":   
    
    menu()
