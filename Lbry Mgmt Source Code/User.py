class User:
    def __init__(self,isAdmin,book):
        self.isAdmin = isAdmin
        self.book = book

    def SearchBook(self,book):
        pass
    def RaiseRequest(self,book):
        pass

if __name__ == "__main__":
    user = User()
    user.SearchBook()
    user.RaiseRequest()