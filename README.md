# Automação de Preenchimento de Formulários Contábeis com Selenium e Python

Este projeto visa automatizar o processo de preenchimento de formulários contábeis online, extraindo dados de documentos **Word (.docx)** e preenchendo os campos do formulário em um site contábil. O código foi desenvolvido em **Python** utilizando as bibliotecas **Selenium** e **python-docx**.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver a automação.
- **Selenium WebDriver**: Biblioteca para controle e automação do navegador (Chrome, Firefox, etc.) para interação com o site.
- **python-docx**: Biblioteca para ler e extrair dados de arquivos **.docx** (Word).
- **XPath**: Técnica usada para localizar elementos no HTML da página e interagir com eles.
- **WebDriverWait**: Utilizado para garantir que os elementos da página estejam carregados antes de realizar a interação.

## Funcionalidade

1. **Login no Sistema Contábil**: O script realiza o login no site de um sistema contábil usando as credenciais fornecidas.
2. **Extração de Dados de Documentos Word**: Os dados financeiros, como **Ativo Circulante**, **Caixa e Equivalentes**, **Contas a Receber**, entre outros, são extraídos de documentos **Word** armazenados localmente.
3. **Preenchimento Automático de Formulários**: O script preenche automaticamente os campos de um formulário online com os dados extraídos do arquivo **.docx**.
4. **Envio do Formulário**: Após preencher os campos, o script submete o formulário ao clicar no botão de cadastro.

## Como Funciona

1. **Configuração do Ambiente**:
   - Instalar o **ChromeDriver** (ou outro driver compatível com seu navegador) e configurá-lo corretamente.
   - Instalar as dependências utilizando **pip**:

     ```bash
     pip install selenium python-docx
     ```

2. **Pré-Requisitos**:
   - Ter o navegador **Google Chrome** ou outro navegador compatível com Selenium.
   - Baixar o **ChromeDriver** ou **GeckoDriver** (dependendo do navegador escolhido).
   - Ter os arquivos **Word (.docx)** que contêm os dados do balanço patrimonial a serem extraídos.

3. **Execução do Script**:
   - Altere a variável `pasta_relatorios` para apontar para o diretório onde seus arquivos **.docx** estão armazenados.
   - Execute o script:

     ```bash
     python seu_script.py
     ```

   - O script realizará o login no site, preencherá os campos do formulário e os enviará com base nos dados extraídos dos documentos Word.

## Estrutura de Arquivos

```plaintext
seu_projeto/
├── seu_script.py            # Script principal de automação
└── relatorios/              # Pasta com arquivos .docx a serem processados
    ├── relatorio1.docx
    ├── relatorio2.docx
    └── ...
