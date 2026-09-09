from sqlalchemy.orm import Session
from models.usuario import Usuario

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def buscar_por_id(self, usuario_id: int) -> Usuario | None:
        return self.session.get(Usuario, usuario_id)

    def buscar_por_nome(self, nome: str) -> Usuario | None:
        return self.session.query(Usuario).filter(Usuario.nome == nome).first()

    def salvar(self, usuario: Usuario) -> Usuario:
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def listar_todos(self) -> list[Usuario]:
        return self.session.query(Usuario).all()