class Library:
    def __init__(self,list,name):
        self.booksList = list
        self.name = name
        self.lendDict = {}
    def displayBooks(self):
        print(f"we have such a good books in Library: {self.name}")
        for book in self.booksList:
            print(book)
    def lendBook(self, user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-book database has been updated.you can take book now")
        else:
            print(f"book is already used by {self.lendDict[book]}")


    def addBook(self,book):
        self.booksList.append(book)
        print("book has been added to book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ =='__main__':
    mansi = Library(['python', 'c','java','machine learning'], "Mansi")
    while(True):
        print(f"Welcome to {mansi.name}library. Enter ur choice to continue")
        print("1. Display a Books")
        print("2. Lend a Books")
        print("3. Add a2 Books")
        print("4. Return a Books")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice ==1:
            mansi.displayBooks()
        elif user_choice ==2:
            book = input("Enter the name of the book you lend:")
            user = input("enter your name")
            mansi.lendBook(user, book)

        elif user_choice == 3:
            book = input("enter name of the book you have to add:")
            mansi.addBook(book)

        elif user_choice == 4:
            book = input("enter the name of the book you want  return:")
            mansi.returnBook(book)

        else:
            print("not a valid option")

        print("press Q to quit and C to continue")
        user_choice2 =""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 =="q":
                exit()
            elif user_choice2 =="c":
                continue





