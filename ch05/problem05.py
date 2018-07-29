def main():
    name = str(raw_input("Enter your name : "))

    sum = 0
    for i in name:
        sum = sum + ord(i.lower()) - ord("a") + 1

    print(sum)


main()
