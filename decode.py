def decode(password):
    decoded_password = ''
    for character in password:
        if (int(character) - 3) < 0:
            decoded_password += str(10 + (int(character) - 3))
        else:
            decoded_password += str(int(character) - 3)
    return int(decoded_password)


def main():
    pass


if __name__ == "__main__":
    main()
