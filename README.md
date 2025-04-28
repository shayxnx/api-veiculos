API de Veículos
Documentação da API
1. Listar Todos os Veículos
Método: GET
Rota: /veiculos

Descrição:
Retorna uma lista de todos os veículos cadastrados.

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
    "preco": 75000.00
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

Descrição:
Retorna os dados de um veículo específico pelo seu ID.

Exemplo de resposta:

json
Copiar
Editar
{
  "id": 1,
  "modelo": "Civic",
  "marca": "Honda",
  "ano": 2020,
  "preco": 75000.00
}
3. Criar um Novo Veículo
Método: POST
Rota: /veiculos

Descrição:
Cria um novo veículo com base nos dados fornecidos no corpo da requisição.

Corpo da requisição (JSON):

json
Copiar
Editar
{
  "modelo": "Fiesta",
  "marca": "Ford",
  "ano": 2018,
  "preco": 45000.00
}
Exemplo de resposta:

json
Copiar
Editar
{
  "id": 3,
  "modelo": "Fiesta",
  "marca": "Ford",
  "ano": 2018,
  "preco": 45000.00
}
4. Atualizar um Veículo
Método: PUT
Rota: /veiculos/<int:veiculo_id>

Descrição:
Atualiza os dados de um veículo específico pelo seu ID.

Corpo da requisição (JSON):

json
Copiar
Editar
{
  "modelo": "Fiesta Titanium",
  "marca": "Ford",
  "ano": 2019,
  "preco": 47000.00
}
Exemplo de resposta:

json
Copiar
Editar
{
  "id": 3,
  "modelo": "Fiesta Titanium",
  "marca": "Ford",
  "ano": 2019,
  "preco": 47000.00
}
5. Deletar um Veículo
Método: DELETE
Rota: /veiculos/<int:veiculo_id>

Descrição:
Remove um veículo específico do banco de dados pelo seu ID.

Exemplo de resposta:

json
Copiar
Editar
{
  "mensagem": "Veículo excluído com sucesso"
}
