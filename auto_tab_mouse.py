# import pyautogui
# import time
# import random

# # Ensure a safe exit is possible
# pyautogui.FAILSAFE = True

# # Slow down PyAutoGUI actions
# pyautogui.PAUSE = 1  # Add a 1-second pause after each PyAutoGUI call

# def user_input_detected():
#     current_pos = pyautogui.position()
#     time.sleep(0.5)  # Check for input every half second
#     return current_pos != pyautogui.position()

# def switch_tab(direction):
#     if direction == 'next':
#         pyautogui.hotkey('ctrl', 'tab')
#     else:
#         pyautogui.hotkey('ctrl', 'shift', 'tab')
#     time.sleep(random.uniform(3, 5))  # Random pause between 3 to 5 seconds after switching tabs

# def perform_tab_switching():
#     num_switches = random.randint(3, 7)  # Random number of tab switches
    
#     for _ in range(num_switches):
#         direction = random.choice(['next', 'previous'])
#         switch_tab(direction)
#         if user_input_detected():
#             return True
    
#     return False

# def main_loop():
#     while True:
#         if perform_tab_switching():
#             return
        
#         # Longer pause before next switching cycle
#         pause_duration = random.uniform(8, 12)  # Random pause between 8 to 12 seconds
#         for _ in range(int(pause_duration * 2)):  # Check for input every 0.5 seconds
#             if user_input_detected():
#                 return
#             time.sleep(0.5)

# if __name__ == "__main__":
#     print("Starting gentle VSCode tab switching script...")
#     print("Ensure VSCode is open with multiple tabs before running this script.")
#     print("The script will gently switch between open tabs in VSCode.")
#     print("Move your mouse or use your keyboard at any time to stop the script.")
#     print("You can also move the mouse to the upper-left corner to abort.")
    
#     # Give user time to switch to VSCode
#     for i in range(5, 0, -1):
#         print(f"Starting in {i} seconds...")
#         time.sleep(1)
    
#     try:
#         main_loop()
#     except pyautogui.FailSafeException:
#         print("\nScript aborted by user (mouse moved to upper-left corner).")
#     except Exception as e:
#         print(f"\nAn error occurred: {e}")
#     finally:
#         print("Script ended due to user input or an error.")
import pyautogui
import time
import random

# Ensure a safe exit is possible
pyautogui.FAILSAFE = True

# Slow down PyAutoGUI actions
pyautogui.PAUSE = 0.5  # Add a 0.5-second pause after each PyAutoGUI call

def user_input_detected():
    current_pos = pyautogui.position()
    time.sleep(0.5)  # Check for input every half second
    return current_pos != pyautogui.position()

def move_mouse_smoothly(x, y):
    pyautogui.moveTo(x, y, duration=1, tween=pyautogui.easeInOutQuad)
    time.sleep(random.uniform(0.5, 1))

def switch_tab(direction):
    if direction == 'next':
        pyautogui.hotkey('ctrl', 'tab')
    else:
        pyautogui.hotkey('ctrl', 'shift', 'tab')
    time.sleep(random.uniform(1, 2))

def navigate_in_file(direction, amount):
    key = 'down' if direction == 'down' else 'up'
    for _ in range(amount):
        pyautogui.press(key)
        time.sleep(0.1)
    time.sleep(random.uniform(0.5, 1))

def perform_random_action():
    actions = [
        lambda: switch_tab(random.choice(['next', 'previous'])),
        lambda: navigate_in_file('down', random.randint(5, 20)),
        lambda: navigate_in_file('up', random.randint(5, 20)),
        lambda: move_mouse_smoothly(random.randint(200, 800), random.randint(200, 600))
    ]
    
    action = random.choice(actions)
    action()

def main_loop():
    while True:
        num_actions = random.randint(3, 8)
        
        for _ in range(num_actions):
            perform_random_action()
            
            if user_input_detected():
                return
        
        # Pause before next interaction cycle
        pause_duration = random.uniform(2, 5)
        for _ in range(int(pause_duration * 2)):  # Check for input every 0.5 seconds
            if user_input_detected():
                return
            time.sleep(0.5)

if __name__ == "__main__":
    print("Starting randomized VSCode interaction script...")
    print("Ensure VSCode is open with multiple tabs and files before running this script.")
    print("The script will interact with VSCode, switching tabs and navigating within files.")
    print("Move your mouse or use your keyboard at any time to stop the script.")
    print("You can also move the mouse to the upper-left corner to abort.")
    
    # Give user time to switch to VSCode
    for i in range(5, 0, -1):
        print(f"Starting in {i} seconds...")
        time.sleep(1)
    
    try:
        main_loop()
    except pyautogui.FailSafeException:
        print("\nScript aborted by user (mouse moved to upper-left corner).")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        print("Script ended due to user input or an error.")