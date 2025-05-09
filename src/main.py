"""
Python Source code to generate a secure random password using the CLI
Example: python3 main.py --length 16
"""

from Functions.generate import generate_pwd
from Functions.parser import parse

# =========================  Main Function  ======================= #
if __name__ == "__main__":
    args = parse()
    password = generate_pwd(args.length)
    print("Generated Password:", password)