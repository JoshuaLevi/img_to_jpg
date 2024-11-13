
# Image to JPG Converter

A Python script that converts various image formats (including AVIF, WebP, PNG, etc.) to JPG format while preserving the folder structure of the input images. This is useful for batch processing and converting images to a more widely compatible JPG format.

## Features

- Converts multiple image formats to JPG, including:
  - AVIF
  - WebP
  - PNG
  - JPG
  - JPEG
  - TIFF
  - BMP
  - GIF
- Preserves the original folder structure in the output directory
- Handles errors gracefully with detailed error reporting for easier debugging
- Automatically creates and cleans the output directory to avoid file conflicts

## Requirements

- Python 3.x
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)
- [pillow-avif](https://github.com/TadashiMizukami/pillow-avif-plugin) (for AVIF support)

Install the required packages using pip:
```bash
pip install Pillow pillow-avif
```

## Usage

1. Create an `input_folder` directory in the same location as the script.
2. Place your images in the `input_folder` (you can include subfolders).
3. Run the script:
   ```bash
   python img_to_jpg.py
   ```

The script will:
- Create an `output_folder` (or clean it if it already exists)
- Convert all supported images to JPG format
- Maintain the same folder structure as the input
- Print progress and any errors encountered during the conversion process

## Output

- Converted images will be saved in the `output_folder`.
- All images will be converted to JPG format with a `.jpg` extension.
- The original folder structure from `input_folder` will be preserved.
- Non-image files will be skipped with a notification.

## Error Handling

The script includes error handling that will:
- Print detailed error messages for any failed conversions, including the error type and traceback.
- Continue processing remaining images even if some conversions fail.
- Display the full error traceback for debugging purposes if an error occurs.

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to open issues or submit pull requests on GitHub if you would like to contribute to improving this script.
