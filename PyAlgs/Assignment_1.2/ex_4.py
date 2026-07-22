def main():
    score_input = input("Enter score: ")
    try:
        score = float(score_input)
        if score < 0.0 or score > 1.0:
            print("Bad score")
        else:
            if score >= 0.9:
                print("A")
            elif score >= 0.8:
                print("B")
            elif score >= 0.7:
                print("C")
            elif score >= 0.6:
                print("D")
            else:
                print("F")
    except ValueError:
        print("Bad score")

if __name__ == "__main__":
    main()
