def delimiter_cleaner(dirty_text: str):
    if 'parênteses' in dirty_text:
        parentheses = dirty_text\
            .find('parênteses')
        for counter in range(0, parentheses):
            if counter % 2 == 0:
                dirty_text = dirty_text\
                    .replace('parêntesis', '(', 1)
            else:
                dirty_text = dirty_text \
                    .replace('parêntesis', ')', 1)
    elif 'chaves' in dirty_text:
        chaves = dirty_text \
            .find('chaves')
        for counter in range(0, chaves):
            if counter % 2 == 0:
                dirty_text = dirty_text \
                    .replace('chaves', '{', 1)
            else:
                dirty_text = dirty_text \
                    .replace('chaves', '}', 1)
    elif 'colchetes' in dirty_text:
        brackets = dirty_text \
            .find('colchetes')
        for counter in range(0, brackets):
            if counter % 2 == 0:
                dirty_text = dirty_text \
                    .replace('colchetes', '[', 1)
            else:
                dirty_text = dirty_text \
                    .replace('colchetes', ']', 1)
    elif 'aspas' in dirty_text:
        dirty_text = dirty_text \
            .replace(' aspas', "'")
    cleaned_text = dirty_text.replace(' ', '')
    return cleaned_text
