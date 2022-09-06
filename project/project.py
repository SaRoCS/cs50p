"""Creates a tkinter GUI that tests the security of a password"""

from math import log2
import re
import tkinter as tk
from tkinter import END, ttk
from tkinter.messagebox import showerror, showinfo
# from ctypes import windll
from humanize import intword


class App(tk.Tk):
    """Creates a tkinter GUI"""

    def __init__(self):
        super().__init__()

        # set title and icon
        self.title("PyPass")
        icon = tk.PhotoImage(file='lock.png')
        self.tk.call('wm', 'iconphoto', self._w, icon)
        # self.iconbitmap("lock.ico")

        # center the GUI on the screen
        width = 500
        height = 150

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int((screen_width / 2) - (width / 2))
        center_y = int((screen_height / 2) - (width / 2))

        self.geometry(f"{width}x{height}+{center_x}+{center_y}")

        # call to create GUI widgets
        self.create_widgets()

    def create_widgets(self):
        """Create and pack tkinter widgets in the GUI"""

        # create title label
        label = ttk.Label(self, text="Password", font=(48))
        label.pack(pady=10)

        # create entry box
        password = tk.StringVar()
        password_box = ttk.Entry(self, textvariable=password, show="*")

        # bind return event to submit
        password_box.bind("<Return>", lambda x: handle(password.get(), password_box))

        password_box.pack(fill="x", pady=10, padx=100)
        password_box.focus()

        # create a submit button
        button = ttk.Button(
            self, text="Test", command=lambda: handle(password.get(), password_box)
        )
        button.pack(pady=10)


def main():
    """Starts the GUI"""

    # fix resolution for tk interfaces
    # windll.shcore.SetProcessDpiAwareness(1)

    # run tkinter app
    app = App()
    app.mainloop()


# function to go between the GUI and the check functions
def handle(password, password_box):
    """Takes in GUI widgets and input, runs checks, then returns output to GUI"""

    # validate for only ASCII printable characters not including space
    if (
        password
        and password.isascii()
        and password.isprintable()
        and " " not in password
    ):
        # run checks
        entropy_check = entropy(password)
        patterns_check = patterns(password)

        # display results
        showinfo(
            "Test Results",
            (
                f"Bits of entropy: {entropy_check['bits']}    (60-80 recommended)\n"
                f"Average number of random guesses required: {entropy_check['guesses']}"
                f"\n Patterns: {patterns_check}"
            ),
        )
    else:
        # error
        showerror(
            "Error",
            (
                "Invalid Password. Passwords may not contain "
                "spaces or non-standard symbols "
                "and must contain at least one character."
            ),
        )

    # clear entry
    password_box.delete(0, END)


def entropy(password):
    """Calculate the strings entropy"""

    length = len(password)
    pool = pool_size(password)

    entropy_bits = log2(pool**length)
    guesses_avg = 2 ** (entropy_bits - 1)

    return {"bits": round(entropy_bits, 2), "guesses": intword(guesses_avg)}


def pool_size(password):
    """Calculate size of charachter pool"""

    lower = False
    upper = False
    number = False
    symbol = False

    # test which sets of characters are used
    for char in password:
        if char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char.isdecimal():
            number = True
        else:
            symbol = True

    # add the possible characters in each used set
    pool = 0
    if lower:
        pool += 26
    if upper:
        pool += 26
    if number:
        pool += 10
    if symbol:
        pool += 32

    return pool


def patterns(password):
    """Tests for repeated patterns"""

    if matches := re.search(r"((.+?)\2+)", password, re.IGNORECASE):
        print(matches)
        return f'Repeated patterns found: "{matches.group(2)}"'
    if matches := re.search(r"(..*)(.*?)\1", password, re.IGNORECASE):
        return f'Repeated patterns found: "{matches.group(1)}"'
    return "No repeated patterns found"


if __name__ == "__main__":
    main()
