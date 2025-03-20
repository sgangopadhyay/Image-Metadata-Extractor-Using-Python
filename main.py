import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

class SumanImageMetadataExtractor:
    """
    A class to extract and process EXIF metadata from images.
    """

    def __init__(self, folder_path):
       
        self.folder_path = folder_path

    def get_exif_data(self, image):
        """
        Extract EXIF data from an image and return it as a dictionary.
        GPSInfo is decoded separately using GPSTAGS.

        :param image: PIL Image object.
        :return: Dictionary containing EXIF data.
        """
        exif_data = {}
        info = image._getexif() 
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)  
                if decoded == 'GPSInfo':
                    gps_data = {}
                    for gps_tag in value:
                        sub_decoded = GPSTAGS.get(gps_tag, gps_tag)  
                        gps_data[sub_decoded] = value[gps_tag]
                    exif_data[decoded] = gps_data
                else:
                    exif_data[decoded] = value
        return exif_data

    def dms_to_decimal(self, dms, ref):
        """
        Convert GPS coordinates from Degrees, Minutes, Seconds (DMS) to decimal degrees.

        :param dms: Tuple of (degrees, minutes, seconds), each as (numerator, denominator)
        :param ref: Reference direction ('N', 'S', 'E', 'W')
        :return: Decimal degrees as a float.
        """
        degrees = dms[0][0] / dms[0][1]
        minutes = dms[1][0] / dms[1][1]
        seconds = dms[2][0] / dms[2][1]
        decimal = degrees + minutes / 60 + seconds / 3600
        if ref in ['S', 'W']:
            decimal = -decimal 
        return decimal

    def process_images(self):
        """
        Process all JPEG images in the folder to extract and print GPS coordinates.
        """
        
        if not os.path.isdir(self.folder_path):
            print("The provided path is not a directory.")
            sys.exit(1)

        
        image_files = [f for f in os.listdir(self.folder_path) if f.lower().endswith(('.jpg', '.jpeg'))]

        # Process each image file
        for image_file in image_files:
            try:
                full_path = os.path.join(self.folder_path, image_file)
                with Image.open(full_path) as img:
                    exif_data = self.get_exif_data(img)
                    print(f"Photo: {image_file}")
                    if 'GPSInfo' in exif_data:
                        gps_data = exif_data['GPSInfo']
                        # Check if all required GPS keys are present
                        required_keys = ['GPSLatitude', 'GPSLatitudeRef', 'GPSLongitude', 'GPSLongitudeRef']
                        if all(key in gps_data for key in required_keys):
                            lat = self.dms_to_decimal(gps_data['GPSLatitude'], gps_data['GPSLatitudeRef'])
                            lon = self.dms_to_decimal(gps_data['GPSLongitude'], gps_data['GPSLongitudeRef'])
                            print(f"GPS Coordinates: {lat}, {lon}")
                        else:
                            print("Incomplete GPS data.")
                    else:
                        print("No GPS data found.")
            except Exception as e:
                print(f"Error processing {image_file}: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Please provide the folder path.")
        print("Usage: python script.py /path/to/folder")
        sys.exit(1)

    folder_path = sys.argv[1]
    extractor = SumanImageMetadataExtractor(folder_path)
    extractor.process_images()
