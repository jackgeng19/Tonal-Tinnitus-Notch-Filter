# Tonal-Tinnitus-Notch-Filter

# Tonal Tinnitus Notch Filter

This application is a simple GUI tool for filtering out specific frequency ranges from .wav audio files using the `scipy.signal` library. The user can specify the center frequency and bandwidth of the notch filter, and the application will apply the filter to the chosen audio file and save the filtered audio to a new file.

## Requirements

- Python 3.x
- soundfile
- scipy
- tkinter

## Usage

1. Clone or download this repository
2. Install the required packages by running `pip install -r requirements.txt`
3. Run the script by typing `python main.py` in the command line
4. A GUI window will appear, select the audio file by clicking the "Apply Filter" button
5. Enter the center frequency and bandwidth of the notch filter in Hz
6. Click the "Apply Filter" button again
7. The filtered audio will be saved to a new file called `filtered_file.wav`

## Note

- Make sure that the file you are trying to filter is a .wav file and that it is not corrupted.
- The center frequency and bandwidth should be entered in Hz and should be valid numbers.
- The application will raise an error if the file path is invalid or the file is corrupted.
- The application will raise an error if the center frequency or bandwidth input is invalid.
- The application is tested on MacOS, and it may not work as expected on other operating systems.

## Author

- Jack Geng
