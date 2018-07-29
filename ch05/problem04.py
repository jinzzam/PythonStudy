def main():
    word = str(raw_input("Enter word : "))

    acronym = ""
    for Word in word.split():
        acronym = acronym + Word[0]
    acronym = acronym.upper()

    print(acronym)


main()
