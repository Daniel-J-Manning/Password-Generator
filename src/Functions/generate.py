from secrets import choice
from string import (
    ascii_letters,
    digits,
    punctuation
)

CHARS = (ascii_letters + digits + punctuation)

# ======================= Generate Function ======================= #
def generate_pwd(length: int) -> str:
    return ''.join(choice(CHARS) for _ in range(length))
# ======================= Generate Function ======================= #