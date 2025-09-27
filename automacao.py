# login_unieuro_final.py
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# ===== CONFIGURAÇÕES FINAIS =====
LOGIN = "07097896108"
SENHA = "07097896108"
URL_LOGIN = "https://ead.unieuro.edu.br/login/index.php"

# --- URL DIRETA DO ARQUIVO ---
# Após o login, vamos navegar diretamente para este link para forçar o download.
URL_DOWNLOAD_DIRETO = "https://ead.unieuro.edu.br/pluginfile.php/58764/mod_resource/content/1/globo.pdf"

# --- CAMINHOS ---
# Caminho corrigido para o seu chromedriver.exe dentro da subpasta.
CHROMEDRIVER_PATH = r"C:\Users\aluno\Desktop\AutomacaoFinal\ChromeDriver\chromedriver.exe"
# Cria uma pasta 'downloads' dentro da pasta do seu projeto.
DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")


def create_driver():
    """Configura e cria a instância do WebDriver (navegador)."""
    if not os.path.exists(CHROMEDRIVER_PATH):
        raise FileNotFoundError(f"ChromeDriver não encontrado! Verifique se ele está no caminho: {CHROMEDRIVER_PATH}")

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Preferências de download para baixar o PDF automaticamente.
    prefs = {
        "download.default_directory": DOWNLOAD_DIR,
        "plugins.always_open_pdf_externally": True,
    }
    options.add_experimental_option("prefs", prefs)

    service = ChromeService(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def main():
    """Função principal que executa a automação."""
    driver = None
    try:
        driver = create_driver()
        wait = WebDriverWait(driver, 20)

        # --- 1. Login ---
        print(f"Acessando a URL de login: {URL_LOGIN}")
        driver.get(URL_LOGIN)

        print("Preenchendo credenciais...")
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(LOGIN)
        driver.find_element(By.ID, "password").send_keys(SENHA)
        driver.find_element(By.ID, "loginbtn").click()
        print("Login realizado com sucesso!")
        
        # Espera um momento para a sessão de login ser estabelecida.
        time.sleep(3)

        # --- 2. Download Direto ---
        print(f"Acessando a URL de download direto: {URL_DOWNLOAD_DIRETO}")
        driver.get(URL_DOWNLOAD_DIRETO)
        
        # Pausa para dar tempo ao download iniciar e completar.
        print(f"Download iniciado. O arquivo será salvo em: {os.path.abspath(DOWNLOAD_DIR)}")
        print("Aguardando 15 segundos para o download completar...")
        time.sleep(15)

        print("\n>>> Automação concluída com sucesso! <<<")

    except Exception as e:
        print(f"\n[ERRO] Ocorreu uma falha inesperada durante a automação: {e}")

    finally:
        if driver:
            print("Fechando o navegador em 10 segundos...")
            time.sleep(10)
            driver.quit()
            print("Navegador fechado.")


# --- Ponto de Entrada do Script ---
if __name__ == "__main__":
    main()