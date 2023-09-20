# Characters functions
def a_convert(word: str, index: int) -> str:
    """
    а
    :param word:
    :param index:
    :return:
    """

    if not index == 0:
        if word[index - 1] == 'а':
            return ''

    text = word[index:]

    is_ai = 'й' == text[1] if len(text) > 1 else False
    if is_ai:
        return 'æː'

    is_aa = 'а' == text[1] if len(text) > 1 else False

    # Check if the substring contains 'и', 'ь', or 'ий'
    is_i = 'и' == text[2] if len(text) > 2 else False
    is_soft = 'ь' == text[2] if len(text) > 2 else False

    if is_i or is_soft:
        if is_aa:
            return 'æː'
        else:
            return 'æ'

    if is_aa:
        return 'aː'

    # If none of the substrings are found, return the original substring
    return word[index]


def w_convert(word: str, index: int) -> str:
    """
     В
    :param word:
    :param index:
    :return:
    """

    if len(word) > index + 1:
        next_char = word[index + 1]

        if next_char == 'т' or next_char == 'ц' or next_char == 'ч':
            return 'ɸ'

    return 'w'


def k_convert(word: str, index: int) -> str:
    """
     Г
    :param word:
    :param index:
    :return:
    """

    return 'k'
