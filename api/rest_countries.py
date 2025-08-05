import requests

API_URL = 'https://restcountries.com/v3.1/'

class RestCountriesAPI:
    @staticmethod
    def get_all():
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0',
                'Accept': 'application/json',
                'Accept-Language': 'pt-BR,pt;q=0.9'
            }
            url = 'https://restcountries.com/v3.1/all'
            params = {'fields': 'name,capital,region,population,area,currencies,flags'}
            resp = requests.get(url, headers=headers, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            if not isinstance(data, list):
                return None, 'Formato inesperado de resposta da API.'
            return data, None
        except requests.exceptions.RequestException as e:
            return None, f'Erro de conexão: {e}'
        except ValueError as e:
            return None, f'Erro ao decodificar JSON: {e}'
        except Exception as e:
            return None, f'Erro inesperado: {type(e).__name__}: {e}'

    @staticmethod
    def get_by_name(name):
        if not name or not isinstance(name, str):
            return None, 'Nome inválido.'
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0',
                'Accept': 'application/json',
                'Accept-Language': 'pt-BR,pt;q=0.9'
            }
            url = f'https://restcountries.com/v3.1/name/{name}'
            params = {'fields': 'name,capital,region,population,area,currencies,flags'}
            resp = requests.get(url, headers=headers, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            if not isinstance(data, list):
                return None, 'Formato inesperado de resposta da API.'
            return data, None
        except requests.exceptions.RequestException as e:
            return None, f'Erro de conexão: {e}'
        except ValueError as e:
            return None, f'Erro ao decodificar JSON: {e}'
        except Exception as e:
            return None, f'Erro inesperado: {type(e).__name__}: {e}'

# Código fora da classe para execução imediata
url = 'https://restcountries.com/v3.1/all'
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json',
    'Accept-Language': 'pt-BR,pt;q=0.9'
}
params = {'fields': 'name,capital,region,population,area,currencies'}
resp = requests.get(url, headers=headers, params=params, timeout=10)
print(resp.status_code)
print(resp.json())
