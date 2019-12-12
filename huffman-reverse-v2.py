def decode(dictionary, encoded_string):
    sequence = ''
    decoded_string = ''
    for symbol in encoded_string:
        sequence += symbol
        if sequence in dictionary:
            decoded_string += dictionary[sequence]
            sequence = ''
    return decoded_string


def main():
    k, l = map(int, input().split())
    dictionary = {}
    for i in range(k):
        data = input().split(': ')
        dictionary[data[1]] = data[0]
    encoded_string = input()
    print(decode(dictionary, encoded_string))


if __name__ == "__main__":
    main()