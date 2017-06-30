import re
from emo import emo_unicode

'''emo library to detect emoji and emoticons.

    >>> import emo
    >>> text = "I love python 👨 :-)"
    >>> emoji(text)
    >>> [{'value': '👨', 'str_span': [10, 10]}]
    >>> emoticons(text)
    >>> [{'value': ':-)', 'str_span': [12, 15]}]
'''

__all__ = ['emoji','emoticons']

def emoji(string):
    '''emo.emoji is use to detect emoji from text

        >>> text = "I love python 👨 :-)"
        >>> emoji(text)
        >>> [{'value': '👨', 'str_span': [10, 10]}]
    '''
    __entities = []
    pro_string = str(string)
    for pos,ej in enumerate(pro_string):
        if ej in emo_unicode.UNICODE_EMO:
            __entities.append({
                "value": ej,
                "str_span": [pos,pos]
                })
    return __entities

def emoticons(string):
    '''
    '''
    __entities = []
    pattern = u'(' + u'|'.join(k for k in emo_unicode.EMOTICONS) + u')'
    __entities = []
    matches = re.finditer(r"%s"%pattern,str(string),re.IGNORECASE)
    for et in matches:
        __entities.append({'value': et.group().strip(),
        'str_span': [et.start(),et.end()]
        })
    return __entities

def test_emo():
    test = "I love it 👨 :-)"
    print(emoji(test))
    print(emoticons(test))
    return None
