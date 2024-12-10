from libnmap.process import NmapProcess
from libnmap.parser import NmapParser
import time

# Lista ampliada de opções para maximizar a coleta de informações
options_list = [
    "-sS -T4 --reason --open --version-intensity 5",  # Scan SYN com maior intensidade de versão
    "-sT -T4 --reason --version-all",               # Scan TCP Connect detalhado
    "-sU -sV --script=discovery --top-ports 200",   # Scan UDP com script de descoberta
    "-O --osscan-guess --fuzzy",                   # Detecção detalhada do sistema operacional
    "-A --script=vuln --traceroute",               # Detecção completa com vulnerabilidades
    "-sC -sV --script=default,auth",               # Scripts padrão e de autenticação
    "-p 1-65535 --open --script=service",          # Verifica todas as portas com script de serviço
    "--script=vuln --script-args=unsafe=1",        # Scripts de vulnerabilidade com opções agressivas
    "--top-ports 1000 --open",                     # Verifica as 1000 portas mais comuns
    "--traceroute --max-retries 1",                # Traceroute com menos tentativas
    "--version-all --script=all",                  # Detalha todas as versões e scripts disponíveis
    "-sS --min-rate 5000 --max-rate 10000",        # Ajusta a taxa de pacotes no scan SYN
    "-sU -sV --top-ports 50",                      # Scan UDP nas 50 portas mais usadas
    "--source-port 53 -Pn --dns-servers 8.8.8.8",  # Usa porta de origem 53 e ignora ping
]

# Alvo para teste
target = "scanme.nmap.org"

# Função para executar e processar os testes
def run_nmap_test(options, output_file):
    print(f"\n[INFO] Iniciando scan com as opções: {options}")
    print("[INFO] Alvo: ", target)
    
    nmap_proc = NmapProcess(targets=target, options=options)
    nmap_proc.run()

    if nmap_proc.rc != 0:
        print(f"[ERRO] Scan falhou com as opções: {options}. Verifique os detalhes no arquivo.")
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(f"\n[ERRO] Scan falhou com opções: {options}\n{nmap_proc.stderr}\n")
    else:
        report = NmapParser.parse(nmap_proc.stdout)
        with open(output_file, "a", encoding="utf-8") as file:
            file.write("\n========== RELATÓRIO ==========\n")
            file.write(f"Comando executado: {report.commandline}\n")
            file.write(f"Hora de início: {report.started}\n")
            file.write(f"Hora de término: {report.endtime}\n")
            file.write(f"Duração: {report.elapsed} segundos\n\n")

            for host in report.hosts:
                file.write(f"Endereço IP: {host.address}\n")
                file.write(f"Status: {host.status}\n")
                file.write(f"Hostname: {', '.join(host.hostnames) if host.hostnames else 'Não detectado'}\n")
                file.write(f"Sistema Operacional: {host.os_match_probabilities()[0].name if host.os_match_probabilities() else 'Não detectado'}\n")

                for service in host.services:
                    file.write(f"  Porta: {service.port}/{service.protocol}\n")
                    file.write(f"  Serviço: {service.service}\n")
                    file.write(f"  Estado: {service.state}\n")
                    file.write(f"  Versão: {service.banner}\n")
        print(f"[INFO] Scan concluído: {options}\nResultados salvos no arquivo.")

output_file = "nmap/nmap_teste3_detailed_results.txt"

with open(output_file, "w", encoding="utf-8") as file:
    file.write("Relatórios Detalhados de Scans Nmap\n")

for options in options_list:
    print("[INFO] Executando próximo scan...")
    run_nmap_test(options, output_file)
    print("[INFO] Aguardando 2 segundos antes do próximo teste...")
    time.sleep(2)  # Pausa maior para não sobrecarregar o sistema

print("[INFO] Todos os testes foram concluídos. Verifique os resultados em 'nmap_detailed_results.txt'.")
