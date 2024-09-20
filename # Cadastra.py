class Livro:
    def __init__(self,codigo,titulo,autor,categoria,emprestado,preco):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.emprestado = emprestado
        self.preco = preco
    def __repr__(self):
        return (f'\nCódigo: {self.codigo}, '
                f'Título: {self.titulo}, '
                f'Autor: {self.autor}, '
                f'Categoria: {self.categoria}, '
                f'Emprestado: {self.emprestado}, '
                f'Preço: R${self.preco:.2f}\n')
    
class Biblioteca:
    def __init__(self):
        self.livros= [ 
            Livro(1, "Código Limpo", "Robert C. Martin", "Programação", False, 59.90),
            Livro(2, "Aprendizado Acelerado", "André de Almeida", "Educação", False, 39.90),
            Livro(3, "O Caminho do Mago", "Paulo Coelho", "Ficção", False, 29.90)
        ]
        
    def menu(self):
        print('---BEM VINDO AO MENU---')
        print('[1] CADASTRAR LIVRO')
        print('[2] REMOVER LIVRO')
        print('[3] EDITAR LIVRO')
        print('[4] BUSCAR LIVRO PELO CODIGO')
        print('[5] VER LISTA DE LIVROS')
        print('[6] ALUGAR LIVRO')
        print('[7] DEVOLVER LIVRO')
        print('[0] SAIR DO SISTEMA')

        return int(input('SELECIONE A OPÇÃO DESEJADA'))
    
    def addLivro(self):
            titulo= input("DIGITE NOME DO LIVRO")
            codigo = len(self.livros)+1
            autor= input("DIGITE AUTOR DO LIVRO")
            categoria= input("DIGITE CATEGORIA DO LIVRO")
            emprestado = (input("DIGITE STATUS DO LIVRO (True/False): ") == "True")
            preco = float(input("DIGITE PREÇO DO LIVROS"))
            livro = Livro(codigo,titulo,autor,categoria,emprestado,preco)
            self.livros.append(livro)
            print(f"\nLivro {livro.titulo} adicionado com sucesso\n")

    def removerLivro(self):
        codigo= int(input("DIGITE O CODIGO DO LIVRO QUE DESEJA REMOVER"))
        livro=self.buscarPorCodigo(codigo)
        if livro:
            self.livros.remove(livro)
            print("\nLivro removido com sucesso\n")
        print("\nLivro não encontrado\n")

    def editarLivro(self):
        codigo= int(input("DIGITE O CODIGO DO LIVRO QUE DESEJA REMOVER"))
        livro=self.buscarPorCodigo(codigo)
        if(livro):
            livro.titulo = input("DIGITE NOME DO LIVRO")
            livro.autor = input("DIGITE AUTOR DO LIVRO")
            livro.categoria= input("DIGITE CATEGORIA DO LIVRO")
            livro.emprestado = (input("DIGITE STATUS DO LIVRO (True/False): ") == "True")
            livro.preco = float(input("DIGITE PREÇO DO LIVROS"))
            print("\nLivro editado com sucesso\n")
        else:
            print("\nLivro não encontrado\n")

    def buscar(self):
        codigo= int(input("DIGITE O CODIGO DO LIVRO QUE DESEJA VER"))
        livro=self.buscarPorCodigo(codigo)
        if(livro):
            print(livro)
            return
        else:
            print('\nLivro não encontrado\n')

    def imprimirTodos(self):
        for livro in self.livros:
            print(livro)
        

    def buscarPorCodigo(self,codigo: int):
        for livro in self.livros:
            if livro.codigo == codigo:
                return livro
        return None 
    
    def alugar(self):
        codigo= int(input("DIGITE O CODIGO DO LIVRO QUE DESEJA ALUGAR"))
        livro=self.buscarPorCodigo(codigo)
        if livro:
            if(livro.emprestado==True):
                print("\nLivro não disponível\n")
                return
            else:
                livro.emprestado = True 
                print("\nLivro alugado com sucesso\n")
                return
        print("\nlivro não cadastrado")        

    def devolver(self):
        codigo= int(input("DIGITE O CODIGO DO LIVRO QUE DESEJA DEVOLVER"))
        livro=self.buscarPorCodigo(codigo)
        if livro:
            if(livro.emprestado==True):
                print("\nLivro devolvido com sucesso\n") 
                livro.emprestado = False
                return
            else: 
                print("\nLivro não encontrasse alugado\n") 
                return
        print("\nLivro não cadastrado\n") 

def selecionarFunc(biblioteca):
    opcao=biblioteca.menu()
    if(opcao == 1):
        biblioteca.addLivro()
    elif(opcao == 2):
        biblioteca.removerLivro()
    elif(opcao == 3):
        biblioteca.editarLivro()
    elif(opcao == 4):
        biblioteca.buscar()
    elif(opcao == 5):
        biblioteca.imprimirTodos()
    elif(opcao == 6):
        biblioteca.alugar()
    elif(opcao == 7):
        biblioteca.devolver()
    elif(opcao == 0):
        print("Saindo do sistema...")
        exit()

        
biblioteca = Biblioteca()
while True:
    selecionarFunc(biblioteca)


