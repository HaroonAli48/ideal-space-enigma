a0331={'Name':'Haseeb','DOB':'09 May,2008','age':'16','Origin':'shehri','City':'faisalabad'}
a0332={'Name':'Mahad','DOB':'18 August,2009','age':'14','Origin':'paindu','Pind':'Pandura'}
a0333={'Name':'Haroon','DOB':'10 January,2011','age':'13','Origin':'shehri','City':'faisalabad'}

b="gandi bo"

while (b!="NO"):
    print("Enter your ID:")
    i=input()
    if(i=='a0331'):
         print("What do you want")
         a=input()
         if(a=='name'):
           value=a0331['Name']
           print(value)
         elif(a=='DOB'):
            value=a0331['DOB']
            print(value)
         elif(a=='city'):
           value=a0331['City']
           print(value)
         elif(a=='origin'):
           value=a0331['Origin']
           print(value)
         elif(a=='age'):
           value=a0331['age']
           print(value)
         else:
            print("Invalid command.Please enter \"name\",\"DOB\",\"city\",\"origin\".")
    elif(i=='a0332'):
       print("What do you want")
       a=input()
       if(a=='name'):
          value=a0332['Name']
          print(value)
       elif(a=='origin'):
          value=a0332['Origin']
          print(value)
       elif(a=='pind'):
          value=a0332['Pind']
          print(value)
       elif(a=='age'):
           value=a0332['age']
           print(value)  
       elif(a=='DOB'):
           value=a0332['DOB']
           print(value)
       else:
           print("Invalid command.Please enter \"name\",\"DOB\",\"city\",\"origin\".")
    elif(i=='a0333'):
       print("What do you want")
       a=input()
       if(a=='name'):
          value=a0333['Name']
          print(value)
       elif(a=='DOB'):
         value=a0333['DOB']
         print(value)        
       elif(a=='age'):
           value=a0333['age']
           print(value)
       elif(a=='city'):
          value=a0333['City']
          print(value)
       elif(a=='origin'):
          value=a0333['Origin']
          print(value)
       else:
          print("Invalid command.Please enter \"name\",\"DOB\",\"city\",\"origin\".")
    else:
        print("Invalid ID")
    print("Enter \"YES\" for more information\n otherwise enter \"NO\"" ) 
    b=input()
if(b=='NO'):    
    print("Regards,\n Muhammad Haseeb Ali(Main Programmer)\n Muhammad Haroon Ali(Professional Programmer)")

