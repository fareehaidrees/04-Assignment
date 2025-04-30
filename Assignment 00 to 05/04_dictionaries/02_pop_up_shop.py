def main():
    fruits = {"apple": 1.5, "durian": 50, "jackfruit": 80, "kiwi": 1, "rambutan": 1.5, "mango": 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        quantity = int(input("How many (" + fruit_name + ") do you want to buy? : "))
        total_cost += (price * quantity)
    
    print("Your total is $" + str(total_cost))

if __name__ == '__main__':
    main()