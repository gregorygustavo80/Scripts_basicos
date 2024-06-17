import sys
import subprocess
import pkg_resources

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = ['opencv-python', 'mediapipe', 'pyautogui', 'pycaw', 'comtypes'] 

installed_packages = {pkg.key for pkg in pkg_resources.working_set}
for package in required_packages:
    if package not in installed_packages:
        print(f"Instalando {package}...")
        install(package)

        