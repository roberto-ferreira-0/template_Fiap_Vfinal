import cx_Oracle
import pandas as pd

usuario = "rm561131"
senha = "020196"
host = "oracle.fiap.com.br"
porta = 1521
servico = "ORCL"  # nome do serviço (ex: xe, ORCL)


conn = cx_Oracle.connect(f"{usuario}/{senha}@{host}:{porta}/{servico}")
cursor = conn.cursor()


df = pd.read_csv("dados/dados_dos_sensores_fase2_esp32.csv")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO tabela_fiap_dados_do_esp32
        (id, umidade, ph, temperatura, nitrogenio, fosforo, potassio, irrigacao)
        VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
    """, tuple(row))


conn.commit()
cursor.close()
conn.close()

print("Dados importados com sucesso na tabela existente!")
