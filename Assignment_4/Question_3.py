import random

choice = 'y'
while choice == 'y':
    print("Press 1 - To create a list of n integers.")
    print("Press 2 - The display the list if elements.")
    print("Press 3 - Insert an element in a specific position.")
    print("Press 4 - Delete an element in a given position.")
    print("Press 5 - Exit.")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            n = int(input("Enter number of elements: "))
            arr = [random.randint(1, 100) for _ in range(n)]
            print(arr, "\n")
        case 2: 
            print(f"The list is: {arr}\n")
        case 3:
            pos = int(input("Enter index to insert: "))
            val = int(input("Enter an integer: "))
            arr.insert(pos, val)
            print("\n")
        case 4:
            pos = int(input("Enter position: "))
            if 0 <= pos <= len(arr):
                arr.pop(pos)
                print("\n")
        case 5:
            choice = 'n'
            choice.lower()
        case _:
            print("Invalid choice!")

print("Thank you!")
