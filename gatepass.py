import getpass  
  
users = {'Keshava': 'pass123', 'Hemu': 'pass456', 'Deva': 'pass789'}  
  
username = input('Enter username: ')  
password = getpass.getpass('Enter password: ')  
  
if username in users and users[username] == password:  
    print('Access granted')  
else:  
    print('Access denied')  