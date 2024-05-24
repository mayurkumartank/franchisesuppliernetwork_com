# Web Content Analysis Script

## Overview
This Python script is designed to extract content (text and images) from a given webpage and analyze it. The analysis includes counting the number of images and links, as well as categorizing image formats. Additionally, the script downloads images and saves them to a specified output folder.

## Requirements
- Python 3.x
- Libraries: `os`, `BeautifulSoup`, `requests`, `urllib`

## How to Use
1. Clone or download the script files to your local machine.
2. Ensure you have Python installed.
3. Install the required libraries using pip:
4. Run the script using the command line or an integrated development environment (IDE) such as PyCharm or Visual Studio Code.

## Usage

python main.py

## Script Functionality

- **Content Extraction**: The script extracts text and image URLs from the provided webpage using BeautifulSoup.
- **Analysis**: It analyzes the extracted content by counting the number of images and links, as well as categorizing image formats (PNG, JPG, JPEG).
- **Image Download**: The script downloads images from the webpage and saves them to a specified output folder.
- **Output**: The analysis results are saved in a text file named `analysis.txt`, and the extracted content is saved in a text file named `output_main.txt`.

## Customization
- You can customize the URL to analyze by modifying the `url` variable in the `main()` function.
- Adjust the user-agent string in the `headers` variable if necessary.
- Modify the output folder structure or file names as per your preference.

## File Structure
- `main.py`: Main Python script file.
- `output folder/`: Directory where output files and images are saved.
- `README.md`: Documentation file.
