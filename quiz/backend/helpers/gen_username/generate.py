import os
import random

from typing import List

dir_path = os.path.dirname(__file__)

with open(os.path.join(dir_path, "data", "useradj.txt"), "r") as file_useradj:
    adjectives = [line.strip() for line in file_useradj]
with open(os.path.join(dir_path, "data", "usernoun.txt"), "r") as file_usernoun:
    nouns = [line.strip() for line in file_usernoun]


def generate_username(num_results: int = 5) -> List[str]:
    """Generates random usernames consisting of adjective, noun and two-digit number.

    :param num_results: number of usernames to generate
    :type num_results: int
    :returns: list of usernames
    :rtype: list
    """

    usernames = []
    for _ in range(num_results):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        num = str(random.randrange(100))
        usernames.append(adjective + noun + num)

    return usernames
