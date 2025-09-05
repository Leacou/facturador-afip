import platform
import os
import zipfile
import urllib.request

# Detectar arquitectura
arch = platform.machine()
if arch == "arm64" or arch == "aarch64":
    chromedriver_url = "https://storage.googleapis.com/chrome-for-testing-public/138.0.7204.94/mac-arm64/chromedriver-mac-arm64.zip"
    zip_name = "chromedriver-mac-arm64.zip"
elif arch == "x86_64":
    chromedriver_url = "https://storage.googleapis.com/chrome-for-testing-public/138.0.7204.94/mac-x64/chromedriver-mac-x64.zip"
    zip_name = "chromedriver-mac-x64.zip"
else:
    raise Exception(f"No soportado: {arch}")

print(f"Descargando ChromeDriver para {arch} desde {chromedriver_url}")
urllib.request.urlretrieve(chromedriver_url, zip_name)

print("Descomprimiendo...")
with zipfile.ZipFile(zip_name, 'r') as zip_ref:
    zip_ref.extractall(".")

print("Hecho. Borrando ZIP...")
os.remove(zip_name)

print("Listo! Ahora tenés el ChromeDriver en la carpeta actual.")
