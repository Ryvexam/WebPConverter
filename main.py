import os
from PIL import Image


def convert_to_webp(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, 'webp')


def scan_and_convert(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(foldername, filename)
                output_filename = os.path.splitext(filename)[0] + '.webp'
                output_path = os.path.join(foldername, output_filename)

                try:
                    convert_to_webp(input_path, output_path)
                    print(f"Converted: {input_path} -> {output_path}")
                except Exception as e:
                    print(f"Error converting {input_path}: {str(e)}")


if __name__ == "__main__":
    root_folder = input("Enter the full path of the folder to start scanning: ")
    if os.path.isdir(root_folder):
        scan_and_convert(root_folder)
    else:
        print("Invalid directory path. Please enter a valid directory path.")
