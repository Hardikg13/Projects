def main():
    print("Welcome to Email Slicer")
    print(" ")

    email_input = input("Enter your email address:")

    (username,domain) = email_input.split("@")
    (domain,extension) = domain.split(".")

    print("username =",username)
    print("domain =",domain)
    print("extension =",extension)

while True:
    main()



