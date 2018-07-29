def main():
    day = int(input("Enter day : "))
    month = int(input("Enter month : "))
    year = int(input("Enter year : "))

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    date = "{0} {1} {2}".format(months[month - 1], day, year)

    print(date)


main()
