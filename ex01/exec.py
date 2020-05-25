import sys

# argv give the list of command line arguments
words_list = sys.argv[1:]
# join make a string with a list. Each element will be separeted with ' '
result = ' '.join(words_list)
# reverse order of the string
result = result[::-1]
# reverse case for each character of the string
result = result.swapcase()
print(result)
