from turbine import *
from dashboard.dashboard import security_dashboard


# ==========================================
# ADMINISTRATOR MENU
# ==========================================

def admin_menu(username):

    while True:

        print("\n===================================")
        print("   ADMINISTRATOR ACCESS")
        print("===================================")
        print("Welcome:", username)

        print("""
1. View Users
2. View Security Logs
3. Start Wind Turbine
4. Stop Wind Turbine
5. Security Dashboard
6. Turbine Status
7. Exit
""")

        choice = input("Enter Choice: ")

        if choice == "1":

            print("\nUsers:")
            print("----------------")
            print("admin")
            print("operator")
            print("analyst")


        elif choice == "2":

            print("\nSecurity Logs feature")
            
            try:
                with open("logs/security.log", "r") as log:
                    print(log.read())

            except FileNotFoundError:
                print("No logs found.")


        elif choice == "3":

            start_turbine()


        elif choice == "4":

            stop_turbine()


        elif choice == "5":

            security_dashboard()


        elif choice == "6":

            turbine_status()


        elif choice == "7":

            print("\nLogging Out...")
            break


        else:

            print("\nInvalid Choice")



# ==========================================
# OPERATOR MENU
# ==========================================

def operator_menu(username):

    while True:

        print("\n===================================")
        print("   OPERATOR ACCESS")
        print("===================================")
        print("Welcome:", username)


        print("""
1. Start Wind Turbine
2. Stop Wind Turbine
3. View Turbine Status
4. Exit
""")


        choice = input("Enter Choice: ")


        if choice == "1":

            start_turbine()


        elif choice == "2":

            stop_turbine()


        elif choice == "3":

            turbine_status()


        elif choice == "4":

            print("\nLogging Out...")
            break


        else:

            print("\nInvalid Choice")



# ==========================================
# SECURITY ANALYST MENU
# ==========================================

def analyst_menu(username):

    while True:

        print("\n===================================")
        print("   SECURITY ANALYST ACCESS")
        print("===================================")
        print("Welcome:", username)


        print("""
1. View Security Logs
2. View Failed Login Attempts
3. View Security Dashboard
4. Exit
""")


        choice = input("Enter Choice: ")


        if choice == "1":

            try:

                with open("logs/security.log", "r") as log:
                    print(log.read())

            except FileNotFoundError:

                print("No logs found.")



        elif choice == "2":

            try:

                with open("logs/security.log", "r") as log:

                    for line in log:

                        if "FAILED" in line:
                            print(line)


            except FileNotFoundError:

                print("No logs found.")



        elif choice == "3":

            security_dashboard()



        elif choice == "4":

            print("\nLogging Out...")
            break



        else:

            print("\nInvalid Choice")



# ==========================================
# ROLE BASED ACCESS CONTROL
# ==========================================

def access_control(username, role):


    if role == "Administrator":

        admin_menu(username)


    elif role == "Operator":

        operator_menu(username)


    elif role == "Security Analyst":

        analyst_menu(username)


    else:

        print("\nUnauthorized Role")



# ==========================================
# RBAC TEST
# ==========================================

if __name__ == "__main__":


    print("===================================")
    print("      SecureWind RBAC System")
    print("===================================")


    username = input("Enter Username: ")

    role = input(
        "Enter Role (Administrator / Operator / Security Analyst): "
    )


    access_control(username, role)