from typing import *
import csv
import os

DATA_FOLDER_NAME = "data"

def get_path(filename: str) -> str:
    """Produces a file path used in write operations
    
    Args:
        filename: the name of the file to save data to, does not need to
        already exist in the file system.
    
    Returns:
        a string in the format "../DATA_FOLDER_NAME/<filename>"
    """
    return os.path.join("..", DATA_FOLDER_NAME, filename)
