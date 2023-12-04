import os
import re
def get_serials(archivos):
    seriales = set()
    for archivo in archivos:
        match = re.search(r'\[([^\]]+)\]', archivo)
        if match:
            serial = match.group(1)
            seriales.add(serial)
    return seriales

def main():
    directorio = 'Logfile'  # Reemplaza esto con la ruta de tu directorio
    archivos = os.listdir(directorio)

    seriales_unicos = get_serials(archivos)
    
    print(f'Total de archivos: {len(archivos)}')
    print(f'Total de piezas únicas probadas: {len(seriales_unicos)}')

if __name__ == "__main__":
    main()