def main():
    score = int(input("Enter score : "))

    if score == 5:
        print("A")
    elif score == 4:
        print("B")
    elif score == 3:
        print("C")
    elif score == 2:
        print("D")
    elif score == 1 or score == 0:
        print("F")
    else:
        print("score error")


main()
