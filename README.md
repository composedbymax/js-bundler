# JS Bundler GUI

A simple Python desktop app to visually select, organize, and bundle JavaScript files into a single output file

## Features

- Graphical interface (built with Tkinter)  
- Add multiple `.js` files at once  
- See the list of files to be bundled  
- Remove or clear selected files  
- **Reorder files using "Move Up" and "Move Down" buttons** to control the bundling order  
- Bundle all files into one output in the order listed  
- Output includes clear file boundaries as comments  

## Requirements

- Python 3.x  
  *(Tkinter is included with most Python installations)*

## Usage

1. Clone the repo or download the `app.py` file:  
    ```bash
    git clone https://github.com/yourusername/js-bundler-gui.git
    cd js-bundler-gui
    ```

2. Run the app:  
    ```bash
    python app.py
    ```

3. Use the GUI to:  
   - Add `.js` files or all JS files in the current folder  
   - Select a file and use **Move Up** or **Move Down** buttons to reorder  
   - Remove or clear files  
   - Click **"Bundle JS"** and choose an output path  
