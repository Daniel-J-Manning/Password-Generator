import argparse

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