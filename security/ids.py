# ==========================================
# SecureWind Intrusion Detection System (IDS)
# ==========================================

def detect_attack(username, password):

    attack_patterns = [

        "'",

        "--",

        ";",

        "<script>",

        "</script>",

        "../",

        "&&",

        "|",

        " OR ",

        "SELECT",

        "DROP",

        "DELETE",

        "INSERT",

        "UPDATE"

    ]

    username_upper = username.upper()
    password_upper = password.upper()

    for attack in attack_patterns:

        if attack.upper() in username_upper or attack.upper() in password_upper:

            print("\n===================================")
            print("      SECURITY ALERT")
            print("===================================")
            print("Possible Cyber Attack Detected!")
            print("Blocked Pattern:", attack)
            print("Access Denied")
            print("===================================")

            return True

    return False


# Test IDS

if __name__ == "__main__":

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if not detect_attack(username, password):
        print("\nNo attack detected.")