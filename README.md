# Aplicação Desktop REST COUNTRIES

Este projeto é uma aplicação desktop em Python (Tkinter) que consome a API REST COUNTRIES, exibindo informações de países e persistindo dados localmente.

## Como executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o aplicativo:
   ```bash
   python main.py
   ```

## Estrutura do Projeto
- `main.py`: Ponto de entrada da aplicação
- `gui/`: Interface gráfica (telas e componentes)
- `api/`: Consumo da API REST COUNTRIES
- `data/`: Persistência local (JSON)

## Endpoints Utilizados
- `https://restcountries.com/v3.1/all` (GET)
- `https://restcountries.com/v3.1/name/{name}` (GET)

## Requisitos
- Python 3.8+
- Tkinter
- requests

## Licença
Veja o arquivo LICENSE para detalhes.
