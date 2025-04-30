def main():
    # Ask the user for a number 
    value = int(input("Enter a number: "))

    # Loop until value is 100 or greater
    while value < 100:
        value *= 2  # Double the value
        print(value, end=" ") 

if __name__ == '__main__':
    main()