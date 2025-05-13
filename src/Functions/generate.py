import cython as C
from secrets import choice
from string import (
    ascii_letters,
    digits,
    punctuation
)

CHARS: C.char[100] = (ascii_letters + digits + punctuation)

# ======================= Generate Function ======================= #
def generate_pwd(length: C.int) -> C.char[100]:
    return ''.join(choice(CHARS) for _ in range(length))
# ======================= Generate Function ======================= #