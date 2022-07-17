def iphone():
 print(" unlock your device ")
password_input = input(" please enter your password ")
password = "6862"
number = {}
if password_input == password:
  print("1.PHONE :")
  print ("2.safari:")
  print ("3.message:")
  print("4.music:")
  d = int (input(" please enter your choice"))
  if d ==1:
   print("5. Add contact ")
   print("6. Remove a phone number ")
   e = int(input("please enter the choice"))
  if e==5:

    print(" New contact")
    name = input("Name:")
    phone = input(" number:")
    number[name] = phone
  elif e == 6:
   print("delete name and phone number ")
   name= input("name ")
   if name in number :
     del number[name]
   else:
    print(name,"was not found")
    iphone()
















