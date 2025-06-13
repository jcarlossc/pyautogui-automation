import pyautogui # Biblioteca Python usada para automação de GUI.
import time # Módulo que oferece ferramentas para trabalhar com funcionalidades relacionadas ao tempo.
import subprocess # Módulo subprocesso em Python permite que você crie novos processos.

class BlocoNotasSemImagem:
    """Classe que automatiza o uso de um bloco de notas sem uso de imagens. """
    def __init__(self) -> None:
        pass

    def abrirBlocoNotas(self, texto: str) -> None: 
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

        pyautogui.write("exemplo04.txt", interval=0.05) # Nome do arquivo a ser salvo.
        time.sleep(3)
        pyautogui.press('enter') # Salva o arquivo ao pressionar enter
        time.sleep(3)
 
        pyautogui.hotkey('alt', 'f4') # Fechar o Bloco de Notas (Alt + F4)