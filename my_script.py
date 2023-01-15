__author__ = "Jack Qicheng Geng"

import soundfile as sf
import scipy.signal
import numpy as np
import tkinter as tk
from tkinter import filedialog
from cx_Freeze import setup, Executable

def apply_filter():
    # Get the input file
    file_path = filedialog.askopenfilename()

    # Get the center frequency and bandwidth from the input fields
    center_frequency = float(center_frequency_entry.get())
    bandwidth = float(bandwidth_entry.get())

    # Read the audio file
    data, sr = sf.read(file_path)

    # Define the notch filter parameters
    center_frequency = center_frequency # Hz
    bandwidth = bandwidth # Hz

    # Create the notch filter
    b, a = scipy.signal.iirnotch(center_frequency, bandwidth, sr)

    # Apply the filter to the audio data
    filtered_data = scipy.signal.lfilter(b, a, data)

    # Write the filtered data to a new file
    sf.write('filtered_file.wav', filtered_data, sr)
    label_result.config(text='File filtered successfully')

# Create the main window
root = tk.Tk()
root.title("Notch Filter")

# Create input fields for center frequency and bandwidth
center_frequency_label = tk.Label(root, text="Center frequency (Hz)")
center_frequency_label.pack()
center_frequency_entry = tk.Entry(root)
center_frequency_entry.pack()

bandwidth_label = tk.Label(root, text="Bandwidth (Hz)")
bandwidth_label.pack()
bandwidth_entry = tk.Entry(root)
bandwidth_entry.pack()

# Create a button to apply the filter
apply_filter_button = tk.Button(root, text="Apply Filter", command=apply_filter)
apply_filter_button.pack()

# Create a label to show the result
label_result = tk.Label(root, text="")
label_result.pack()

# Run the GUI
root.mainloop()

# Set up for exe info
setup(
    name = "Tonal Tinnitus Therapy Filter",
    version = "0.1",
    options = {"build_exe": {"includes":["scipy.signal"]}},
    executables = [Executable("my_script.py")]
)