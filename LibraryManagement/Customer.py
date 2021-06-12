class Customer:
    # creates a new customer(the constructor)
    def __init__(self, last_name, id_number):
        self.last_name = last_name
        self.id_number = id_number
        self.books = []  # the books the customer currently holds
        self.next = None  # points to the next customer
        self.prev = None  # points to the prev customer
    # ------------------------------------------------------------------------------------------------------------------
    # check if a customer have a certain book
    # going through all of the books(n) if needed
    # Running Times = O(n)

    def is_have_book(self, book_name):
        if len(self.books) == 0:
            return False
        for book in self.books:
            if book_name == book:
                return True
        return False
    # ------------------------------------------------------------------------------------------------------------------
    # returns the numbers of books the customer have
    # which means the length of the array
    # len function in python cost O(1)
    # Running Time = O(1)

    def get_num_of_book(self):
        return len(self.books)
    # ------------------------------------------------------------------------------------------------------------------
    # creates and returns a new customer object
    # Running Times = O(1)

    @staticmethod
    def create_new_customer(last_name, id_number):
        new_customer = Customer(last_name, id_number)
        return new_customer
    # ------------------------------------------------------------------------------------------------------------------
    # print the all the books the customer currently has
    # Running Time = O(n)

    def print_book_list(self):
        if len(self.books) == 0:
            print(f"{self.last_name} has no books")
            return
        print(f"{self.last_name} borrowed {len(self.books)} books: ")
        for i in range(0, len(self.books)):
            print(f"{i + 1}) {self.books[i]}")
    # ------------------------------------------------------------------------------------------------------------------
    # looks and removes a record from the books  array
    # Running Times = O(n)

    def delete_record(self, book_name):
        for book in self.books:
            if book == book_name:
                self.books.remove(book)
    # ------------------------------------------------------------------------------------------------------------------
    # add a new record to the customer books array
    # Running Time = O(1)

    def add_record(self, book_name):
        if book_name in self.books:
            print(f"Customer has already have this book ({book_name})")
            return
        if len(self.books) < 10:    # if the customer has less than 10 books, allow another one
            self.books.append(book_name)
        else:  # if the customer has more than 10 books, don't allow another one
            print("Customer has reached 10 books so another book cannot be taken")

    # ------------------------------------------------------------------------------------------------------------------
    # print information about the customer
    # going through all of the books(n) if needed
    # Running Time = O(n)

    def print_info(self):
        print(f"Last name: {self.last_name}\nID number: {self.id_number}")
        self.print_book_list()
    # ------------------------------------------------------------------------------------------------------------------
