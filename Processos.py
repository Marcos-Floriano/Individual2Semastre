import time
import psutil
from datetime import datetime

# Lista para armazenar dados do uso de disco
uso_disco_data = []

# Lista para armazenar dados da distribuição de CPU por tipo de processo
distribuicao_cpu_data = []

# Tempo total de execução (em segundos)
tempo_total = 1

# Obtém a lista de processos no início
processos_iniciais = psutil.process_iter()

# Grava o tempo inicial
inicio = time.time()

# Loop para coletar dados ao longo do tempo
while time.time() - inicio < tempo_total:
    # Obtém informações sobre o uso do disco
    uso_disco = psutil.disk_usage('/')
    uso_disco_data.append((datetime.now(), uso_disco.percent))

    # Obtém informações sobre a distribuição de CPU por tipo de processo
    distribuicao_cpu = {}
    for processo in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        info = processo.info
        distribuicao_cpu[info['name']] = info['cpu_percent']
    distribuicao_cpu_data.append((datetime.now(), distribuicao_cpu))

    # Obtém informações sobre o uso de memória
    uso_memoria = psutil.virtual_memory().percent
    uso_memoria_data.append((datetime.now(), uso_memoria))

    # Aguarda 1 segundo antes de coletar novamente
    time.sleep(1)



# Imprime a utilização da CPU de cada processo
for processo in processos_iniciais:
    try:
        # Obtém as informações do processo
        info = processo.as_dict(attrs=['pid', 'name', 'cpu_percent'])
        info2 = processo.as_dict(attrs=['pid', 'name', 'io_counters'])

        # Imprime as informações do processo
        print(f"PID: {info['pid']}, Nome: {info['name']}, Utilização da CPU: {info['cpu_percent']}%")
        print(f"PID: {info2['pid']}, Nome: {info2['name']}, Utilização do Disco: {info2['io_counters'].write_bytes / (1024 * 1024)} MB")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
