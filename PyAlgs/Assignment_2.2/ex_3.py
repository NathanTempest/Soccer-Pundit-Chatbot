def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # a. The first half of the string using starting and ending indices.
    slice_a = alphabet[0:13]
    # b. The first half of the string using only the ending index.
    slice_b = alphabet[:13]
    # c. The second half of the string using starting and ending indices.
    slice_c = alphabet[13:26]
    # d. The second half of the string using only the starting index.
    slice_d = alphabet[13:]
    # e. Every second letter in the string starting with ‘a’.
    slice_e = alphabet[::2]
    # f. The entire string in reverse.
    slice_f = alphabet[::-1]
    # g. Every third letter of the string in reverse starting with ‘z’.
    slice_g = alphabet[::-3]
    
    # Print outputs
    print(f"a. {slice_a}")
    print(f"b. {slice_b}")
    print(f"c. {slice_c}")
    print(f"d. {slice_d}")
    print(f"e. {slice_e}")
    print(f"f. {slice_f}")
    print(f"g. {slice_g}")

if __name__ == '__main__':
    main()
