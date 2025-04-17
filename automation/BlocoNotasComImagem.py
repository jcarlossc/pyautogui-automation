import pyautogui
import time
import subprocess

class BlocoNotasComImagem:
    """Classe que representa um bloco de notas com uso de imagens. """
    def __init__(self):
        pass

    def abrirBlocoNotas(self, texto): 
        """Este função recebe o parâmeto texto para ser
           escrito e usa os métodos da biblioteca PyAutoGUI
           para realizar a automação com o bloco de notas
           usando imagem para orientar o fechamento do software.

           Argumentos:
           texto (str): texto a ser escrito.
        """
        subprocess.Popen(['notepad.exe']) # Abri o Bloco de Notas.
        time.sleep(3)  # Tempo para o Bloco de Notas abrir.

        pyautogui.write(texto, interval=0.05) # Recebe texto.
        time.sleep(3)

        pyautogui.hotkey('ctrl', 's') # Salvar o arquivo (Ctrl + S).
        time.sleep(3)

        pyautogui.write("exemplo02.txt", interval=0.05) # Nome do arquivo a ser calvo.
        time.sleep(3)
        
        pyautogui.press('enter') # Salva o arquivo ao pressionar enter
        time.sleep(3)
 
        # Fecha o bloco de notas com uso de uma imgem do botão fechar da janela do software.
        # A imagem está no diretório img na raiz do projeto.
        img_fechar = pyautogui.locateOnScreen('img/fechar_bloco.png', confidence=0.9)

        # Testa se a imagem existe.
        if img_fechar:
            pyautogui.click(img_fechar)