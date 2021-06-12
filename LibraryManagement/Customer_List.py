import Customer

class Customer_List:
    # creates a new list of customers(the constructor)
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_customers = 0
    # ------------------------------------------------------------------------------------------------------------------
    # checks if the customer is head or tail and sends it to the relevant function
    # if not head or tail, switch the pointers for the previous and the next customer
    # in the list
    # Running Time = O(1)

    def delete_customer(self, del_customer):
        if del_customer is None:
            print("Customer does not exist!")
            return
        if del_customer.prev is None:  # if it's the head of the list
            self.del_first()
        elif del_customer.next is None:  # if it's the tail of the list
            self.del_last()
        else:
            del_customer.next.prev = del_customer.prev
            del_customer.prev.next = del_customer.next
            self.num_of_customers -= 1
    # ------------------------------------------------------------------------------------------------------------------
    # deletes the head of the list and makes the next customer to be the new head
    # Running Time = O(1)

    def del_first(self):
        if self.is_empty():
            print("The list is empty!")
            return
        self.head = self.head.next
        self.num_of_customers -= 1

        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None
    # ------------------------------------------------------------------------------------------------------------------
    # deletes the tail of the list and makes the previous customer to be the new tail
    # Running Time = O(1)

    def del_last(self):
        if self.is_empty():
            print("The list is empty!")
            return
        self.tail = self.tail.prev
        self.num_of_customers -= 1

        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
    # ------------------------------------------------------------------------------------------------------------------
    # add a new customer to the list
    # Running Time = O(1)

    def add_customer(self, new_customer):
        if self.is_exist(new_customer) is not None:  # checks if the customer is not already in the list
            print("Customer is already exist!")
            return
        if self.head is None:  # if the list is empty
            self.head = new_customer
            self.tail = new_customer
            new_customer.prev = new_customer.next = None
        else:  # if the list is not empty, add to tail and make the new customer to be the tail
            self.tail.next = new_customer
            new_customer.prev = self.tail
            self.tail = self.tail.next
        self.num_of_customers += 1
    # ------------------------------------------------------------------------------------------------------------------
    # print the customers in the list
    # going through all the customers(n)
    # Running Time = O(1)

    def print_list(self):
        if self.num_of_customers == 0:  # checks if the list is empty
            print("The Customer list is empty!")
            return
        print("Customer List: ")
        current_cus = self.head  # pointer to traverse with
        index = 1  # to numerate the list
        while current_cus is not None:
            print(f"{index}) Last Name: {current_cus.last_name} ID Number: {current_cus.id_number}")
            index += 1
            current_cus = current_cus.next

    # ------------------------------------------------------------------------------------------------------------------
    # returns if the list is empty
    # Running Time = O(1)

    def is_empty(self):
        return self.num_of_customers == 0
    # ------------------------------------------------------------------------------------------------------------------
    # returns the length\size of the list(how many customers are in the list)
    # Running Time = O(1)

    def get_len(self):
        return self.num_of_customers
    # ------------------------------------------------------------------------------------------------------------------
    # print what customer holds the biggest amount of books at the moment
    # going through all of the customers(n)
    # Time Running = O(n)

    def who_have_max_num_of_books(self):
        biggest_num_of_books = 0
        current_cus = self.head  # to traverse with
        while current_cus is not None:
            if current_cus.get_num_of_book() >= biggest_num_of_books:  # if bigger than the current biggest amount
                biggest_num_of_books = current_cus.get_num_of_book()   # swap if needed
            current_cus = current_cus.next
        if biggest_num_of_books == 0:
            print("No one has books!")
            return  # if no one has books, can stop here
        current_cus = self.head  # initiate the traverser again to be the head
        print(f"The Customers who have the biggest number of books ({biggest_num_of_books}) are: ")
        # print anyone who has the biggest amount of books
        while current_cus is not None:
            if current_cus.get_num_of_book() == biggest_num_of_books:
                print(current_cus.last_name)
            current_cus = current_cus.next
    # ------------------------------------------------------------------------------------------------------------------
    # checks all of the customer if have a certain book
    # going through all of the customers(n)
    # and for each customer, going through all of the books(m)
    # Running Time = O(n*m)

    def who_holds_this_book(self, book_name):
        current_cus = self.head  # to traverse with
        is_someone_have_it = False  # to keep track if anyone has this book
        while current_cus is not None:
            if current_cus.is_have_book(book_name):
                print(f"{current_cus.last_name} has this book {book_name}")
                is_someone_have_it = True
            current_cus = current_cus.next

        if not is_someone_have_it:  # if no one has this book, print notification about it
            print("No one holds this book")
    # ------------------------------------------------------------------------------------------------------------------
    # searches for a customer by an id number, going through all of the customers(n)
    # Running Time = O(n)

    def find_by_id(self, id_number):
        current_cus = self.head
        while current_cus is not None:
            if current_cus.id_number == id_number:
                return current_cus
            current_cus = current_cus.next
        return None
    # ------------------------------------------------------------------------------------------------------------------
    # equals and customer object to all of the existing customers in the list
    # returns the customer from the list if found one
    # going through all of the customers(n)
    # Running Time = O(n)

    def is_exist(self, cus_to_check):
        current_cus = self.head
        while current_cus is not None:
            if current_cus.last_name == cus_to_check.last_name and current_cus.id_number == cus_to_check.id_number:
                return current_cus
            current_cus = current_cus.next
        return None
    # ------------------------------------------------------------------------------------------------------------------
    # returns the head of the list
    # Running Time = O(1)

    def get_head(self):
        if self.head is None:
            print("There are no customers in the list")
            return None
        return self.head
    # ------------------------------------------------------------------------------------------------------------------
    # returns the tail of the list
    # Running Time = O(1)

    def get_tail(self):
        if self.tail is None:
            print("There are no customers in the list")
            return None
        return self.tail
    # ------------------------------------------------------------------------------------------------------------------


