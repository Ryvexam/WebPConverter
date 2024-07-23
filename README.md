# 🖼️ Image Converter to WebP

This project converts `.jpg`, `.jpeg`, and `.png` images to `.webp` format within a specified directory and its subdirectories.

## 📦 Installation

To install this project, follow these steps:

1. **Clone the repository**
    ```bash
    git clone https://github.com/Ryvexam/WebPConverter
    ```
2. **Navigate to the project directory**
    ```bash
    cd WebPConverter
    ```
3. **Install the required dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

To use this project, follow these steps:

1. **Run the script**
    ```bash
    python main.py
    ```

2. **Enter the full path of the folder to start scanning when prompted**

## 🛠️ How It Works

1. The script scans the specified root folder and all its subfolders for images with `.jpg`, `.jpeg`, and `.png` extensions.
2. For each found image, it converts the image to `.webp` format using the `PIL` library.
3. The converted images are saved in the same directory as the original images with the same name but a `.webp` extension.
4. The script prints out the conversion status of each image.

## ⚠️ Error Handling

If an image cannot be converted, the script will print an error message indicating the issue with the specific image file.

## 📂 Example Folder Structure

```
root_folder/
├── image1.jpg
├── image2.png
├── subfolder/
│   ├── image3.jpeg
│   └── image4.jpg
```

After running the script:

```
root_folder/
├── image1.jpg
├── image1.webp
├── image2.png
├── image2.webp
├── subfolder/
│   ├── image3.jpeg
│   ├── image3.webp
│   ├── image4.jpg
│   └── image4.webp
```

## 📜 License

This project is licensed under the MIT License.

---

Feel free to contribute to this project by opening issues or submitting pull requests.

Happy Converting! 🎉
