import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = ['pywhatkit']

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Instalando {package}...")
        install(package)

import pywhatkit as kit

num = int(input('Digite o número com (ddd): ').strip())
msg = input('Digite sua mensagem: ').strip()
hora = input('Digite o horário do envio da mensagem no formato 00:00:').split(':')

def enviar_msg(): 
    try:
        kit.sendwhatmsg(f'+55{num}', f'{msg}', int(hora[0]), int(hora[1]))
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")

enviar_msg()
