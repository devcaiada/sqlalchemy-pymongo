# Desafio Integração Sqlite e MongoDB no Python

## Parte 1 - Implementando um Banco de Dados Relacional com SQLAlchemy

### Objetivo:

Neste desafio você irá implementar uma aplicação de integração com SQLite com base em um esquema relacional disponibilizado. Sendo assim, utilize o esquema dentro do contexto de cliente e conta para criar as classes de sua API. Essas classes irão representar as tabelas do banco de dados relacional dentro da aplicação.

![image](https://github.com/devcaiada/sqlalchemy-pymongo/blob/main/images/transferir.png?raw=true)

### Entregável:

- Aplicação com a definição do esquema por meio das classes usando SQLAlchemy
- Inserção de um conjunto de dados mínimo para manipulação das informações
- Execução de métodos de recuperação de dados via SQLAlchemy

```python
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
```

### Arquivo .py

[SQLAlchemy](https://github.com/devcaiada/sqlalchemy-pymongo/blob/main/sql_integration.py)

---

## Parte 2 – Implementando um Banco de Dados NoSQL com Pymongo

Você irá implementar um banco NoSQL com mongodb para fornecer uma visão agregada do modelo relacional. Sendo assim, as informações de cliente e contas existentes estão contidas dentro de documentos de acordo com cliente.

### Execute as operações:

- Conecte ao mongo atlas e crie um banco de dados
- Defina uma coleção bank para criar os documetos de clientes
- Insira documentos com a estrutura mencionada
- Escreve instruções de recuperação de informações com base nos pares de chave e valor como feito em aula

```python
def connect_to_mongo(uri, db_name):
    client = MongoClient(uri)
    db = client[db_name]
    return db

# Função para inserir documentos na coleção 'bank'
def insert_documents(collection, documents):
    if isinstance(documents, list):
        collection.insert_many(documents)
    else:
        collection.insert_one(documents)

# Função para recuperar documentos com base em pares de chave-valor
def find_documents(collection, query):
    return list(collection.find(query))

# Exemplo de utilização
if __name__ == "__main__":
    # Substitua com sua URI do MongoDB Atlas
    uri = "mongodb+srv://caio_arruda:<password>@seu_cluster.mongodb.net/test?retryWrites=true&w=majority"
    db_name = "banco_de_dados"
    collection_name = "bank"

    # Conectar ao MongoDB Atlas
    db = connect_to_mongo(uri, db_name)
    collection = db[collection_name]
```

### Arquivo .py

[Pymongo](https://github.com/devcaiada/sqlalchemy-pymongo/blob/main/mongodb_integration.py)

---
