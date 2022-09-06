# PyPass
#### Video Demo:  <https://youtu.be/pi5sBnx8-h4>
#### Description:
PyPass is a password strength tester using a tkinter GUI.
The password is tested for bits of entropy, the average number of random guesses required to guess the password,
and any repeated patterns.  PyPass only measures the strength of a password against brute force attacks not dictionary attacks.

#### `project.py`
This file contains all of the code for PyPass.  The `App` class creates a tkinter GUI with a title and icon, centers the window
on the screen and creates the tkinter widgets.  The `label` widget is the title, the `password_box` widget provide a space to enter
passwords, and the `button` widget submits the entered password.  The `handle` function validates the password, calls the check functions,
and displays a dialogue box.  `entropy` uses the formula log2(P^L) where P is the pool of characters and L is the password's length to
calculate entropy and the formula 2^(n-1) where n is bits of entropy to calculate the average number of guesses.  I debated creating my own
formula that took repeated characters and the amount of characters used out of the pool into account, but I chose not to due to the complexity
and the fact that it began to move the score away from purely brute force attacks to a spot somewhere in between, that did not really represent
either type of strength.  `pool_size` determines what character pools were used and totals their size.  Finally, `patterns` uses regular expressions to first find repeated patterns in a row and then repeated patterns throughout the string.  I included `patterns` when I
decided to use the standard formula for entropy to at least alert the user of repetitions.

#### `test_project.py`
This file contains all the tests to be run with `pytest`.  The GUI's creation, character pool size calculation, bits of entropy
calculation, and pattern recognition are tested.

#### `requirements.txt`
This file contains all required packages to run PyPass.

#### Instructions:
Install requirements and run the project.py file.  Enter a password and click the test button or press Enter.