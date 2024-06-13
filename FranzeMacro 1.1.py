import keyboard
import time
import threading
import os

os.system("title FranzeMacro V1.1")
os.system("cls")
os.system("color 0a")
os.system("echo FranzeMacro V1.1 is running, press 'Alt+F7' to force quit` and '`' to pause the macro!")

def press_key():
    while not stop_event.is_set():
        if not pause_event.is_set():
            keyboard.press_and_release('e')
        time.sleep(0.5)

def stop_program(event):
    if event.name == 'f7' and event.event_type == 'down' and keyboard.is_pressed('alt'):
        stop_event.set()

def toggle_pause(event):
    if event.name == '`' and event.event_type == 'down':
        if pause_event.is_set():
            pause_event.clear()
            print("Macro started!")
        else:
            pause_event.set()
            print("Macro is paused!")

stop_event = threading.Event()
pause_event = threading.Event()

# Start the thread that presses 'E' every 0.5 seconds
thread = threading.Thread(target=press_key)
thread.start()

# Add hooks to listen for 'Alt + F7' to stop the program and '`' to toggle pause
keyboard.hook(stop_program)
keyboard.hook(toggle_pause)


# Wait for the stop event
stop_event.wait()

# Clean up
keyboard.unhook_all()
thread.join()
print("Program stopped.")
input("Press Enter to exit...")
os.system("exit")