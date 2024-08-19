import os
import random
import string

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def rename_images_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']:  # tambahkan ekstensi lain jika perlu
                random_name = generate_random_string() + ext
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, random_name)
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} to {new_path}")

# Ganti 'your_directory_path' dengan path direktori yang berisi file gambar
directory_path = 'your_directory_path'
rename_images_in_directory('./data')
