import os
import shutil

""""

"""

def move_files_with_serial(serial, source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith(".html"):
            if serial in filename:
                source_path = os.path.join(source_folder, filename)
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(source_path, destination_path)
                print(f"Se movió el archivo {filename} a {destination_folder}")

def main():
    log_folder = 'Logfile'
    save_folder = 'saves'

    serial = input('Escanea el serial: ')

    move_files_with_serial(serial, log_folder, save_folder)

if __name__ == "__main__":
    main()
