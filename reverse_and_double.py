def reverse_and_double():
    x = input("Enter a three-digit number: ")

    if len(x) == 3 and x.isdigit():
        reversed_x = int(x[::-1])
        print("Reversed number:", reversed_x)
        print("Double of reversed number:", reversed_x * 2)
    else:
        print("Invalid input. Please enter exactly three digits.")

reverse_and_double()
