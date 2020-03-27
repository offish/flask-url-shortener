from lib.config import random_len
import random
import string


def generate(url: str, characters: int = random_len) -> str:
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(characters))
