my_dict = {"Num": [98, 26, 35, 234, 416345, 45, 345, 4, 234, 29]}

user_input = input("Enter a number: ")

chosen_number = int(user_input)

if chosen_number in my_dict["Num"]:

    print(f"The number {chosen_number} appears in the list!")
else:
    print("That number is not in the list.")
