import sys
from PIL import Image, ImageOps

def main():
    #test arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_1 = sys.argv[1].lower()
    input_2 = sys.argv[2].lower()

    if input_1[-4:] != input_2[-4:]:
        sys.exit("Invalid Input")
    if not validate_input(input_1) and not validate_input(input_2):
        sys.exit("Invalid Input")

    fit_shirt(sys.argv[1], sys.argv[2])


def validate_input(file):
    if ".jpg" in file or ".png" in file or ".jpeg" in file:
        return True
    else:
        return False


def fit_shirt(image, output):
    shirt = Image.open("shirt.png")
    size = shirt.size
    image = Image.open(image)
    image_fit = ImageOps.fit(image, size)
    image_fit.paste(shirt, shirt)
    image_fit.save(output)


if __name__ == "__main__":
    main()