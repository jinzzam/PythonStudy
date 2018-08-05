def main():
    phrase = str(raw_input("Enter the phrase : "))

    word_count = phrase.count(" ") + 1

    sum = 0
    for i in phrase.split():
        sum += len(i) - 1

    print(sum / word_count)


main()
