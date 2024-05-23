from pymongo import MongoClient

# Função para conectar ao MongoDB Atlas
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

    # Estrutura de exemplo para os documentos dos clientes
    clientes = [
        {
            "nome": "Caio Arruda",
            "idade": 31,
            "endereco": "Rua das Dores, 123",
            "conta": {
                "tipo": "corrente",
                "saldo": 1000.00
            }
        },
        {
            "nome": "Thais Princesa",
            "idade": 25,
            "endereco": "Rua das Alegrias, 456",
            "conta": {
                "tipo": "poupança",
                "saldo": 3000.00
            }
        }
    ]

    # Inserir documentos na coleção
    insert_documents(collection, clientes)

    # Recuperar documentos com base em pares de chave-valor
    query = {"conta.tipo": "corrente"}
    resultados = find_documents(collection, query)

    # Imprimir resultados
    for doc in resultados:
        print(doc)
