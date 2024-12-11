import subprocess
import os

#erro de libs, resolver depois
def run_webmap_scan(target, output_path="output"):
    webmap_path = "tools/WebMap"
    os.chdir(webmap_path)
    
    command = [
        "python3", "webmap.py", "-h"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("[INFO] WebMap executado com sucesso!")
        print(result.stdout)  
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("[ERRO] Falha ao executar o WebMap")
        print(e.stderr)
        return None
    finally:

        os.chdir("../../")

# Executar um teste de scan
output = run_webmap_scan("https://owasp.org/www-project-juice-shop/")
if output:
    print("Scan concluído. Veja os detalhes no console acima.")
