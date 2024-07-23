import os
import shutil
from PIL import Image
import re


def convert_to_webp(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, 'webp')


def replace_references(file_path, old_filename, new_filename, assets_path):
    with open(file_path, 'r') as file:
        content = file.read()

    pattern = re.compile(r'(assets/.*?)' + re.escape(old_filename))
    new_content = pattern.sub(r'\1' + new_filename, content)

    if new_content != content:
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"Updated references in: {file_path}")


def scan_and_convert(root_folder, replace_refs, backup_originals):
    backup_folder = os.path.join(root_folder, 'original_images_backup')
    if backup_originals:
        os.makedirs(backup_folder, exist_ok=True)

    assets_path = None
    for root, dirs, files in os.walk(root_folder):
        if 'assets' in dirs:
            assets_path = os.path.join(root, 'assets')
            break

    if not assets_path:
        print("Warning: 'assets' folder not found. Reference replacement may not work as expected.")

    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(foldername, filename)
                output_filename = os.path.splitext(filename)[0] + '.webp'
                output_path = os.path.join(foldername, output_filename)

                try:
                    convert_to_webp(input_path, output_path)
                    print(f"Converted: {input_path} -> {output_path}")

                    if replace_refs and assets_path:
                        for root, _, files in os.walk(root_folder):
                            for file in files:
                                if file.endswith(('.html', '.js', '.jsx', '.ts', '.tsx', '.twig')):
                                    replace_references(os.path.join(root, file), filename, output_filename, assets_path)

                    if backup_originals:
                        relative_path = os.path.relpath(foldername, root_folder)
                        backup_path = os.path.join(backup_folder, relative_path)
                        os.makedirs(backup_path, exist_ok=True)
                        shutil.move(input_path, os.path.join(backup_path, filename))
                        print(f"Moved original to backup: {input_path}")

                except Exception as e:
                    print(f"Error converting {input_path}: {str(e)}")


if __name__ == "__main__":
    root_folder = input("Enter the full path of the folder to start scanning: ")
    if os.path.isdir(root_folder):
        replace_refs = input(
            "Do you want to replace references in HTML, JS, JSX, TS, TSX, and Twig files? (y/n): ").lower() == 'y'
        backup_originals = input("Do you want to move original images to a backup folder? (y/n): ").lower() == 'y'
        scan_and_convert(root_folder, replace_refs, backup_originals)
    else:
        print("Invalid directory path. Please enter a valid directory path.")
