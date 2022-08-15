def print_multiplication_table():
    for row_index in range(1,10):
        print_row(row_index)
        print()

def print_row(row_index):
    print_row_label(row_index)
    for col_index in range(1,21):
        print_number(row_index*col_index)
        

def print_row_label(label):
    print(' ', label, "|", end = "")

def print_number(number):
    if number<10:
        print(" ", end="")
    if number<100:
        print(" ", end="")
    print(number, end=" ")





f()