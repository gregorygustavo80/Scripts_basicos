import requests

while True:
    def buscar_musicas(artista_banda, quantidade):
        try:
            url = f'https://itunes.apple.com/search?entity=song&limit={quantidade}&term={artista_banda}'
            response = requests.get(url)
            response.raise_for_status() 
            return response.json()['results']
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar músicas: {e}")
        return []

    artista_banda = input('Digite o nome de um artista ou banda: ')
    quantidade = input('Quantas músicas deseja procurar?')

    musicas = buscar_musicas(artista_banda, quantidade)

    for musica in musicas:
        print(musica['trackName'])