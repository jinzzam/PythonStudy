def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(raw_input("Enter a month num : "))

    pos = (n - 1) * 3
    monthAbbrev = str(months[pos:pos + 3])

    print("The month is " + monthAbbrev + ".")


main()
