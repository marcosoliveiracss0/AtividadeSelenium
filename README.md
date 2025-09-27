# AtividadeSelenium Marcos e Rayna

# Projeto de Automação com Selenium - Unieuro

Este script utiliza Python e Selenium para automatizar o processo de login na plataforma EAD Unieuro, navegar até um link específico e realizar o download de um arquivo PDF.

## Pré-requisitos

Antes de começar, garanta que você tenha os seguintes programas instalados no seu computador:

1.  **Python 3.8 ou superior:** [Baixe aqui](https://www.python.org/downloads/).
      * **Importante:** Durante a instalação, marque a caixa que diz "Add Python to PATH".
2.  **Google Chrome:** O navegador precisa estar instalado.
3.  **VS Code (ou outro editor de código):** [Baixe aqui](https://code.visualstudio.com/).

## Instalação e Configuração

Siga estes passos para configurar o ambiente e preparar o projeto para execução.

### Passo 1: Baixar o ChromeDriver

O Selenium precisa de um "motorista" (driver) para controlar o navegador Chrome.

1.  **Verifique sua versão do Chrome:** Abra o Chrome, digite `chrome://settings/help` na barra de endereços e anote a versão (ex: `117.0.5938.149`).
2.  **Baixe o driver correspondente:**
      * Acesse o site oficial: [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)
      * Encontre a seção que corresponde à sua versão (ex: **Stable**).
      * Na linha do `chromedriver`, clique no link de download para `chromedriver-win64.zip`.

### Passo 2: Organizar a Pasta do Projeto

A estrutura de pastas correta é essencial para o funcionamento do script.

1.  Crie a pasta principal do projeto, chamada `AutomacaoFinal`.
2.  Coloque o arquivo de script `automacao.py` dentro dela.
3.  Dentro da `AutomacaoFinal`, crie uma **subpasta** chamada `ChromeDriver`.
4.  Extraia o arquivo `.zip` que você baixou. Mova o arquivo `chromedriver.exe` para dentro da pasta `ChromeDriver`.

A estrutura final deve ser esta:

```
AutomacaoFinal/
│
├── ChromeDriver/
│   └── chromedriver.exe   <-- O driver fica aqui dentro
│
└── automacao.py           <-- O script fica aqui
```

### Passo 3: Configurar o Caminho no Script

1.  No seu Windows Explorer, navegue até a pasta `ChromeDriver` e clique na barra de endereço para copiar o caminho completo.

2.  Abra o arquivo `automacao.py` e cole este caminho na variável `CHROMEDRIVER_PATH`. O resultado deve ser algo assim (ajuste para o seu caminho real):

    ```python
    CHROMEDRIVER_PATH = r"C:\Users\aluno\Desktop\AutomacaoFinal\ChromeDriver\chromedriver.exe"
    ```

### Passo 4: Instalar as Dependências

1.  Abra a pasta `AutomacaoFinal` no VS Code.
2.  Abra um novo terminal (**Command Prompt**): `Ctrl + '` ou `Terminal > Novo Terminal`.
3.  Crie e ative o ambiente virtual:
    ```cmd
    python -m venv .venv
    .venv\Scripts\activate
    ```
4.  Instale o Selenium:
    ```cmd
    pip install selenium
    ```

## Execução

Com tudo configurado, para rodar a automação:

1.  Abra um novo terminal no VS Code (dentro da pasta `AutomacaoFinal`).
2.  Ative o ambiente virtual:
    ```cmd
    .venv\Scripts\activate
    ```
3.  Execute o script:
    ```cmd
    python automacao.py
    ```

O navegador Chrome irá abrir e executar todos os passos programados. O arquivo baixado será salvo na pasta `downloads`, que será criada dentro de `AutomacaoFinal`.

## Observações

  * Se o seu navegador Google Chrome for atualizado no futuro, o script pode parar de funcionar. Para corrigir, basta repetir o **Passo 1** e substituir o arquivo `chromedriver.exe` antigo pelo novo, compatível com a nova versão do Chrome.
