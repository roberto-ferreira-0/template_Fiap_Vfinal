import oracledb
import pandas as pd

usuario = "rm561131"
senha = "020196"
host = "oracle.fiap.com.br"
porta = 1521
servico = "ORCL" 


conn = oracledb.connect(f"{usuario}/{senha}@{host}:{porta}/{servico}")
cursor = conn.cursor()


df = pd.read_csv("dados/dados_dos_sensores_fase2_esp32.csv")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO tabela_fiap_dados_do_esp32
        (id, umidade, ph, temperatura, nitrogenio, fosforo, potassio, irrigacao)
        VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
    """, (
        int(row['id']),
        float(row['umidade']),
        float(row['ph']),
        float(row['temperatura']),
        float(row['nitrogenio']),
        float(row['fosforo']),
        float(row['potassio']),
        str(row['irrigacao'])
    ))

conn.commit()
cursor.close()
conn.close()
print("Dados rodados com sucesso na Oracle!")

print(df.head())

