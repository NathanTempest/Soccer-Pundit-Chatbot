def fahrenheit(celsius):
    """Returns the Fahrenheit equivalent of a Celsius temperature."""
    return (9 / 5) * celsius + 32

def main():
    # Print header
    print(f"{'Celsius':>7}  {'Fahrenheit':>11}")
    print("-" * 20)
    
    # Print table values
    for c in range(101):
        f = fahrenheit(c)
        print(f"{c:>7}  {f:>11.1f}")

if __name__ == '__main__':
    main()
