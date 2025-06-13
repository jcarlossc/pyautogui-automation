import pyautogui # Biblioteca Python usada para automação de GUI.
import time # Módulo que oferece ferramentas para trabalhar com funcionalidades relacionadas ao tempo.
import subprocess # Módulo subprocesso em Python permite que você crie novos processos.

class BlocoNotasComImagem:
    """Classe que automatiza o uso de um bloco de notas com uso de imagem. """
    def __init__(self) -> None:
        pass

    def abrir_bloco_notas(self, texto: str) -> None: 
        """Esta função recebe o parâmeto texto para ser
           escrito e usa os métodos da biblioteca PyAutoGUI
           para realizar a automação com o bloco de notas
           usando imagem para orientar o fechamento do software.

           Argumentos:
           texto (str): texto a ser escrito.
        """
        subprocess.Popen(['notepad.exe']) # Abre o Bloco de Notas.
        time.sleep(3)  # Tempo para o Bloco de Notas abrir.

        pyautogui.write(texto, interval=0.05) # Recebe texto.
        time.sleep(3)

        pyautogui.hotkey('ctrl', 's') # Salvar o arquivo (Ctrl + S).
        time.sleep(3)

        pyautogui.write("exemplo02.txt", interval=0.05) # Nome do arquivo a ser salvo.
        time.sleep(3)
        
        pyautogui.press('enter') # Salva o arquivo ao pressionar enter.
        time.sleep(3)

        try:
            # Fecha o bloco de notas com uso de uma imagem do botão fechar da janela do software.
            # A imagem está no diretório img na raiz do projeto.
            img_fechar = pyautogui.locateCenterOnScreen('img/fechar_bloco.png', confidence=0.7)

            # Testa se a imagem existe.
            if img_fechar:
                pyautogui.click(img_fechar)
            else:
                print("Imagem não encontrada na tela.")
                
        except pyautogui.ImageNotFoundException:
            print("Imagem do botão fechar não localizada.")