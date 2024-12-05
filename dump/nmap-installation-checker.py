import subprocess

def is_nmap_installed():
    try:
        subprocess.run(['nmap', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True 
    except subprocess.CalledProcessError:
        return False  
    except FileNotFoundError:
        return False  

if is_nmap_installed():
    print("O Nmap is installed")
else:
    print("O Nmap is not istalled")
