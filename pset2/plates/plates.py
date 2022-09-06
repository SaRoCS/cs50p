def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #first 2 letters
    if not s[0:2].isalpha():
        return False
    #length btwn 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False
    #no punctuation
    if not s.isalnum():
        return False
    #numbers must be at the end
    if numbers_not_end(s):
        return False
    #zero cannot be first number
    if zero_first(s):
        return False
    return True


def numbers_not_end(text):
    for i in range(len(text) - 1):
        if text[i].isnumeric() and text[i + 1].isalpha():
            return True
    return False


def zero_first(text):
    #get first number
    first = None

    for letter in text:
        if letter.isnumeric():
            first = letter
            break
    #check number
    if first == "0":
        return True
    else:
        return False

main()