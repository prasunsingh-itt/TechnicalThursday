class Transaction:
    def __init__(self,issueDate,returnDate,bookId,studentId,librarianId):
        super().__init__()
        self.issueDate = issueDate
        self.returnDate = returnDate
        self.bookId = bookId
        self.studentId = studentId
        self.librarianId = librarianId

    def LogTransaction(self):
        pass

if __name__ == "__main__":
    transaction = Transaction('23-03-2020','',1,1,1)
    transaction.LogTransaction()    