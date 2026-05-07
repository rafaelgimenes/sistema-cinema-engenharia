from repositories.filme_repository import FilmeRepository

class FilmeService:
    def __init__(self):
        self.repository = FilmeRepository()

    def listar_filmes_disponiveis(self):
        return self.repository.buscar_todos()
