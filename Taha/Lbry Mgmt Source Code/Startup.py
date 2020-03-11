from Librarian import Librarian
from Student import Student
class Startup:
    role = 0
    choice = 'Y'
    print("\n\nWelcome  To Library Management \n\n")
        
    role = int(input("Please Enter the Role \n1.Admin \n2.Student \nYour Role : "))    
    if (role == 1):
        while(choice != 'N'):
            choice =input("\n\nPlease Enter the operation to be performed. \n1.Add USer \n2.Delete User \n3.Add Book \n4.Delete Book \n5.Issue Book \n6.Generate Fine \nPress N to logout \nYour Chice : ")
            if (choice == '1'):
                Librarian.AddUSer();
            elif (choice == '2'):
                Librarian.DeleteUser()
            elif (choice == '3'):
                Librarian.AddBook()
            elif (choice == '4'):
                Librarian.DeleteBook()
            elif (choice == '5'):
                Librarian.IssueBook()
            elif (choice == '6'):
                Librarian.GenerateFine()

    elif(role == 2):
        while (choice != 'N'):
            choice = input("\n\nPlease Enter the operation to be performed. \n1.Borrow Book \n.2.Return Book \n3.Pay Fine \nPress N to logout \nYour Chice : ")
            if(choice == '1'):
                Student.Borrow_Book()
            elif(choice == '2'):
                Student.Return_Book()
            elif(choice == '3'):
                Student.Pay_Fine()
    

startup = Startup()
