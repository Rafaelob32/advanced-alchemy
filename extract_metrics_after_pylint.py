import os
import subprocess

# Cria o diretório de saída caso não exista
output_dir = "metrics-after-pylint"
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, "pylint_report.txt")

print("Executando Pylint pós-refatoração...")
# Executa o pylint na pasta do pacote principal
with open(output_file, "w", encoding="utf-8") as f:
    subprocess.run(["pylint", "advanced_alchemy"], stdout=f, stderr=subprocess.STDOUT)

print(f"Relatório do Pylint salvo com sucesso em: {output_file}")
