#Carl Bernardo

def encoder(val):
    # Takes each digit in the val and adds 3 to it
    s = ""
    for i in val:
        if int(i) + 3 > 9:
            s += str((int(i) + 3) % 10)
        else:
            s += str(int(i) + 3)
    return s

if __name__ == "__main__":
    # Create main menu
    currentValue = None
    while True:
        try:
            print("Menu\n"
                  "-------------\n"
                  "1. Encode\n"
                  "2. Decode\n"
                  "3. Quit\n")
            selection = int(input("Please enter an option: "))
            match selection:
                case 1:
                    currentValue = encoder(input("Please enter your password to encode: "))
                    print("Your password has been encoded and stored!")
                case 2:
                    print("Section 2")
                case 3:
                    exit()
                case _:
                    print("Error. Please make valid selection")
        except ValueError as error:
            print(f"ERROR: {error}")
        print()