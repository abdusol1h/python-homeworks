password = input("Create a password: ")
list = list(password)
capsPresent = False

for char in list:
    if 'A' <= char <= 'Z':
        capsPresent = True

if len(list) < 8:
    print("Password too short")
else:
    if not capsPresent:
        print("Password must contain at least one uppercase letter.")
    else:
        print("Password is strong.")