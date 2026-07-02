from codecarbon import EmissionsTracker
import subprocess
import sys
import os

# ==============================================================================
# CONFIGURAÇÃO ADAPTADA PARA ADVANCED-ALCHEMY (EVITANDO SHADOWING)
# ==============================================================================

# Nome do projeto
PROJETO  = "advanced-alchemy"

# Ponto de entrada ajustado para modo Módulo (impede o conflito com a stdlib)
SCRIPT   = "advanced_alchemy.cli"

# Argumentos necessários para a execução do projeto.
# Como queremos apenas testar a execução, passamos '--help' para que ele encerre sozinho.
ARGS     = ["--help"]

# Tempo máximo que o CodeCarbon vai aguardar a execução do projeto.
# None -> sem limite — o CodeCarbon aguarda o projeto terminar sozinho.
TIMEOUT  = None

# Não altere o nome dessa pasta, os relatórios vão ser salvos nela.
PASTA    = "metrics-before-codecarbon"

# ==============================================================================

# Executa com medição 
os.makedirs(PASTA, exist_ok=True)

tracker = EmissionsTracker(
    project_name=PROJETO,
    measure_power_secs=1,
    output_dir=PASTA,
    output_file="emissions_antes.csv",
    allow_multiple_runs=True,
    log_level="error",
)

print(f"Iniciando medição de emissões para: {PROJETO}")
print(f"Comando: python -m {SCRIPT} {' '.join(ARGS)}")
if TIMEOUT:
    print(f"Timeout: {TIMEOUT} segundos")

tracker.start()

try:
    # Ajustado para executar usando 'python -m advanced_alchemy.cli'
    resultado = subprocess.run(
        [sys.executable, "-m", SCRIPT] + ARGS,
        timeout=TIMEOUT
    )
    exit_code = resultado.returncode
except subprocess.TimeoutExpired:
    print("Tempo de medição encerrado.")
    exit_code = 0

emissions = tracker.stop()

print(f"\nResultados:")
print(f"  Exit code:         {exit_code}")
if emissions is not None:
    print(f"  CO₂ emitido:       {emissions * 1000:.6f} g CO₂")
else:
    print(f"  CO₂ emitido:       Não foi possível calcular (tempo muito curto).")
print(f"  Arquivo salvo em:  {os.path.join(PASTA, 'emissions_antes.csv')}")
print("\nConcluído.")
