"""
Python Source code to generate a secure random password using the CLI
Example: python3 main.py --length 16
"""

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
def generate_pwd(length: int) -> str:
    return ''.join(choice(CHARS) for _ in range(length))
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


# =========================  Main Function  ======================= #
if __name__ == "__main__":
    args = parse()
    password = generate_pwd(args.length)
    print("Generated Password:", password)