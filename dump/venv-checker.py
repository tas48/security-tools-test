import os

def check_venv():
    if 'VIRTUAL_ENV' in os.environ:
        print("O ambiente virtual (venv) está ativo.")
    else:
        print("O ambiente virtual (venv) não está ativo.")

check_venv()
