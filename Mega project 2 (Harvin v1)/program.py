import pyautogui
import pyperclip
import time

# Small delay so you can switch to the correct window
time.sleep(3)

# 1️⃣ Click the  instagram icon
pyautogui.click(1429, 1045)

time.sleep(1)

# 2️⃣ Drag to select text
pyautogui.moveTo(666, 154)
pyautogui.mouseDown()
pyautogui.moveTo(666, 940, duration=0.5)
pyautogui.mouseUp()

time.sleep(0.5)

# 3️⃣ Copy selected text (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')

time.sleep(0.5)

# 4️⃣ Get text from clipboard into variable
copied_text = pyperclip.paste()

print("Copied Text:")
print(copied_text)