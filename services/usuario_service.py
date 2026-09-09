from sqlalchemy.orm import Session
from repositories.usuario_repository import UsuarioRepository
from models.usuario import Usuario

class UsuarioService:
    def __init__(self, db_or_repo=None, repository=None):
        # Compatibilidade com testes (recebendo repositório direto) e produção (recebendo sessão do banco)
        if repository:
            self.repository = repository
        elif hasattr(db_or_repo, "query") or isinstance(db_or_repo, Session):
            self.repository = UsuarioRepository(db_or_repo)
        else:
            # Caso o teste passe o repositório falso direto no primeiro argumento
            self.repository = db_or_repo

    def criar_usuario(self, nome: str, senha: str, estilo_instrucao: str = "direto") -> Usuario:
        if not nome or not nome.strip():
            raise ValueError("O nome do usuário não pode ser vazio.")
            
        # Valida se o estilo de instrução é permitido
        estilos_permitidos = ["direto", "detalhado"]
        if estilo_instrucao not in estilos_permitidos:
            raise ValueError(f"Estilo de instrução inválido. Escolha entre: {', '.join(estilos_permitidos)}.")
            
        if self.repository.buscar_por_nome(nome):
            raise ValueError("Já existe um usuário cadastrado com este nome.")
        
        novo_usuario = Usuario(nome=nome, senha=senha, estilo_instrucao=estilo_instrucao)
        return self.repository.salvar(novo_usuario)

    def buscar_por_id(self, usuario_id: int) -> Usuario | None:
        return self.repository.buscar_por_id(usuario_id)

    def buscar_por_nome(self, nome: str) -> Usuario | None:
        return self.repository.buscar_por_nome(nome)

    def listar_usuarios(self) -> list[Usuario]:
        return self.repository.listar_todos()