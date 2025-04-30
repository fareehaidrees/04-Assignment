def main():
    lst = []  
    
    while True:
        value = input("Enter a value: ") 
        
        if value == "":  # If user press enter without typing anything, exit loop
            break
        
        lst.append(value)  # Adding value to the list

    print("Here's the list:", lst)  

if __name__ == '__main__':
    main()