def add_three_copies(my_list, data):
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    message = input("Enter a message to copy: ")

    # Empty list before modification
    my_list = []
    print("List before:", my_list)

    # Call the function 
    add_three_copies(my_list, message)

    # List after modification
    print("List after:", my_list)

if __name__ == '__main__':
    main()