from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, TIMESTAMP
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(255), nullable=False)
    estilo_instrucao: Mapped[str] = mapped_column(String(50), nullable=False, default="direto")
    criado_em: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=True)