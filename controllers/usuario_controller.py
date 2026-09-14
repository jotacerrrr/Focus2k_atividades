from services.usuario_service import UsuarioService


class UsuarioController:
    def __init__(self, db_or_service=None):
        if isinstance(db_or_service, UsuarioService):
            self.service = db_or_service
        elif db_or_service is not None:
            self.service = UsuarioService(db_or_service)
        else:
            self.service = UsuarioService()

    def listar_perfis(self):
        try:
            usuarios = self.service.listar_usuarios()
            return {
                "sucesso": True,
                "tipo": "SUCESSO",
                "dados": [getattr(u, "nome", str(u)) for u in usuarios]
            }
        except Exception as e:
            return {
                "sucesso": False,
                "tipo": "FALHA_TECNICA",
                "mensagem": f"FALHA_TECNICA ({type(e).__name__}): {e}"
            }

    def criar_perfil(self, nome, escolha_estilo):
        estilo_input = str(escolha_estilo).strip().lower()

        # Mapeia valores "1", "2", "direto" e "detalhado"
        if estilo_input in {"1", "direto"}:
            estilo = "direto"
        elif estilo_input in {"2", "detalhado"}:
            estilo = "detalhado"
        else:
            return {
                "sucesso": False,
                "tipo": "REGRA_NEGOCIO",
                "mensagem": "Estilo inválido! Escolha 1 para Direto ou 2 para Detalhado."
            }

        try:
            # Tenta executar primeiro na assinatura padrão do projeto da Aula 03
            try:
                usuario = self.service.criar_usuario(nome, estilo)
            except TypeError:
                # Tenta executar na assinatura secundária (com parâmetro de senha)
                usuario = self.service.criar_usuario(nome=nome, senha="123", estilo_instrucao=estilo)

            nome_usuario = getattr(usuario, "nome", nome)

            return {
                "sucesso": True,
                "tipo": "SUCESSO",
                "mensagem": f"Perfil {nome_usuario} criado."
            }
        except ValueError as erro:
            return {
                "sucesso": False,
                "tipo": "REGRA_NEGOCIO",
                "mensagem": str(erro)
            }
        except Exception as e:
            # Retorna o tipo da exceção e a mensagem real do Python para identificação rápida
            return {
                "sucesso": False,
                "tipo": "FALHA_TECNICA",
                "mensagem": f"FALHA_TECNICA ({type(e).__name__}): {e}"
            }