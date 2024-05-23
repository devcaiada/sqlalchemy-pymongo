# Desafio Integração Sqlite e MongoDB no Python


![image]()
~~~python
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
~~~

