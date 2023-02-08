# Strings, Bytes, Character Encodings

import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        # return statement calling the same function is where the looping comes from
        return main(language_file, encoding, errors)
    else:
        print("Done")


def print_line(line, encoding, errors):
    next_lang = line.strip()  # .strip() strips the '\n' on the line sting
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, encoding, error)

# if you have raw bytes that you must use .decode() function to get the string
# sometimes you must .encode() to get bytes from a string
# DBES, which stands for Decode Bytes, Encode Strings
