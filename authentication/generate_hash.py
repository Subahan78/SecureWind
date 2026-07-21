import bcrypt

password = input("Enter Password: ")

hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

print("\nHashed Password:")
print(hashed.decode())