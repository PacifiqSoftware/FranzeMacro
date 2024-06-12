import keyboard
import time
import threading
import os

os.system("title FranzeMacro V1")
os.system("cls")
os.system("color 0a")
os.system("echo FranzeMacro V1 is runnning, press Alt+F7 to force quit!")

def press_key():
    while not stop_event.is_set():
        keyboard.press_and_release('e')
        time.sleep(0.5)

def stop_program(event):
    if event.name == 'f7' and event.event_type == 'down' and keyboard.is_pressed('alt'):
        stop_event.set()

stop_event = threading.Event()

# Start the thread that presses 'E' every 0.5 seconds
thread = threading.Thread(target=press_key)
thread.start()

# Add a hook to listen for 'Alt + F7' to stop the program
keyboard.hook(stop_program)

print("Press 'Alt + F7' to stop the program.")

# Wait for the stop event
stop_event.wait()

# Clean up
keyboard.unhook_all()
thread.join()
print("Program stopped.")
