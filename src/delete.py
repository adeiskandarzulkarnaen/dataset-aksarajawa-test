import os
import random

def delete_random_images(directory, delete_percentage=0.2):
    for root, dirs, files in os.walk(directory):
        image_files = [f for f in files if os.path.splitext(f)[1].lower() in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']]
        num_to_delete = int(len(image_files) * delete_percentage)
        
        images_to_delete = random.sample(image_files, num_to_delete)
        
        for image in images_to_delete:
            image_path = os.path.join(root, image)
            os.remove(image_path)
            print(f"Deleted: {image_path}")

# Ganti 'your_directory_path' dengan path direktori yang berisi file gambar
delete_random_images('./data')
