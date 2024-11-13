from PIL import Image
import pillow_avif  # This line is enough to register the AVIF plugin
import os
import shutil

input_folder = '/Users/joshua/Desktop/dataset_raw'
output_folder = '/Users/joshua/Desktop/dataset_nieuw'

# Clear and recreate output folder
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)
os.makedirs(output_folder)

for root, _, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.avif', '.webp')):
            input_path = os.path.join(root, file)
            try:
                with Image.open(input_path) as img:
                    # Preserve folder structure in output
                    relative_path = os.path.relpath(root, input_folder)
                    output_path = os.path.join(output_folder, relative_path)
                    os.makedirs(output_path, exist_ok=True)
                    
                    # Convert and save as JPG
                    output_file = os.path.splitext(file)[0] + '.jpg'
                    output_full_path = os.path.join(output_path, output_file)
                    img.convert("RGB").save(output_full_path, 'JPEG')
                    print(f"Converted and saved: {output_full_path}")
            except Exception as e:
                print(f"Error converting {input_path}: {str(e)}")
                print(f"Error type: {type(e).__name__}")
                import traceback
                traceback.print_exc()
        else:
            print(f"Skipping non-image file: {file}")

print("Conversion process completed.")
