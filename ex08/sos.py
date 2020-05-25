from sys import argv

# https://morsecode.world/international/morse2.html
morse_encoder = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


def morse_encode(a_list):
    if len(a_list) > 1:
        str = ' '.join(a_list[1:])
    else:
        return ""

    a_list = str.split()
    for char in a_list:
        if not char.isalnum():
            return "ERROR"
    str = ' '.join(a_list).lower()

    result = ""
    for i in range(len(str)):
        if i != 0:
            result = result + " "
        if str[i] == " ":
            result = result + "/"
            continue
        result = result + morse_encoder[str[i]]
    return result


if __name__ == "__main__":
    print(morse_encode(argv))
