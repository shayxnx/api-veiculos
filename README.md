# API de Veículos

## 📄 Documentação da API

---

## 🔍 1. Listar Todos os Veículos
- **Método:** `GET`
- **Rota:** `/veiculos`
- **Descrição:** Retorna uma lista de todos os veículos cadastrados.

### 🛠 Exemplo de resposta:
```json
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
