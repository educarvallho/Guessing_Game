import requests

def buscar_palavra():
    url = 'https://raw.githubusercontent.com/educarvallho/Guessing_Game/main/words.json'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança uma exceção se a requisição falhar
        return resposta.json()
    except requests.exceptions.RequestException as e:
        print("Erro ao obter palavras:", e)
        return None
