import Customer
import Customer_List


# Library Management System
# this program will manage a library, it will have
# the following options :
# 1) the option to add or delete customers
# 2) to add or remove record of a book that has been borrowed
# ----------------------------------------------------------------------------------------------------------------------
# prints the help guide for the user

def print_commands():
    print("""To add or remove a customer, write down: 
    "[+/-] [Customer last name] [ID number]"
    
    To add or remove record of a book for a customer, write down: 
    "[Customer last name] [ID number] [Book code] [+/-]"
    
    To see who have the most books, write down:
    "[?] [!]"
    
    To search fo a certain book among all of the customers, write down:
    "[?] [Book code]"
    
    To check what books a certain customer currently has, write down:
    "[?] [ID number]"
    
    To print customer list
    [?] [list]
    
    to print the oldest/newest customer
    [?] [newest/oldest]
    
    To quit, just write "quit" 
    
    IMPORTANT NOTE: write the whole sentence with spaces in between before applying the command
    """)
    # ------------------------------------------------------------------------------------------------------------------


# analysing input line that receive from the user
# and sends it tot he relevant functions of the program

def line_parser(line, customer_list):
    words = line.split(" ")  # split the line into separate lines
    if words[0] == '+':  # checks if needs to add a new customer
        print(f"You are about to add {words[1]} as a new customer")
        cus_to_add = Customer.Customer.create_new_customer(words[1], words[2])
        if customer_list.find_by_id(cus_to_add.id_number):
            print("ID number is already in use, cannot add another one with the same ID!")
            return
        customer_list.add_customer(cus_to_add)
        customer_list.print_list()
    elif words[0] == '-':  # checks if needs to remove an exist customer
        print(f"You are about to remove {words[1]} from the list")
        cus_to_del = Customer.Customer.create_new_customer(words[1], words[2])
        del_customer = customer_list.is_exist(cus_to_del)
        customer_list.delete_customer(del_customer)
        customer_list.print_list()
    elif words[0] == '?':  # checks for other options
        if words[1] == '!':  # who borrowed the most books
            print("Who have the biggest number of books: ")
            customer_list.who_have_max_num_of_books()
        elif words[1] == "oldest":
            if customer_list.get_head() is not None:
                customer_list.get_head().print_info()
        elif words[1] == "newest":
            if customer_list.get_head() is not None:
                customer_list.get_tail().print_info()
        elif len(words[1]) == 6:  # looking for a book with all of the customers
            print(f"Who have this book ({words[1]}): ")
            customer_list.who_holds_this_book(words[1])
        elif words[1] == "list":  # check is the user want to print the list
            customer_list.print_list()
        else:  # checks whats books the customer holds(looking by id number)
            current_cus = customer_list.find_by_id(words[1])
            if current_cus is not None:
                print(f"The id number {current_cus.id_number} belongs to {current_cus.last_name}")
                current_cus.print_book_list()
            else:
                print(f"Cannot find customer with this id number({words[1]})")
    else:  # manage records
        current_customer = Customer.Customer.create_new_customer(words[0], words[1])
        add_or_remove = customer_list.is_exist(current_customer)
        if add_or_remove is None:  # checks if the user is in the list
            print(f"The customer {current_customer.last_name} is not in the list!")
            return
        if words[3] == '+':  # add a record to the customer
            add_or_remove.add_record(words[2])
            add_or_remove.print_book_list()
        else:  # removes a record from the user
            add_or_remove = customer_list.is_exist(current_customer)
            add_or_remove.delete_record(words[2])
            add_or_remove.print_book_list()
    # ------------------------------------------------------------------------------------------------------------------


print("""Welcome to the Library Management System
you can type "help" any time to see the commands""")

cus_list = Customer_List.Customer_List()
command = input()
while command != 'quit':
    if command == 'help':
        print_commands()
    else:
        line_parser(command, cus_list)
    command = input()
