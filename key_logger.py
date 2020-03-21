from pynput import keyboard
import logging
import time
import pickle

global key_value_list
global key_value_list_press
key_value_list = list()
key_value_list_press = list()


def on_press(key_data):
    ts = time.time()
    try:
        key_value = str(key_data.char)
        key_type = "char"
    except AttributeError:
        key_value = str(key_data)
        key_type = "else"
    finally:
        print(key_value)
        key_value_list.append((key_value, ts))
        key_value_list_press.append((key_value, key_type, ts))



def on_release(key_data):
    ts = time.time()
    key_value_raw = str(key_data) 
    if key_value_raw.startswith("'") and key_value_raw.endswith("'"):
        key_value = key_value_raw.strip("'") + '_'
    else: 
        key_value = key_value_raw + '_'

    key_value_list.append((key_value, ts))

    if key_data == keyboard.Key.esc:
        return False


def get_text_from_data(keylog_list):
    eng_article = ""
    for one_key in keylog_list:

        if one_key[1] == 'char':
            eng_article += one_key[0]
        elif one_key[1] == 'else':
            if one_key[0] == 'Key.space':
                eng_article += " "
            elif one_key[0] == 'Key.enter':
                eng_article += "\n"
            elif one_key[0] == 'Key.backspace':
                eng_article = eng_article[:-1]

    return eng2kor.engTypeToKor(eng_article)


if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press,
                           on_release=on_release) as listener:
        listener.join()

    get_text_from_data(key_value_list_press)