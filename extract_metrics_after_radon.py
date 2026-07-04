import os
import subprocess

output_dir = "metrics-after-radon"
os.makedirs(output_dir, exist_ok=True)

cc_file = os.path.join(output_dir, "radon_cc.json")
hal_file = os.path.join(output_dir, "radon_hal.json")

print("Executando Radon (Complexidade Ciclomática e Halstead)...")

# Extrai complexidade ciclomática em formato JSON
with open(cc_file, "w", encoding="utf-8") as f:
    subprocess.run(["radon", "cc", "advanced_alchemy", "-j"], stdout=f)

# Extrai métricas de Halstead em formato JSON
with open(hal_file, "w", encoding="utf-8") as f:
    subprocess.run(["radon", "hal", "advanced_alchemy", "-j"], stdout=f)

print(f"Métricas do Radon salvas com sucesso em: {output_dir}")
