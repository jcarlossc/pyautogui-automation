import pyautogui
import time
import subprocess

class BlocoNotasSemImagem:
    def __init__(self):
        pass

    def abrirBlocoNotas(self, texto): 
        subprocess.Popen(['notepad.exe']) # Abri o Bloco de Notas.
        time.sleep(3)  # Tempo para o Bloco de Notas abrir.

        pyautogui.write(texto, interval=0.05) # Recebe texto.
        time.sleep(3)

        pyautogui.hotkey('ctrl', 's') # Salvar o arquivo (Ctrl + S).
        time.sleep(3)

        pyautogui.write("exemplo01.txt", interval=0.05) # Nome do arquivo a ser calvo.
        time.sleep(3)
        pyautogui.press('enter') # Salva o arquivo ao pressionar enter
        time.sleep(3)
 
        pyautogui.hotkey('alt', 'f4') # Fechar o Bloco de Notas (Alt + F4)