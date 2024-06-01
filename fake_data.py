from faker import Faker
import pandas as pd

fake = Faker('pt_BR')

num_registros = 100

dados_fake = []

for i in range(num_registros):
    dados = {
        'nome': fake.name(),
        'endereco': fake.address(),
        'email': fake.email(),
        'telefone': fake.phone_number(),
        'data_nascimento': fake.date_of_birth().strftime('%d/%m/%Y')
    }
    dados_fake.append(dados)

df = pd.DataFrame(dados_fake)

nome_arquivo = 'dados_fake.xlsx'
df.to_excel(nome_arquivo, index=False)

print(f"Os dados foram salvos em {nome_arquivo}")
