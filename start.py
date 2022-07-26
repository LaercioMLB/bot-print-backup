import pyautogui
import pyperclip

pyautogui.PAUSE = 1

# abrir nome do computador
pyautogui.hotkey('win','pause')
im1 = pyautogui.screenshot('nome-maquina')