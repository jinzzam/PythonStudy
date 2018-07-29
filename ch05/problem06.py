def main():
    fullName = str(raw_input("Enter your name : "))

    name = "".join(fullName.split(" "))
    print(name)
    sum = 0

    for i in name:
        sum = sum + ord(i.lower()) - ord("a") + 1
        print(sum)

    print(sum)


main()
