__version__ = '0.1.0'

from keysymdef import keysymdef
from pynput.keyboard import Controller, Listener
keyboard = Controller()
last_pressed_key = None


def main():
    with Listener(
            on_press=on_press, 
            on_release=on_release, 
            suppress=True
    ) as listener:
        listener.join()


def on_press(key):
    global last_pressed_key
    last_pressed_key = key


def on_release(key):
    if key != last_pressed_key:
        return False

    virtual_key = get_virtual_key(key)
    key_name = get_x11_key_name(virtual_key)
    print(key_name)

    # disable listener
    return False


def get_virtual_key(key):
    virtual_key = getattr(key, "vk", None)
    if not virtual_key:
        virtual_key = key.value.vk
    return virtual_key


def get_x11_key_name(virtual_key):
    for key_name, key_sym, _ in keysymdef:
        if virtual_key == key_sym:
            return key_name
    return None

if __name__ == "__main__":
    main()
