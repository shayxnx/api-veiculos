from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)

# Configure o CORS para permitir requisições do seu frontend
CORS(app, origins=['http://127.0.0.1:5500'])

# Função para conectar ao banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row  # Para retornar dados como dicionário
    return conn

# Função para criar a tabela de veículos
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "tabela de veiculos" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            marca TEXT NOT NULL,
            ano INTEGER NOT NULL,
            preco REAL NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

# Chama a função para criar a tabela ao iniciar a aplicação
create_table()

# Rota para listar todos os veículos
@app.route('/veiculos', methods=['GET'])
def get_veiculos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "tabela de veiculos"')
    veiculos = cursor.fetchall()
    conn.close()

    return jsonify([{
        'id': veiculo['id'],
        'modelo': veiculo['modelo'],
        'marca': veiculo['marca'],
        'ano': veiculo['ano'],
        'preco': veiculo['preco']
    } for veiculo in veiculos])

# Rota para listar um veículo específico
@app.route('/veiculos/<int:veiculo_id>', methods=['GET'])
def get_veiculo(veiculo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "tabela de veiculos" WHERE id = ?', (veiculo_id,))
    veiculo = cursor.fetchone()
    conn.close()

    if veiculo is None:
        return jsonify({'mensagem': 'Veículo não encontrado'}), 404

    return jsonify({
        'id': veiculo['id'],
        'modelo': veiculo['modelo'],
        'marca': veiculo['marca'],
        'ano': veiculo['ano'],
        'preco': veiculo['preco']
    })

# Rota para criar um novo veículo
@app.route('/veiculos', methods=['POST'])
def create_veiculo():
    dados = request.get_json()

    if not all(key in dados for key in ['modelo', 'marca', 'ano', 'preco']):
        return jsonify({'mensagem': 'Dados incompletos!'}), 400

    modelo = dados['modelo']
    marca = dados['marca']
    ano = dados['ano']
    preco = dados['preco']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO "tabela de veiculos" (modelo, marca, ano, preco)
        VALUES (?, ?, ?, ?)
    ''', (modelo, marca, ano, preco))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Veículo criado com sucesso!'}), 201

# Rota para atualizar um veículo
@app.route('/veiculos/<int:veiculo_id>', methods=['PUT'])
def update_veiculo(veiculo_id):
    dados = request.get_json()

    if not all(key in dados for key in ['modelo', 'marca', 'ano', 'preco']):
        return jsonify({'mensagem': 'Dados incompletos!'}), 400

    modelo = dados['modelo']
    marca = dados['marca']
    ano = dados['ano']
    preco = dados['preco']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE "tabela de veiculos"
        SET modelo = ?, marca = ?, ano = ?, preco = ?
        WHERE id = ?
    ''', (modelo, marca, ano, preco, veiculo_id))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Veículo atualizado com sucesso!'})

# Rota para excluir um veículo
@app.route('/veiculos/<int:veiculo_id>', methods=['DELETE'])
def delete_veiculo(veiculo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "tabela de veiculos" WHERE id = ?', (veiculo_id,))
    veiculo = cursor.fetchone()

    if veiculo is None:
        conn.close()
        return jsonify({'mensagem': 'Veículo não encontrado'}), 404

    cursor.execute('DELETE FROM "tabela de veiculos" WHERE id = ?', (veiculo_id,))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Veículo excluído com sucesso!'})

# Rota para servir a página HTML
@app.route('/')
def home():
    return render_template('index.html')

# Inicializa a aplicação
if __name__ == '__main__':
    app.run(debug=True)
