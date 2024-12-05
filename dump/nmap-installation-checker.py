import subprocess

def is_nmap_installed():
    try:
        # Tenta executar o comando 'nmap -v' para verificar se o Nmap está instalado
        subprocess.run(['nmap', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True  # Se o comando funcionar, o Nmap está instalado
    except subprocess.CalledProcessError:
        return False  # Se o comando falhar, o Nmap não está instalado
    except FileNotFoundError:
        return False  # Caso o comando 'nmap' não seja encontrado no PATH

# Testando a função
if is_nmap_installed():
    print("O Nmap está instalado!")
else:
    print("O Nmap não está instalado.")
