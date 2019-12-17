import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()  # remove '\n' which is at the end of the line
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)  # next_lang == cooked_string

    print(raw_bytes, "<===>", cooked_string)


languages = open("ex23_languages.txt", encoding = 'utf-8')  # ex23_languages.txt is encoded by utf-8

main(languages, encoding, error)