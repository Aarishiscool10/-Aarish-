import sys



def initial_phonebook():
    print("Loading.....")
    rows, cols = int(input("Please enter the number of contacts: ")), 5


    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("/nEnter contacts %d details in the following order (ONLY):" % (i+1))
        print("NOTE * Indicates Mandatory Field")

        print(".../............/......./...LOADING NEXT SECTION......../......../.............../............../.........../.............../........./...")
        temp = []
        for j in range(cols):


           if j == 0:
               temp.append(str(input("Enter name*: ")))