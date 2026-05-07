from services.filme_service import FilmeService

class FilmeController:
    def __init__(self):
        self.service = FilmeService()

    def exibir_catalogo(self):
        return self.service.listar_filmes_disponiveis()
