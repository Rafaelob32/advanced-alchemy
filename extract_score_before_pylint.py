import subprocess
import os

# Configuração
PROJETO = "./advanced_alchemy" # diretório do código fonte ajustado para o projeto atual
PASTA   = "metrics-before-pylint"

os.makedirs(PASTA, exist_ok=True)

resultado = subprocess.run(
    ["pylint", PROJETO, "--score=y"],
    capture_output=True,
    text=True,
    encoding="utf-8",
)

caminho_score = os.path.join(PASTA, "pylint_score_antes.txt")
with open(caminho_score, "w", encoding="utf-8") as f:
    for linha in resultado.stdout.splitlines():
        if "Your code has been rated at" in linha:
            f.write(linha + "\n")
            print(linha)

print(f"Score salvo em: {caminho_score}")
