def main():
    text = input("Input: ")
    print("Output: " + shorten(text))


def shorten(word):
    txt = ""

    for letter in word:
        if letter.lower() not in "aeiou":
            txt += letter
    return txt


if __name__ == "__main__":
    main()