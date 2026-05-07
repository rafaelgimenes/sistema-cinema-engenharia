from controllers.filme_controller import FilmeController

def main():
    controller = FilmeController()
    print("--- CINE-SISTEMA ---")
    filmes = controller.exibir_catalogo()
    for f in filmes:
        print(f"Filme: {f['titulo']} | Gênero: {f['genero']}")

if __name__ == "__main__":
    main()
