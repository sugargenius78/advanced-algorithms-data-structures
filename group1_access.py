import re  
# simulate user database
users_db = [] 
# Function to check if password is secure enough
def check_password_security(password):
    if len(password) < 8:
        print("❌ Password weak: Must be at least 8 characters.")
        return False
    if not re.search(r"\d", password):
        print("❌ Password weak: Must contain at least one number.")
        return False
    if not re.search(r"[A-Za-z]", password):
        print("❌ Password weak: Must contain at least one letter.")
        return False
    
    print("✅ Password is secure.")
    return True

# User registration function
def register_user():
    print("\n--- REGISTER NEW ACCOUNT ---")
    
    # Loop for Username
    while True:
        username = input("Enter a username (or 'exit' to cancel): ")
        if username.lower() == 'exit':
            return

        # Check if user already exists
        username_taken = False
        for user in users_db:
            if user['username'] == username:
                username_taken = True
                break
        
        if username_taken:
             print("❌ Error: Username already taken! Try another one.")
        else:
            break 

    # Loop for Password
    while True:
        password = input("Enter a password (must be 8+ chars, letters & numbers): ")
        if check_password_security(password):
            new_user = {'username': username, 'password': password}
            users_db.append(new_user)
            print(f"✅ Success: User '{username}' registered successfully!")
            break
        else:
            print("⚠️ Password too weak. Please try again.\n")

# Login function to authenticate users
def login_user():
    print("\n--- LOGIN ---")
    while True:
        username = input("Enter username (or 'exit' to return): ")
        if username.lower() == 'exit':
            return

        password = input("Enter password: ")
        
        login_success = False
        for user in users_db:
            if user['username'] == username and user['password'] == password:
                print(f"✅ Welcome back, {username}!")
                login_success = True
                break 
        
        if login_success:
            break 
        else:
            print("❌ Login failed: Invalid username or password. Try again.\n")

# Function to list all registered users
def list_all_data():
    print("\n--- DATABASE CONTENTS ---")
    if not users_db:
        print("Database is empty. Register someone first!")
    else:
        print(f"{'ID':<5} {'Username':<15} {'Password':<20}")
        print("-" * 40)
        for index, user in enumerate(users_db):
            print(f"{index+1:<5} {user['username']:<15} {user['password']:<20}")

# Function to search for a specific user
def select_specific_data():
    print("\n--- SEARCH USER ---")
    target = input("Enter the username you want to find: ")
    
    found = False
    for user in users_db:
        if user['username'] == target:
            print("\n✅ User Found!")
            print(f"Username: {user['username']}")
            print(f"Password: {user['password']}") 
            found = True
            break
    
    if not found:
        print("❌ Error: User not found in database.")

# Main menu loop for user interaction
while True:
    print("\n=== SYSTEM MENU ===")
    print("1. Register ")
    print("2. Login")
    print("3. List All Users ")
    print("4. Search User ")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        register_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
        list_all_data()
    elif choice == '4':
        select_specific_data()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")