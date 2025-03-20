# Image Metadata Extractor

## Program Description

* **Functionality:** Performs monkey testing on a website.
* **Programmer:** Suman Gangopadhyay
* **Email ID:** linuxgurusuman@gmail.com
* **Date:** 25-Feb-2025
* **Version:** 1.0
* **Code Library:** Selenium
* **Prerequisites:** Python, Pillow
* **Caveats:** None

## Overview
The **SumanImageMetadataExtractor** is a Python-based tool for extracting and processing EXIF metadata from JPEG images. It specifically extracts GPS coordinates if available and converts them from Degrees, Minutes, and Seconds (DMS) to decimal degrees.

## Features
- Extracts EXIF metadata from images.
- Processes GPS data to obtain latitude and longitude.
- Displays GPS coordinates in decimal format.
- Handles multiple images within a directory.
- Provides error handling for invalid images or missing metadata.

## Prerequisites
Ensure you have Python installed (version 3.6 or higher).

### Required Python Packages:
- **Pillow**: For image processing.

You can install Pillow using:
```bash
pip install Pillow
```

## Usage
1. Clone this repository or copy the script.
2. Ensure the script is executable:
    ```bash
    chmod +x script.py
    ```
3. Run the script by providing the folder path containing your images:
    ```bash
    python script.py /path/to/your/image/folder
    ```

## Example Output
```
Photo: example.jpg
GPS Coordinates: 37.7749, -122.4194
```

If no GPS data is found:
```
Photo: example.jpg
No GPS data found.
```

## Code Structure
- **SumanImageMetadataExtractor**: Main class to handle metadata extraction.
- **get_exif_data**: Extracts and decodes EXIF data.
- **dms_to_decimal**: Converts DMS coordinates to decimal format.
- **process_images**: Processes all JPEG images in the provided folder and prints the results.

## Error Handling
- If the specified path is not a directory, an error message is displayed.
- Incomplete or corrupted EXIF data will result in an appropriate error message.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

