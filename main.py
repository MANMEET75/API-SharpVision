####################################### IMPORT #################################
import json
import sys
import uvicorn
from io import BytesIO
from app import *
import pandas as pd
from PIL import Image
from fastapi import FastAPI, UploadFile

from fastapi import FastAPI, File, status
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse, StreamingResponse
from loguru import logger

from app import get_image_from_bytes

app = FastAPI(
    title="SharpVision: Image Clarity Analyzer Using Computer Vision",
    version="2023.1.31",
)



@app.get("/", include_in_schema=False)
async def redirect():
    return RedirectResponse("/docs")

@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    """Perform a healthcheck and return a response."""
    return {'healthcheck': 'Everything OK!'}



@app.post("/identify_blur_image")
async def check_blur(file: UploadFile):
    # Create a temporary file to save the uploaded image
    with open("temp_image.jpg", "wb") as temp_image:
        temp_image.write(file.file.read())

    # Check if the uploaded image is blurred
    is_blurred_image = is_blurred("temp_image.jpg")

    # Remove the temporary image file
    import os
    os.remove("temp_image.jpg")

    if is_blurred_image:
        return JSONResponse(content={"message": "Image is blurred"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Image is not blurred"}, status_code=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)