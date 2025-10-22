num = input("Enter a integer: ")

match num.isnumeric():
    case True:
        num = int(num)
        print(f"Remainder when {num} is divided by 5 is {num % 5}")
    case False:
        print("Invald input")
    case _:
        print("Something went wrong")
