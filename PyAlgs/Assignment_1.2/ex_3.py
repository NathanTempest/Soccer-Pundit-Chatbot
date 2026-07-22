import sys

def main():
    try:
        hours_input = input("Enter Hours: ")
        hours = float(hours_input)
        rate_input = input("Enter Rate: ")
        rate = float(rate_input)
    except ValueError:
        print("Error, please enter numeric input")
        sys.exit(1)
        
    pay = hours * rate
    print(f"Pay: {pay}")

if __name__ == "__main__":
    main()
