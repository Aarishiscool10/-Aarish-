import sys



def initial_phonebook():
    print("Loading.....")
    rows, cols = int(input("Please enter the number of contacts: ")), 5


    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("/nEnter contacts %d details in the following order (ONLY):" % (i+1))
        print("NOTE * Indicates Mandatory Field")

        print(".../............/......./...LOADING NEXT SECTOR......../......../.............../............../.........../.............../........./...")
        temp = []
        for j in range(cols):

         if j == 0:
               temp.append(str(input("Enter name*: ")))



               if temp[j] == ' ' or temp[j] == '  ':
                   sys.exit("Name is mandatory to go on to next sector")


         if j == 1:
               temp.append(str(input("Enter phone number*: ")))
              
               if temp[j] == ' ' or temp[j] == '  ':
                   sys.exit("Phone number is mandatory to go on to next sector")


         if j == 2:
               temp.append(str(input("Enter email*: ")))
              
               if temp[j] == ' ' or temp[j] == '  ':
                   sys.exit("email is mandatory to go on to next sector")

