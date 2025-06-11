import numpy as np
import rasterio
from PIL import Image
import os


def readRGBBands(filePath, rgbIndices=(2, 1, 0)):
    """
    Read specific RGB bands from a multi-band GeoTIFF file.

    Args:
        filePath (str): Path to the GeoTIFF image.
        rgbIndices (tuple): Band indices for RGB (0-based).

    Returns:
        np.ndarray: Float32 RGB image array of shape (H, W, 3).
    """
    with rasterio.open(filePath) as dataset:
        selectedBands = [dataset.read(i + 1).astype(np.float32) for i in rgbIndices]
        rgbArray = np.stack(selectedBands, axis=-1)
    return rgbArray


def normalizeToUint8(array):
    """
    Normalize a float32 image to the 0–255 uint8 range.

    Args:
        array (np.ndarray): Input image array.

    Returns:
        np.ndarray: Normalized uint8 image.
    """
    minVal, maxVal = array.min(), array.max()
    normalized = (array - minVal) / (maxVal - minVal + 1e-8)
    return (normalized * 255).astype(np.uint8)


def generateRGBImage(tifFile):
    """
    Process a GeoTIFF into an RGB image.

    Args:
        tifFile (str): Path to the .tif file.

    Returns:
        np.ndarray: RGB image (uint8).
    """
    floatImage = readRGBBands(tifFile)
    return normalizeToUint8(floatImage)


def saveAsImage(npImage, savePath):
    """
    Save a numpy array as a PNG image.

    Args:
        npImage (np.ndarray): Image data.
        savePath (str): Output file path.
    """
    image = Image.fromarray(npImage)
    image.save(savePath)


if __name__ == "__main__":
    tifInput = r"D:\Desktop\2019_1101_nofire_B2348_B12_10m_roi.tif"
    pngOutput = r"D:\Desktop\converted_rgb_output.png"

    if not os.path.isfile(tifInput):
        print("Error: Input TIFF file not found. Check the path.")
    else:
        try:
            rgbImage = generateRGBImage(tifInput)
            saveAsImage(rgbImage, pngOutput)
            print(f"✔ RGB image saved successfully: {pngOutput}")
        except Exception as err:
            print(f"❌ Failed to process the TIFF image. Reason: {err}")
