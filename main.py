i=True
while i:
  input("Please enter a File name: ")
  name = (input("\nPlease enter your First and last name: "))
  street = (input("\nPlease enter your street name: "))
  phone = (input("\nPlease enter your phone number including your area code: "))
  #empty line (line 6 for a cleaner look)
  print ()
  print(""+name+", "+street+", "+phone+"")
  while True:
    print("\nwould you like to add another File Y or Yes N for No: ")
      
    option = input("y/n > ")
        
    if option == "y" or option == "Y":
      i=True
      break
          
    elif option == "n" or option == "N":
      print("\nThank you and have a great day")
      i=False
      break
    else:
      print("\nError invalid entry please try again with Y or N\n")
      continue