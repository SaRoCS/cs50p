from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    font = random.choice(fonts)
    figlet.setFont(font=font)
elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("invalid args")
else:
    sys.exit("incorrect usage")

print(figlet.renderText(text))

