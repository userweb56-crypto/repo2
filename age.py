try:
    num = int(input("Enter your age: "))
    if num >= 18:
        print("You are eligible")
    else:
        print("You are not eligible")
except ValueError:
    print("Enter a valid integer for your age.")
