from libnmap.process import NmapProcess
from libnmap.parser import NmapParser

# Configura o alvo e os parâmetros de varredura
target = "scanme.nmap.org"  # Substitua pelo IP ou domínio desejado
options = "-sV -O"  # Varredura de serviços e detecção de SO

try:
    # Inicia o processo do Nmap
    nmap_proc = NmapProcess(targets=target, options=options)
    nmap_proc.run()

    # Verifica se o Nmap executou com sucesso
    if nmap_proc.rc != 0:
        print(f"Erro ao executar o Nmap: {nmap_proc.stderr}")
        exit()

    # Analisa os resultados
    report = NmapParser.parse(nmap_proc.stdout)

    # Exibe as informações gerais do relatório
    print("========== RELATÓRIO NMAP ==========")
    print(f"Alvo: {target}")
    print(f"Comando executado: {report.commandline}")
    print(f"Hora de início: {report.started}")
    print(f"Hora de término: {report.endtime}")
    print(f"Duração: {report.elapsed} segundos\n")

    # Itera pelos hosts no relatório
    for host in report.hosts:
        print("========== HOST ==========")
        print(f"Endereço IP: {host.address}")
        print(f"Status: {host.status}")
        print(f"Hostname: {', '.join(host.hostnames) if host.hostnames else 'Não detectado'}")
        print(f"Sistema Operacional: {host.os_match_probabilities()[0].name if host.os_match_probabilities() else 'Não detectado'}")
        
        # Lista portas e serviços
        print("\n=== Portas e Serviços ===")
        for service in host.services:
            print(f"  Porta: {service.port}/{service.protocol}")
            print(f"  Serviço: {service.service}")
            print(f"  Estado: {service.state}")
            print(f"  Versão: {service.banner}\n")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
