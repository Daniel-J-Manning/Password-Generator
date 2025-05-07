# ============================ IMPORTS ============================ #
from string import (
    ascii_lowercase,                # A-Z
    ascii_uppercase,                # a-z
    digits,                         # 0-9
    punctuation)
from secrets import choice          # Import module to select random choice
import argparse                     # Import to allow working with a CLI
# ============================ IMPORTS ============================ #


# =========================== CONSTANTS =========================== #
CHARS = (ascii_lowercase + ascii_uppercase + digits + punctuation)
# =========================== CONSTANTS =========================== #


# ======================= Generate Function ======================= #
def generate_pwd() -> str:
    """
    Prompts the user for password length and returns a generated password string.
    """
    try:

        length = int(input("How long would you like your password to be (Minimum 8): "))

        if length < 8:
            raise ValueError("Password length must be at least 8 characters.")
        
        password = ''.join(choice(CHARS) for _ in range(length))
        return password
    
    except ValueError as e:
        print("Error:", e)
        return ""
# ======================= Generate Function ======================= #


# ========================  Parse Function  ======================= #
def parse():
    parser = argparse.ArgumentParser(
        prog="Password Generator",
        description="Generates a secure random password"
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=12,
        help="Length of the password (minimum 8)"
    )
    args = parser.parse_args()
    
    if args.length < 8:
        parser.error("Password length must be at least 8 characters.")
    
    return args
# ========================  Parse Function  ======================= #

