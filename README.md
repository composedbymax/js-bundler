# JS Bundler GUI

A simple Python desktop app to visually select, organize, and bundle JavaScript files into a single output file

## Features

- Graphical interface (built with Tkinter)
- Add multiple `.js` files at once
- See the list of files to be bundled
- Remove or clear selected files
- Bundle all files into one output in the order listed
- Output includes clear file boundaries as comments

## Requirements

- Python 3.x  
  *(Tkinter is included with most Python installations)*

## Usage

1. Clone the repo or download the `js_bundler.py` file:
    ```bash
    git clone https://github.com/yourusername/js-bundler-gui.git
    cd js-bundler-gui
    ```

2. Run the app:
    ```bash
    python app.py
    ```

3. Use the GUI to:
   - Add `.js` files
   - Arrange or remove files
   - Click **"Bundle JS"** and choose an output path