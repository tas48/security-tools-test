from libnmap.process import NmapProcess
from libnmap.parser import NmapParser
import time

# Lista de algumas opções comuns para testar
options_list = [
    "-sS",               # Scan SYN
    "-sT",               # Scan TCP Connect
    "-sU",               # Scan UDP
    "-sV",               # Detecta versão dos serviços
    "-O",                # Detecta o sistema operacional
    "-A",                # Detecção completa: OS, versões, scripts, traceroute
    "-sC",               # Executa scripts padrão
    "-p 80,443",         # Verifica as portas 80 e 443
    "-p 1-1024",         # Verifica portas 1-1024
    "--script=vuln",     # Executa scripts relacionados a vulnerabilidades
    "--open",            # Exibe apenas as portas abertas
    "--traceroute",      # Executa um traceroute
    "--version-all",     # Exibe informações detalhadas sobre as versões de todos os serviços
    "--max-retries 2",   # Define o número de tentativas
    "--source-port 53",  # Define uma porta de origem
]

# Alvo para teste
target = "scanme.nmap.org"

# Função para executar e processar os testes
def run_nmap_test(options):
    print(f"\nExecutando Nmap com opções: {options}")
    nmap_proc = NmapProcess(targets=target, options=options)
    nmap_proc.run()

    if nmap_proc.rc != 0:
        print(f"Erro ao executar o Nmap: {nmap_proc.stderr}")
    else:
        # Analisa os resultados
        report = NmapParser.parse(nmap_proc.stdout)
        print("========== RELATÓRIO ==========")
        print(f"Comando executado: {report.commandline}")
        print(f"Hora de início: {report.started}")
        print(f"Hora de término: {report.endtime}")
        print(f"Duração: {report.elapsed} segundos\n")

        # Itera pelos hosts no relatório
        for host in report.hosts:
            print(f"Endereço IP: {host.address}")
            print(f"Status: {host.status}")
            print(f"Hostname: {', '.join(host.hostnames) if host.hostnames else 'Não detectado'}")
            print(f"Sistema Operacional: {host.os_match_probabilities()[0].name if host.os_match_probabilities() else 'Não detectado'}")

            # Lista de serviços encontrados
            for service in host.services:
                print(f"  Porta: {service.port}/{service.protocol}")
                print(f"  Serviço: {service.service}")
                print(f"  Estado: {service.state}")
                print(f"  Versão: {service.banner}\n")

# Executar todos os testes de opções
for options in options_list:
    run_nmap_test(options)
    time.sleep(2)  # Pausa para não sobrecarregar o sistema

print("Testes de Nmap concluídos.")
