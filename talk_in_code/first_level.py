def delimiter_cleaner(dirty_text: str):
    if 'parênteses' in dirty_text:
        dirty_text = dirty_text\
            .replace(' abre parênteses ', "(") \
            .replace(' fecha parênteses ', ")")
    if 'chaves' in dirty_text:
        dirty_text = dirty_text \
            .replace(' abre chaves', "{") \
            .replace(' fecha chaves', "}")
    if 'colchetes' in dirty_text:
        dirty_text = dirty_text \
            .replace(' abre colchetes', "{") \
            .replace(' fecha colchetes', "}")
    if 'aspas' in dirty_text:
        dirty_text = dirty_text \
            .replace('aspas', "'")
    cleaned_text = dirty_text
    return cleaned_text
