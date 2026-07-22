def main():
    correct_password = "python123"
    while True:
        password = input("Enter password: ")
        if password == correct_password:
            print("Access granted!")
            break
        else:
            print("Incorrect password. Try again.")

if __name__ == "__main__":
    main()
