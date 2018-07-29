def main():
    word = str(raw_input("Enter one word : "))
    key = int(input("Enter the Key number : "))
    encryption = ""
    for i in word:
        encryption = encryption + chr(ord(i) + key)

    print(encryption)

    decryption = ""
    for i in encryption:
        decryption = decryption + chr(ord(i) - key)

    print(decryption)


main()
