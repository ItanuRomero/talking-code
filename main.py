import speech_recognition as sr


def clean_code(line_of_code=str):
    return line_of_code\
        .replace(' abre parênteses', "(")\
        .replace('aspas', "'")\
        .replace('fecha parênteses', ")")


def start():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
        print('Diga algo: ')
        audio = recognizer.listen(mic)

        try:
            line = recognizer.recognize_google(audio, language='pt-BR')
            print("Você disse: ", line, "?")
            print('Confirme: ')
            response = recognizer.listen(mic)
            response = recognizer.recognize_google(response, language='pt-BR')
            print(response)
            if 'sim' in response:
                line = clean_code(line)
                with open('talked-code.py', 'a') as script_file:
                    script_file.write(line)
        except Exception as err:
            print("Não entendi. ", err)
    return 'Sucesso total!'


if __name__ == '__main__':
     start()
