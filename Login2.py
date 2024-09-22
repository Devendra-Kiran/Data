def login():  
    username = input("Enter username: ")  
    password = input("Enter password: ")  
  
    valid_users = ["Deva", "Devendra", "Madhu"]  
    valid_passwords = ["pass1", "pass2", "pass3"]  
  
    if username in valid_users and password == valid_passwords[valid_users.index(username)]:  
        print("Login successful!")  
     
    else:  
        print("Invalid username or password.")  

login() 
