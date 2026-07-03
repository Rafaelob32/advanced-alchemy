from codecarbon import EmissionsTracker
import subprocess
import sys
import os

# ConfiguraÃ§Ã£o

PROJETO = "advanced-alchemy"
SCRIPT = "-m"
ARGS = [
    "pytest",
    "tests/unit/test_utils",
    "--ignore=tests/unit/test_utils/test_serialization.py",
    "--ignore=tests/unit/test_utils/test_fixtures.py",
]
TIMEOUT = None

# NÃ£o altere o nome dessa pasta, os relatÃ³rios vÃ£o ser salvos nela.
PASTA    = "metrics-before-codecarbon"

# Executa com mediÃ§Ã£o 
os.makedirs(PASTA, exist_ok=True)

tracker = EmissionsTracker(
    project_name=PROJETO,
    measure_power_secs=1,
    output_dir=PASTA,
    output_file="emissions_antes.csv",
    allow_multiple_runs=True,
    log_level="error",
)

print(f"Iniciando mediÃ§Ã£o de emissÃµes para: {PROJETO}")
print(f"Comando: python {SCRIPT} {' '.join(ARGS)}")
if TIMEOUT:
    print(f"Timeout: {TIMEOUT} segundos")

tracker.start()

try:
    resultado = subprocess.run(
        [sys.executable, SCRIPT] + ARGS,
        timeout=TIMEOUT
    )
    exit_code = resultado.returncode
except subprocess.TimeoutExpired:
    print("Tempo de mediÃ§Ã£o encerrado.")
    exit_code = 0

emissions = tracker.stop()

print(f"\nResultados:")
print(f"  Exit code:         {exit_code}")
print(f"  COâ‚‚ emitido:       {emissions * 1000:.6f} g COâ‚‚")
print(f"  Arquivo salvo em:  {os.path.join(PASTA, 'emissions.csv')}")
print("\nConcluÃ­do.")