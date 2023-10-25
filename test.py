

from decode import *
def Encoder(password):
    string= ''
    list = []
    for i in str(Password):
        list.append(str(i))

    for digit in list:
        if digit == '9':
            string += '2'
        if digit == '8':
            string += '1'
        if digit == '7':
            string += '0'
        else:
            string += str(int(digit)+3)
    return string


while True:

    print('''Menu
-------------
1. Encode
2. Decode
3. Quit
Please enter an option:''')
    Choice = input()
    if Choice == '1':
        Password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
        print(str(Password))
    if Choice == '2':
        encoded = Encoder(Password)
        print("Encoded password is", encoded + ", and the original password is", (decode(encoded)))
    if Choice == '3':
        break
