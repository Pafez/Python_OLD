login=input('Do You want to Log In')
if login.upper() == 'Yes':
   name= input('Please Enter Your Username')
   passw= input('Please give me your Password')
   if passw=='SAADAT' :
       print ( 'Thank you! You are in')
   else:
       print( 'Sorry!It is incorrect')
elif login.upper()=='No':
    print('Thank you! You can go back.')
else:
    print('Invalid syntax')