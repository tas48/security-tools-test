import subprocess

def run_nikto(target, output_file=None):
    try:
        command = ["nikto", "-h", target]
        if output_file:
            command += ["-output", output_file]
        
        # Executa o comando e captura a saída
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        print("[INFO] Scan do Nikto concluído.")
        print(result.stdout)
        
        if output_file:
            print(f"[INFO] Resultados salvos em: {output_file}")
    
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o Nikto: {e.stderr}")
    except FileNotFoundError:
        print("[ERRO] Nikto não está instalado ou não foi encontrado no PATH.")

# Executa um scan simples
target_url = "https://owasp.org/www-project-juice-shop/"
output_file = "nikto_results.txt"
run_nikto(target_url, output_file)
