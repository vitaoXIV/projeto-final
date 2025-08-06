
# REST COUNTRIES DESKTOP APP

Aplicação desktop desenvolvida em Python utilizando Tkinter para interface gráfica, que consome a API REST COUNTRIES. Permite pesquisar, filtrar e visualizar detalhes de países, além de persistir dados localmente em JSON.

## Funcionalidades
- Busca de países por nome
- Filtro por região e população
- Visualização de detalhes do país (nome, capital, região, população, área, moedas, bandeira)
- Alternância de tema claro/escuro
- Persistência local dos dados para acesso offline

## Ferramentas e Tecnologias
- **Python 3.8+**: Linguagem principal
- **Tkinter**: Interface gráfica
- **requests**: Consumo de API REST
- **Pillow**: Exibição de imagens (bandeiras)
- **JSON**: Persistência local dos dados

## Estrutura do Projeto
- `main.py`: Ponto de entrada da aplicação
- `gui/`: Interface gráfica (componentes, telas, tooltips, animações)
  - `components.py`: Listagem, filtros, tooltips, detalhes dos países
  - `screens.py`: Gerenciamento de telas e temas
- `api/`: Consumo da API REST COUNTRIES
  - `rest_countries.py`: Requisições HTTP e tratamento de dados
- `data/`: Persistência local
  - `storage.py`: Salva e carrega dados em JSON
  - `local_data.json`: Armazena os dados baixados

## Endpoints Utilizados
- `GET https://restcountries.com/v3.1/all`: Lista todos os países
- `GET https://restcountries.com/v3.1/name/{name}`: Busca país pelo nome

## Requisitos
- Python 3.8 ou superior
- Tkinter (normalmente já incluso no Python)
- requests
- pillow

## Como executar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
   Ou manualmente:
   ```bash
   pip install requests pillow
   ```
2. Execute o aplicativo:
   ```bash
   python main.py
   ```

## Observações
- O projeto salva os dados dos países em `data/local_data.json` para acesso offline.
- Caso a API esteja indisponível, os dados locais serão utilizados.
- Para exibir bandeiras, o pacote `pillow` deve estar instalado.

## Licença
Consulte o arquivo LICENSE para detalhes.
