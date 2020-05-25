from string import punctuation
from sys import argv


def words_filter() -> list:
    if len(argv) != 3:
        return "ERROR"
    string = argv[1]
    if string.isdigit():
        return "ERROR"
    if not argv[2].isdigit():
        return "ERROR"
    n = int(argv[2])

    words_list = string.split(' ')
    # First remove ponctuation
    words_list = [word.strip(punctuation) for word in words_list]
    # Then keep only element longer than n
    words_list = [word for word in words_list if len(word) > n]
    return words_list


if __name__ == "__main__":
    print(words_filter())
