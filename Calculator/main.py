def get_input():
    return input("What do you want to do?\n")

def get_str_as_array(input_str :str):
    return input_str.split(' ')

def calculate(str_arred):
    num1 = str_arred[0]
    num2 = str_arred[2]
    if(num1.isdigit() and num2.isdigit()):
        num1 = int(num1)
        num2 = int(num2)
    else:
        print('numbers are expected\n')
        return None
    return get_answer(num1,num2,str_arred[1])

def get_answer(num1,num2,command):
    if(command == '+'):
        return num1 + num2
    if(command == '-'):
        return num1 - num2
    if(command == '/'):
        return num1 / num2
    if(command == '*'):
        return num1 * num2


print(float(calculate(['5','/','2'])))