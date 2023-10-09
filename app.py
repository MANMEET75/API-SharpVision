import cv2
import pandas as pd
import numpy as np

import io
import pandas as pd
import numpy as np
from PIL import Image
from fastapi import FastAPI, UploadFile
from typing import Optional

def is_blurred(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return False  # Unable to read the image

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the Laplacian variance as a measure of blurriness
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    # You can adjust this threshold value based on your requirements
    threshold = 550  # Adjust this value as needed

    return laplacian_var < threshold
def get_image_from_bytes(binary_image: bytes) -> Image:
    """Convert image from bytes to PIL RGB format
    
    Args:
        binary_image (bytes): The binary representation of the image
    
    Returns:
        PIL.Image: The image in PIL RGB format
    """
    input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")
    return input_image


def get_bytes_from_image(image: Image) -> bytes:
    """
    Convert PIL image to Bytes
    
    Args:
    image (Image): A PIL image instance
    
    Returns:
    bytes : BytesIO object that contains the image in JPEG format with quality 85
    """
    return_image = io.BytesIO()
    image.save(return_image, format='JPEG', quality=85)  # save the image in JPEG format with quality 85
    return_image.seek(0)  # set the pointer to the beginning of the file
    return return_image