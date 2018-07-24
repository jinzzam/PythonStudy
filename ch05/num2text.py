# -*- coding: utf-8 -*-

def main():
    inString = raw_input("Enter unicode-encoded nums : ")
    message = ""
    for numStr in inString.split():
        codeNum = int(numStr)  # 숫자로 된 문자열을 정수형으로 변환
        message = message + chr(codeNum)  # 각 글자를 message 뒤에 연결한다

    print("The decoded message : " + message)


main()
