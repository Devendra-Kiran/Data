users = {'Devendra': 'Pass1', 'Kiran': 'Pass2', 'Madhu': 'Pass3'}  
  
def login():  
    username = input("Enter your username: ")  
    password = input("Enter your password: ")  
  
    if username in users and users[username] == password:  
        print("Login successful!")  
    else:  
        print("Invalid username or password. Please try again.")  
  
login()  