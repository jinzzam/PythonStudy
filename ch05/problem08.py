def main():
    key = int(input("Enter the key : "))
    plain = raw_input("Enter the phrase : ")

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"

    cipher = ""
    for letter in plain:
        pos = chars.find(letter)
        newpos = (pos + key) % len(chars)
        cipher = cipher + chars[newpos]

    print(cipher)


main()
