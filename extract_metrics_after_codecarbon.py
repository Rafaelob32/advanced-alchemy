import os
import subprocess
from codecarbon import EmissionsTracker

output_dir = "metrics-after-codecarbon"
os.makedirs(output_dir, exist_ok=True)

print("Inicializando o CodeCarbon para monitorar os testes pós-refatoração...")

# Configura o rastreador para salvar os resultados na pasta correta
tracker = EmissionsTracker(
    output_dir=output_dir,
    output_file="emissions.csv",
    project_name="advanced_alchemy_after_refactor"
)

tracker.start()
try:
    print("Executando testes com pytest...")
    # Executa a suíte de testes do projeto
    subprocess.run(["pytest"], check=True)
finally:
    tracker.stop()

print(f"Métricas de emissão de carbono salvas com sucesso em: {output_dir}")
