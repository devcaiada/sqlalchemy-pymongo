from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Cria uma base declarativa para as classes
Base = declarative_base()


# Define a classe CLIENTE
class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    endereco = Column(String, nullable=False)
    contas = relationship("Conta", back_populates="cliente")


# Define a classe CONTA
class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Binary, primary_key=True)
    tipo = Column(String, nullable=False)
    agencia = Column(String, nullable=False)
    num = Column(Integer, nullable=False)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    saldo = Column(DECIMAL, nullable=False)
    cliente = relationship("Cliente", back_populates="contas")


# Cria o engine do banco de dados
engine = create_engine('sqlite:///banco.db')

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Exemplo de como adicionar um cliente e uma conta
novo_cliente = Cliente(nome='João Silva', cpf='12345678901', endereco='Rua das Flores, 123')
session.add(novo_cliente)
session.commit()

# Adicionando uma conta para o cliente
nova_conta = Conta(id=b'12345678', tipo='Corrente', agencia='001', num=12345, id_cliente=novo_cliente.id, saldo=1000.00)
session.add(nova_conta)
session.commit()

# Fechando a sessão
session.close()
