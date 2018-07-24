def main():
    print("This program generates computer usernames.\n")

    first = raw_input("first : ")
    last = raw_input("last : ")

    uname = str(first[0] + last[:7])
   
    print("your username is : ", uname)

main()