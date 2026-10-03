import os
import sqlite3
import pandas as pd

# Caminhos dos arquivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, '..', 'dados', 'simulacao_acidentes_transito_brasil.csv')
DB_DIR = os.path.join(BASE_DIR, '..', 'database')
DB_PATH = os.path.join(DB_DIR, 'acidentes.db')

os.makedirs(DB_DIR, exist_ok=True)

def inicializar_banco():
    print("🔄 Lendo o dataset original de acidentes...")
    df = pd.read_csv(CSV_PATH)
    
    print("🔄 Criando a tabela no banco SQLite...")
    conn = sqlite3.connect(DB_PATH)
    
    # Grava os dados na tabela 'acidentes'
    df.to_sql('acidentes', conn, if_exists='replace', index=False)
    
    # Criação de índices para consultas ultra-rápidas
    cursor = conn.cursor()
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_ano ON acidentes(ano);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_uf ON acidentes(uf);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_regiao ON acidentes(regiao);")
    conn.commit()
    
    print("✅ Banco de dados 'acidentes.db' criado com sucesso na pasta 'database/'!")
    conn.close()

if __name__ == '__main__':
    inicializar_banco()