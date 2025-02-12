from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from docx import Document
import os
import time

# Função para remover a formatação de moeda R$ caso seja aplicada
def remover_formatacao_monetaria(valor):
    valor = valor.replace('R$', '').replace(' ', '').replace(',', '.')
    return valor

# Função para inserir valores de documento Word no formulário sem alterar o formato dos números
def inserir_valores_de_documento_word(caminho_arquivo_word, driver):
    try:
        # Extrair os dados do arquivo Word
        arquivo_word = Document(caminho_arquivo_word)

        # Inicializar as variáveis com valores vazios
        ativo_circulante = ''
        caixa_equivalentes = ''
        contas_receber = ''
        estoques = ''
        ativo_nao_circulante = ''
        imobilizado = ''
        intangivel = ''
        total_ativo = ''

        # Iterar sobre as tabelas e linhas do arquivo Word
        for tabela in arquivo_word.tables:
            for linha in tabela.rows:
                # Extração dos valores das células
                if 'Ativo Circulante' in linha.cells[0].text.strip():
                    ativo_circulante = linha.cells[1].text.strip()
                elif 'Caixa e Equivalentes' in linha.cells[0].text.strip():
                    caixa_equivalentes = linha.cells[1].text.strip()
                elif 'Contas a Receber' in linha.cells[0].text.strip():
                    contas_receber = linha.cells[1].text.strip()
                elif 'Estoques' in linha.cells[0].text.strip():
                    estoques = linha.cells[1].text.strip()
                elif 'Ativo Não Circulante' in linha.cells[0].text.strip():
                    ativo_nao_circulante = linha.cells[1].text.strip()
                elif 'Imobilizado' in linha.cells[0].text.strip():
                    imobilizado = linha.cells[1].text.strip()
                elif 'Intangível' in linha.cells[0].text.strip():
                    intangivel = linha.cells[1].text.strip()
                elif 'Total do Ativo' in linha.cells[0].text.strip():
                    total_ativo = linha.cells[1].text.strip()

        # Debug: Exibir os valores extraídos antes de preenchê-los
        print(f"Ativo Circulante: {ativo_circulante}")
        print(f"Caixa e Equivalentes: {caixa_equivalentes}")
        print(f"Contas a Receber: {contas_receber}")
        print(f"Estoques: {estoques}")
        print(f"Ativo Não Circulante: {ativo_nao_circulante}")
        print(f"Imobilizado: {imobilizado}")
        print(f"Intangível: {intangivel}")
        print(f"Total do Ativo: {total_ativo}")

        # Preencher os campos do formulário com os valores extraídos exatamente como estão
        campos = {
            'ativo_circulante': ativo_circulante,
            'caixa_equivalentes': caixa_equivalentes,
            'contas_receber': contas_receber,
            'estoques': estoques,
            'ativo_nao_circulante': ativo_nao_circulante,
            'imobilizado': imobilizado,
            'intangivel': intangivel,
            'total_ativo': total_ativo
        }

        for campo_id, valor in campos.items():
            if valor:
                campo = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//input[@id='{campo_id}']"))
                )
                driver.execute_script(f"arguments[0].value = '{valor}';", campo)
                time.sleep(1)

        # Clicar no botão cadastrar
        botao_cadastrar = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        botao_cadastrar.click()

        print(f"Dados cadastrados com sucesso para o arquivo: {caminho_arquivo_word}")

    except Exception as e:
        print(f"Erro ao cadastrar balanço patrimonial: {e}")

# Função para processar arquivos .docx na pasta
def processar_arquivos(driver):
    pasta_relatorios = r'C:\Users\bruno\Downloads\python projeto 1\relatorios'

    for nome_arquivo in os.listdir(pasta_relatorios):
        if nome_arquivo.endswith('.docx'):
            caminho_arquivo_word = os.path.join(pasta_relatorios, nome_arquivo)
            inserir_valores_de_documento_word(caminho_arquivo_word, driver)

# 1- Entrar no site
driver = webdriver.Chrome()
driver.get('https://contabil-devaprender.netlify.app/')

# 2- Preencher email, senha e entrar
campo_email = driver.find_element(By.XPATH, "//input[@type='email']")
time.sleep(1)
campo_email.send_keys('brunoteste@gmail.com')

campo_senha = driver.find_element(By.XPATH, "//input[@type='password']")
time.sleep(1)
campo_senha.send_keys('12345678')

# Diminuir a velocidade do login com um pequeno tempo de espera após cada campo
time.sleep(1)  # Espera para simular um tempo mais realista para o preenchimento
botao_entrar = driver.find_element(By.XPATH, "//button[@class='btn btn-primary w-100']")
botao_entrar.click()

# Aguardar o carregamento da página de entrada para garantir que a segunda tela esteja visível
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='btn btn-primary mt-auto']")))

# 3- Cadastrar Balanço Patrimonial
botoes_sistemas = driver.find_elements(By.XPATH, "//a[@class='btn btn-primary mt-auto']")
time.sleep(2)
botoes_sistemas[0].click()

# Espera explícita para garantir que a próxima tela tenha carregado
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='ativo_circulante']")))  # Espera pelo campo do "Ativo Circulante"

# Processar os arquivos .docx
processar_arquivos(driver)

# Pausar para você visualizar a execução antes de fechar o navegador
input("Pressione Enter para fechar o navegador...")

# Fechar o navegador após a execução
driver.quit()
