from controllers.usuario_controller import UsuarioController
from config.database import SessionLocal

db = SessionLocal()
controller = UsuarioController(db)

while True:
    print("\n=== EXEMPLO AULA 02 ===")
    print("1. Listar perfis")
    print("2. Criar perfil")
    print("3. Sair")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        print("\nPerfis:")
        for nome in controller.listar_perfis():
            print("-", nome)

    elif opcao == "2":
        nome = input("Nome: ").strip()
        print("1. Direto")
        print("2. Detalhado")
        escolha = input("Estilo: ").strip()
        
        # Passa a escolha ("1" ou "2") direto para o controller
        resposta = controller.criar_perfil(nome, escolha)
        print(resposta["mensagem"])

    elif opcao == "3":
        db.close()
        break