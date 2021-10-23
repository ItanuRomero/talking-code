import speech_recognition as sr
import pyttsx3


def clean_code(line_of_code=str):
    return line_of_code \
        .replace(' abre parênteses', "(") \
        .replace('aspas', "'") \
        .replace('fecha parênteses', ")")


def initialize_voice_assistant(voice_enabled):
    if voice_enabled:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 25)
        return engine
    return 'Disabled'


def say(voice_assistant, text):
    print(text)
    if not voice_assistant == 'Disabled':
        voice_assistant.say(text)
        voice_assistant.runAndWait()


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


def start(voice_enabled=True):
    voice_assistant = initialize_voice_assistant(voice_enabled)
    say(voice_assistant, 'Sistema de escrita por voz inicializando...')
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as mic:
            say(voice_assistant, 'Diga algo: ')
            line = listen_and_transfer_to_text(recognizer, mic)
            if 'Fechar sistema' in line:
                say(voice_assistant, 'fechar sistema detectado, finalizando...')
                break
            say(voice_assistant, 'Verifique na tela se a frase está correta.')
            print("Você disse: ", line, "?")
            while True:
                response = listen_and_transfer_to_text(recognizer, mic)
                say(voice_assistant, f'Sua resposta: {response}')
                if 'sim' in response or 'confirmo' in response:
                    line_of_code = clean_code(line)
                    write_on_script_file(line_of_code)
                    say(voice_assistant, 'Linha escrita com sucesso, vamos para outra?')
                    break
                elif 'Fechar sistema' in response:
                    return 'Sistema fechado.'
                elif 'não' in response or 'refazer' in response:
                    break
    return 'Sucesso total!'


if __name__ == '__main__':
    start()
