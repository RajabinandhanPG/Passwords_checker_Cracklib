# Password Strength Checker

This Python script provides a simple yet effective way to evaluate the strength of a password. It checks for a mix of uppercase and lowercase letters, numbers, symbols, and overall length to ensure the password meets basic strength criteria. Then the password is ran aganist cracklib library which contrains commonly used passwords to further amplify the integrity of the password.

## Features

- **Length Check:** Ensures the password is at least 8 characters long.
- **Character Diversity:** Checks for the inclusion of uppercase letters, lowercase letters, numbers, and symbols.
- **Error Handling:** Provides user-friendly error messages for common password weaknesses.

## Dependencies

- `cracklib`: Used for additional password strength checking.
- `colorama`: Provides colored terminal output for better readability.

## Installation

To run this script, you'll need Python installed on your system along with the `cracklib` and `colorama` packages. Install them using pip:

```bash
pip install cracklib
pip install colorama
```

## Usage
Run the script in your terminal. When prompted, enter the password you want to check:
```py
python password_strength_checker.py
```




