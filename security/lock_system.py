attempts = {}
MAX_ATTEMPTS = 3
while True:
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username not in attempts:
        attempts[username] = 0

    if attempts[username] >= MAX_ATTEMPTS:
        print("\n===================================")
        print(" ACCOUNT LOCKED")
        print("Too many failed login attempts.")
        print("Please contact the administrator.")
        print("===================================")
        break

    if username == "admin" and password == "SecureWind123":
        print("\n===================================")
        print(" Login Successful")
        print("Welcome Administrator!")
        print("===================================")
        attempts[username] = 0
        break

    else:
        attempts[username] += 1
        remaining = MAX_ATTEMPTS - attempts[username]
        print("\n Invalid Username or Password")
        if remaining > 0:
            print(f"Attempts Left: {remaining}")
        else:
            print("\n===================================")
            print(" ACCOUNT LOCKED")
            print("You have exceeded the maximum login attempts.")
            print("===================================")
            break
