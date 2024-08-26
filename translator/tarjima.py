from translate import Translator


def en_uz(text):
    translator = Translator(to_lang='uz', from_lang='en')
    data = translator.translate(text)
    return data


def uz_en(text):
    translator = Translator(to_lang='en', from_lang='uz')
    data = translator.translate(text)
    return data


def ru_uz(text):
    translator = Translator(to_lang='uz', from_lang='ru')
    data = translator.translate(text)
    return data


def uz_ru(text):
    translator = Translator(to_lang='ru', from_lang='uz')
    data = translator.translate(text)
    return data


def en_ru(text):
    translator = Translator(to_lang='ru', from_lang='en')
    data = translator.translate(text)
    return data


def ru_en(text):
    translator = Translator(to_lang='en', from_lang='ru')
    data = translator.translate(text)
    return data
