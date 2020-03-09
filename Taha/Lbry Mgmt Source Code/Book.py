class Book():

    def __init__(self,ISBN,name,author,publisher,price,quantity):
        self.ISBN = ISBN
        self.name = name
        self.author = author
        self.publisher = publisher
        self.price = price
        self.quantity = quantity
        

    def BookDetails(self):
        pass

if __name__ == " __main__ ":
    book = Book(1234,'abc','sfd','wefew',234,123)
    book.BookDetails()


       