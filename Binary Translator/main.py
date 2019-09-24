def translator():
    sequence = input("Please entire your word/sentence below: \n")
    newSequence = ""
    for i in sequence:
        if i == ' ':
            newSequence += ' '
        elif i == 'a':
            newSequence += '01100001'
        elif i == 'b':
            newSequence += '01100010'
        elif i == 'c':
            newSequence += '01100011'
        elif i == 'd':
            newSequence += '01100100'
        elif i == 'e':
            newSequence += '01100101'
        elif i == 'f':
            newSequence += '01100110'
        elif i == 'g':
            newSequence += '01100111'
        elif i == 'h':
            newSequence += '01101000'
        elif i == 'i':
            newSequence += '01101001'
        elif i == 'j':
            newSequence += '01101010'
        elif i == 'k':
            newSequence += '01101011'
        elif i == 'l':
            newSequence += '01101100'
        elif i == 'm':
            newSequence += '01101101'
        elif i == 'n':
            newSequence += '01101110'
        elif i == 'o':
            newSequence += '01101111'
        elif i == 'p':
            newSequence += '01110000'
        elif i == 'q':
            newSequence += '01110001'
        elif i == 'r':
            newSequence += '01110010'
        elif i == 's':
            newSequence += '01110011'
        elif i == 't':
            newSequence += '01110100'
        elif i == 'u':
            newSequence += '01110101'
        elif i == 'v':
            newSequence += '01110110'
        elif i == 'w':
            newSequence += '01110111'
        elif i == 'x':
            newSequence += '01111000'
        elif i == 'y':
            newSequence += '01111001'
        elif i == 'z':
            newSequence += '01111010'

        elif i == 'A':
            newSequence += '01000001'
        elif i == 'B':
            newSequence += '01000010'
        elif i == 'C':
            newSequence += '01000011'
        elif i == 'D':
            newSequence += '01000100'
        elif i == 'E':
            newSequence += '01000101'
        elif i == 'F':
            newSequence += '01000110'
        elif i == 'G':
            newSequence += '01000111'
        elif i == 'H':
            newSequence += '01001000'
        elif i == 'I':
            newSequence += '01001001'
        elif i == 'J':
            newSequence += '01001010'
        elif i == 'K':
            newSequence += '01001011'
        elif i == 'L':
            newSequence += '01001100'
        elif i == 'M':
            newSequence += '01001101'
        elif i == 'N':
            newSequence += '01001110'
        elif i == 'O':
            newSequence += '01001111'
        elif i == 'P':
            newSequence += '01010000'
        elif i == 'Q':
            newSequence += '01010001'
        elif i == 'R':
            newSequence += '01010010'
        elif i == 'S':
            newSequence += '01010011'
        elif i == 'T':
            newSequence += '01010100'
        elif i == 'U':
            newSequence += '01010101'
        elif i == 'V':
            newSequence += '01010110'
        elif i == 'W':
            newSequence += '01010111'
        elif i == 'X':
            newSequence += '01011000'
        elif i == 'Y':
            newSequence += '01011001'
        elif i == 'Z':
            newSequence += '01011010'

        elif i == '0':
            newSequence += '00110000'
        elif i == '1':
            newSequence += '00110001'
        elif i == '2':
            newSequence += '00110010'
        elif i == '3':
            newSequence += '00110011'
        elif i == '4':
            newSequence += '00110100'
        elif i == '5':
            newSequence += '00110101'
        elif i == '6':
            newSequence += '00110110'
        elif i == '7':
            newSequence += '00110111'
        elif i == '8':
            newSequence += '00111000'
        elif i == '9':
            newSequence += '00111001'

        elif i == '!':
            newSequence += '00100001'
        elif i == '\"':
            newSequence += '00100010'
        elif i == '#':
            newSequence += '00100011'
        elif i == '$':
            newSequence += '00100100'
        elif i == '%':
            newSequence += '00100101'
        elif i == '&':
            newSequence += '00100110'
        elif i == '\'':
            newSequence += '00100111'
        elif i == '(':
            newSequence += '00101000'
        elif i == ')':
            newSequence += '00101001'
        elif i == '*':
            newSequence += '00101010'
        elif i == '+':
            newSequence += '00101011'
        elif i == ',':
            newSequence += '00101100'
        elif i == '-':
            newSequence += '00101101'
        elif i == '.':
            newSequence += '00101110'
        elif i == '/':
            newSequence += '00101111'
        elif i == '?':
            newSequence += '00111111'
        elif i == '@':
            newSequence += '01000000'
        elif i == '_':
            newSequence += '01011111'

    return newSequence


print(translator())
