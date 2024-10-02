import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def load_excel():
    """
    Opens a file dialog to load an Excel file into a pandas DataFrame.
    """
    try:
        root = tk.Tk()
        root.withdraw()

        # Open a file dialog and get the path of the selected Excel file
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls")])

        if file_path:
            # Load the Excel file into a DataFrame
            df = pd.read_excel(file_path)
            df.filepath = file_path  # Store the file path in the DataFrame
            print(f"Loaded {file_path}")
            return df
        else:
            print("No file selected.")
            return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def save_to_folder(df, filename="cleaned_data.xlsx"):
    """
    Opens a folder dialog to save the pandas DataFrame as an Excel file and returns the folder path.
    """
    try:
        root = tk.Tk()
        root.withdraw()

        # Ask user to select a folder
        folder_path = filedialog.askdirectory(title="Select Folder")

        if folder_path:
            # Save the file in the selected folder
            save_path = os.path.join(folder_path, filename)
            df.to_excel(save_path, index=False)
            print(f"File saved successfully at {save_path}")
            return save_path  # Return the path of the saved file
        else:
            print("Folder selection cancelled.")
            return None
    except Exception as e:
        print(f"Error saving file: {e}")
        return None
