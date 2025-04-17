import pyautogui
import time
import subprocess

class BlocoNotasSemImagem:
    """Classe que representa um bloco de notas sem uso de imagens. """
    def __init__(self):
        pass

    def abrirBlocoNotas(self, texto): 
        """Este função recebe o parâmeto texto para ser
           escrito e usa os métodos da biblioteca PyAutoGUI
           para realizar a automação com o bloco de notas.

           Argumentos:
           texto (str): texto a ser escrito.
        """
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