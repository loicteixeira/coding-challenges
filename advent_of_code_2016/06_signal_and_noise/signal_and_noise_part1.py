from collections import Counter
import os


def find_message(repetition_code):
    characters = []

    # Transpose lines to columns
    columns = zip(*repetition_code.splitlines())

    # Find most common character for each column
    for column in columns:
        counter = Counter(column)
        most_common_character = counter.most_common(1)[0][0]
        characters.append(most_common_character)

    message = ''.join(characters)

    return message

if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'input.txt')
    with open(file_path, 'r') as f:
        data = f.read()

    message = find_message(data)
    print('The error-corrected message is `{}`'.format(message))
