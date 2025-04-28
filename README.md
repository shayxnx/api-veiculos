# api-veiculos

Documentação da API
1. Listar Todos os Veículos
Método: GET

Rota: /veiculos

Descrição: Retorna uma lista de todos os veículos cadastrados.

Exemplo de resposta:

json
Copiar
Editar
[
  {
    "id": 1,
    "modelo": "Civic",
    "marca": "Honda",
    "ano": 2020,
    "preco": 95000.00
  },
  {
    "id": 2,
    "modelo": "Corolla",
    "marca": "Toyota",
    "ano": 2021,
    "preco": 100000.00
  }
]
2. Listar um Veículo Específico
Método: GET

Rota: /veiculos/<int:veiculo_id>

Descrição: Retorna os dados de um veículo específico pelo seu ID.

Exemplo de resposta:

json
Copiar
Editar
{
  "id": 1,
  "modelo": "Civic",
  "marca": "Honda",
  "ano": 2020,
  "preco": 95000.00
}
3. Criar um Novo Veículo
Método: POST

Rota: /veiculos

Descrição: Cria um novo veículo com base nos dados fornecidos no corpo da requisição.

Corpo da requisição (JSON):

json
Copiar
Editar
{
  "modelo": "Onix",
  "marca": "Chevrolet",
  "ano": 2023,
  "preco": 75000.00
}
Exemplo de resposta:

json
Copiar
Editar
{
  "mensagem": "Veículo criado com sucesso!"
}
4. Atualizar um Veículo
Método: PUT

Rota: /veiculos/<int:veiculo_id>

Descrição: Atualiza os dados de um veículo específico pelo ID.

Corpo da requisição (JSON):

json
Copiar
Editar
{
  "modelo": "Civic Touring",
  "marca": "Honda",
  "ano": 2021,
  "preco": 120000.00
}
Exemplo de resposta:

json
Copiar
Editar
{
  "mensagem": "Veículo atualizado com sucesso!"
}
5. Deletar um Veículo
Método: DELETE

Rota: /veiculos/<int:veiculo_id>

Descrição: Remove um veículo específico do banco de dados pelo ID.

Exemplo de resposta:

json
Copiar
Editar
{
  "mensagem": "Veículo excluído com sucesso!"
}
Tecnologias Utilizadas
Python

Flask

SQLite

HTML

JavaScript (Fetch API)

CORS

