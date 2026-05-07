class FilmeRepository:
    def __init__(self):
        self.filmes_db = [
            {"id": 1, "titulo": "Batman", "genero": "Ação", "duracao": 175},
            {"id": 2, "titulo": "Duna", "genero": "Sci-Fi", "duracao": 166}
        ]

    def buscar_todos(self):
        return self.filmes_db
