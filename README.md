# PyAutoGUI

Estudo sobre a biblioteca PyAutoGUI para automação e controle do sistema operacional em linguagem de programação Python e ambiente virtual Venv.
Especificamente, este pequeno projeto conta com duas classe: A primeira classe - BlocoNotasSemImagem - abre o bloco
de notas, escreve um pequeno texto, salva e fecha o software. A segunda - BlocoNotasComImagem - abre o bloco
de notas, escreve um pequeno texto, salva e fecha o software com a ajuda de uma imagem png.

PyAutoGUI: é uma biblioteca multiplataforma de automação da interface gráfica do usuário, usada para mover o mouse, clicar, digitar, pressionar teclas e interagir com elementos visuais na tela.

Venv: é um ambiente virtual em Python que isola dependências do projeto, evitando conflitos com pacotes globais do sistema. Ele permite que cada projeto tenha suas próprias bibliotecas e versões específicas.

## FERRAMENTAS UTILIZADAS:
* Linguagem de programação Python.
* Ambiente virtual VENV.
* Git/GitHub.
* Visual studio code.
* Windows 10.

## MODO DE UTILIZAR:
* Clonar repositório.
* Entrar no diretório do projeto ```cd pyautogui-automation```. 
* Executar ```python -m venv venv``` para instalar o ambiente virtual.
* Executar, caso esteja no Windows, ```venv\Scripts\activate``` para iniciar o ambiente. Caso Linux ou MacOS, ```source venv/bin/activate```.
* Executar ```pip install -r requirements.txt``` para instalar as dependências.
* ```python app.py``` - Executa o algoritmo.
* Para sair do ambiente virtual ```deactivate```.

## CONTRIBUIÇÕES:
Se quiser contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas na seção de issues.

## LICENÇA:
Este projeto é licenciado sob a Licença MIT.

## COMANDOS IMPORTANTES
* ```python -m venv venv``` - Cria um ambiente virtual chamado venv. Observação: o primeiro venv é o comando, o segundo, o nome do diretório.
* No Windows, ```venv\Scripts\activate``` e no Linux, ```source venv/bin/activate``` - Inicializa o ambiente.
* ```deactivate``` - Encerra o ambiente.
* ```pip freeze > requirements.txt``` - Gera o arquivo para instalação de dependências. Esse mesmo comando atualiza o arquivo quando uma dependência for instalada.
* ```pip list``` - Lista as dependências do projeto.
* ```pip show``` - Inserindo o nome da dependência após o comando, lista informações da dependência.
* ```pip install -r requirements.txt``` - Instala dependências que estão no arquivo 'requirements.txt'.
* ```pip install``` - Inserindo o nome da dependência após o comando, instala dependências.
* ```pip uninstall``` - Inserindo o nome da dependência após o comando, desinstala dependências.