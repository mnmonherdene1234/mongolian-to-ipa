from mongolian_to_ipa.char_convertor import a_convert, w_convert
from mongolian_to_ipa.mongolia_ipa_dictionary import mongolian_to_ipa


def mongolian_convert_to_ipa(word):
    word.lower()

    ipa_transcription = ''

    for i in range(len(word)):
        c = word[i]

        try:
            add_char = None

            if c == 'а':
                add_char = a_convert(word, i)

            if c == 'в':
                add_char = w_convert(word, i)

            if add_char is not None:
                ipa_transcription += add_char
            else:
                ipa_transcription += mongolian_to_ipa[c]
        except KeyError:
            print(f"Character '{c}' not found.")
            ipa_transcription += c

    return ipa_transcription

