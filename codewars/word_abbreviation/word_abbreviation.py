import re

PATTERN = re.compile(r'(\w)(\w{2,})(\w)')
REPLACE_FUNC = lambda match: match.group(1) + str(len(match.group(2))) + match.group(3)


def abbreviate(word):
    return PATTERN.sub(REPLACE_FUNC, word)
