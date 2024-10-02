import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd
from file_handling import load_excel, save_to_folder
from data_cleaning import clean_data  # Import the new clean_data function
from calculations import add_calculations


class DataProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRM Data Cleaner")
        self.root.geometry("550x300")
        self.root.resizable(False, False)  # Prevent window resizing

        # Create GUI components
        self.create_widgets()

        self.df = None  # Placeholder for DataFrame

    def create_widgets(self):
        # Header Label
        header_label = tk.Label(self.root, text="CRM Data Cleaner", font=("Arial", 16, "bold"))
        header_label.grid(row=0, column=0, columnspan=2, pady=20)

        # File selection label and button
        select_file_label = tk.Label(self.root, text="Select an Excel file to process:", font=("Arial", 12))
        select_file_label.grid(row=1, column=0, sticky="w", padx=20)

        self.file_path_label = tk.Label(self.root, text="No file selected", font=("Arial", 10), fg="gray", wraplength=400)
        self.file_path_label.grid(row=2, column=0, sticky="w", padx=20)

        select_button = tk.Button(self.root, text="Select File", width=15, command=self.load_file)
        select_button.grid(row=2, column=1, padx=20, pady=5)

        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=450, mode='determinate')
        self.progress.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

        # Status label
        self.status_label = tk.Label(self.root, text="Awaiting action...", font=("Arial", 10), wraplength=400)
        self.status_label.grid(row=4, column=0, columnspan=2, padx=20)

        # Process button
        self.process_button = tk.Button(self.root, text="Process Data", width=15, command=self.process_data, state=tk.DISABLED)
        self.process_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Output folder label
        self.output_folder_label = tk.Label(self.root, text="", font=("Arial", 10), wraplength=450)
        self.output_folder_label.grid(row=6, column=0, columnspan=2, padx=20)

    def load_file(self):
        # Load file using the function from file_handling.py
        self.df = load_excel()
        if self.df is not None:
            self.file_path_label.config(text=f"File loaded: {self.df.filepath}")  # Update the label with file path
            self.process_button.config(state=tk.NORMAL)
            messagebox.showinfo("File Loaded", "File loaded successfully!")
        else:
            messagebox.showwarning("No File", "Please select a valid file.")

    def process_data(self):
        if self.df is not None:
            # Step 1: Start the progress bar and update the status
            self.progress['value'] = 0
            self.status_label.config(text="Step 1: Dropping row 0")
            self.root.update_idletasks()

            # Step 1: Clean the data (both column dropping and whitespace cleaning)
            self.df = clean_data(self.df)
            self.progress['value'] += 50
            self.status_label.config(text="Step 2: Cleaning whitespace and dropping columns")
            self.root.update_idletasks()

            # Step 2: Perform calculations
            self.df = add_calculations(self.df)
            self.progress['value'] += 25
            self.status_label.config(text="Step 3: Performing calculations")
            self.root.update_idletasks()

            # Step 3: Save the file
            self.save_file()

    def save_file(self):
        # Call save_to_folder and get the folder path
        output_path = save_to_folder(self.df)
        if output_path:
            self.output_folder_label.config(text=f"File saved in: {output_path}")
            self.progress['value'] = 100
            self.status_label.config(text="Document cleaned and saved!")
            self.show_success_window()

    def show_success_window(self):
        # Create a new top-level window
        success_window = tk.Toplevel(self.root)
        success_window.title("Success")
        success_window.geometry("300x150")
        success_window.resizable(False, False)

        # Success message label
        success_label = tk.Label(success_window, text="Document cleaned and saved!", font=("Arial", 12))
        success_label.pack(pady=20)

        # Button to close the application
        close_button = tk.Button(success_window, text="Close Program", width=15, command=self.close_program)
        close_button.pack(pady=10)

    def close_program(self):
        self.root.quit()  # Exit the application


def main():
    # Create the main window
    root = tk.Tk()
    app = DataProcessorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
