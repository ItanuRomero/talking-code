def delimiter_cleaner(dirty_text: str):
    if 'parênteses' in dirty_text:
        dirty_text = dirty_text\
            .replace(' abre parênteses', "(") \
            .replace(' fecha parênteses', ")")
    elif 'chaves' in dirty_text:
        dirty_text = dirty_text \
            .replace(' abre chaves', "{") \
            .replace(' fecha chaves', "}")
    elif 'colchetes' in dirty_text:
        dirty_text = dirty_text \
            .replace(' abre colchetes', "{") \
            .replace(' fecha colchetes', "}")
    elif 'aspas' in dirty_text:
        dirty_text = dirty_text \
            .replace(' aspas', "'")
    cleaned_text = dirty_text.replace(' ', '')
    return cleaned_text
