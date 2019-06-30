from typing import *
import csv
import os

DATA_FOLDER_NAME = "data"

def write_to_csv(data: List[List[Any]], filename: str) -> None:
    """Writes the given data to a csv file

    Args:
        data: the contents of the csv file to be created. data[0] will act as the
            labels for the csv file.
        filename: the name of the csv file to create

    Returns:
        None
    """
    if data:
        with open(get_path(filename), "w") as csv_file:
            writer = csv.writer(csv_file)
            for row in data:
                writer.writerow(row)

        csv_file.close()

def get_path(filename) -> str:
    return os.path.join("..", DATA_FOLDER_NAME, filename)