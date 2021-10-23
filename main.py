import speech_recognition as sr


def clean_code(line_of_code=str):
    return line_of_code \
        .replace(' abre parênteses', "(") \
        .replace('aspas', "'") \
        .replace('fecha parênteses', ")")


def listen_and_transfer_to_text(recognizer, microphone):
    recognizer.adjust_for_ambient_noise(microphone)
    audio = recognizer.listen(microphone)
    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
    except Exception as err:
        print("Não entendi. ", err)
        return 'Error'
    return text


def write_on_script_file(line, filename='talked-code.py'):
    with open(filename, 'a') as script_file:
        script_file.write(line + '\n')


def start():
    print('Sistema de escrita por voz iniciado!')
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as mic:
            print('Diga algo: ')
            line = listen_and_transfer_to_text(recognizer, mic)
            if 'Fechar sistema' in line:
                print('fechar sistema detectado, finalizando...')
                break
            while True:
                print("Você disse: ", line, "?")
                response = listen_and_transfer_to_text(recognizer, mic)
                print('Sua resposta: ', response)
                if 'sim' in response or 'confirmo' in response:
                    line_of_code = clean_code(line)
                    write_on_script_file(line_of_code)
                    break
                elif 'Fechar sistema' in response:
                    return 'Sistema fechado.'
    return 'Sucesso total!'


if __name__ == '__main__':
    start()
