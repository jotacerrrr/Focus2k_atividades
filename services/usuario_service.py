from sqlalchemy.orm import Session
from repositories.usuario_repository import UsuarioRepository
from models.usuario import Usuario

class UsuarioService:
    def __init__(self, db_or_repo=None, repository=None):
        if repository:
            self.repository = repository
        elif hasattr(db_or_repo, "query") or isinstance(db_or_repo, Session):
            self.repository = UsuarioRepository(db_or_repo)
        else:
            self.repository = db_or_repo

    def criar_usuario(self, nome: str, senha: str = "123", estilo_instrucao: str = "direto") -> Usuario:
        nome_limpo = nome.strip() if nome else ""

        if not nome_limpo:
            raise ValueError("O nome do usuário não pode ser vazio.")
            
        if len(nome_limpo) < 3:
            raise ValueError("O nome do usuário deve ter no mínimo 3 caracteres.")
            
        estilos_permitidos = ["direto", "detalhado"]
        if estilo_instrucao not in estilos_permitidos:
            raise ValueError(f"Estilo de instrução inválido. Escolha entre: {', '.join(estilos_permitidos)}.")
            
        if self.repository.buscar_por_nome(nome_limpo):
            raise ValueError("Já existe um usuário cadastrado com este nome.")
        
        novo_usuario = Usuario(nome=nome_limpo, senha=senha, estilo_instrucao=estilo_instrucao)
        return self.repository.salvar(novo_usuario)

    def buscar_por_id(self, usuario_id: int) -> Usuario | None:
        return self.repository.buscar_por_id(usuario_id)

    def buscar_por_nome(self, nome: str) -> Usuario | None:
        return self.repository.buscar_por_nome(nome)

    def listar_usuarios(self) -> list[Usuario]:
        return self.repository.listar_todos()