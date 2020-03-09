class Transaction:
    def __init__(self):
        super().__init__()
        self.issueDate = issueDate
        self.returnDate = returnDate
        self.bookId = bookId
        self.studentId = studentId
        self.librarianId = librarianId

    def LogTransaction(self):

if __name__ == "__main__":
    transaction = Transaction()
    transaction.LogTransaction()    