import time
import psutil

processos = psutil.process_iter()

# Grava o tempo inicial
inicio = time.time()

# Trecho de código a ser medido
for i in range(10):
    print("Covil do Dev")

# Grava o tempo final
fim = time.time()

# Calcula o tempo total decorrido
tempo_total = fim - inicio

print(f"Tempo de execução: {tempo_total} segundos")

# Imprime a utilização da CPU de cada processo
for processo in processos:
    try:
        # Obtém as informações do processo
        info = processo.as_dict(attrs=['pid', 'name', 'cpu_percent'])
        info2 = processo.as_dict(attrs=['pid', 'name', 'io_counters'])

        # Imprime as informações do processo
        print(f"PID: {info['pid']}, Nome: {info['name']}, Utilização da CPU: {info['cpu_percent']}%")
        print(f"PID: {info2['pid']}, Nome: {info2['name']}, Utilização do Disco: {info2['io_counters'].write_bytes / (1024 * 1024)} MB")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
