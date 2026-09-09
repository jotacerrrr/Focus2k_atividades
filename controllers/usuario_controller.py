from services.usuario_service import UsuarioService

class UsuarioController:
    def __init__(self, db):
        self.service = UsuarioService(db)

    def listar_perfis(self):
        usuarios = self.service.listar_usuarios()
        return [u.nome for u in usuarios]

    def criar_perfil(self, nome, escolha_estilo):
        escolha = str(escolha_estilo).strip()

        if escolha == "1":
            estilo = "direto"
        elif escolha == "2":
            estilo = "detalhado"
        else:
            return {"sucesso": False, "mensagem": "Estilo inválido! Escolha 1 para Direto ou 2 para Detalhado."}

        try:
            self.service.criar_usuario(nome=nome, senha="123", estilo_instrucao=estilo)
            return {"sucesso": True, "mensagem": "Perfil criado com sucesso!"}
        except ValueError as e:
            return {"sucesso": False, "mensagem": str(e)}