from django import template


register = template.Library()


SYMBOLS = (',', '.', '!', ':', '"', '(', ')', '@', '?', '-', '_', '=', '/', '+')

CENSOR_WORD = [
    'сука', 'дурак', 'дебил', 'идиот', 'fuck', 'shit', 'bitch'
]


@register.filter()
def censor(text):
    if not isinstance(text, str):
        raise TypeError('Фильтр censor можно применять только к строковым типам данных!')

    text = text.split()
    result = []
    for word in text:
        if word.strip(''.join(SYMBOLS)).lower() in CENSOR_WORD:
            if word.startswith(SYMBOLS) and word.endswith(SYMBOLS):
                first_sym, last_sym = word[0], word[-1]
                length_censor = len(word[1:-1]) - 1
                word = f'{first_sym}{word[1]}{length_censor * "*"}{last_sym}'
            elif word.endswith(SYMBOLS):
                symbol = word[-1]
                length_censor = len(word[:-1]) - 1
                word = f'{word[0]}{length_censor * "*"}{symbol}'
            else:
                length_censor = len(word) - 1
                word = f'{word[0]}{length_censor * "*"}'
        result.append(word)
    return ' '.join(result)
