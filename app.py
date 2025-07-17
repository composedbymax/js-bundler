import tkinter as tk
from tkinter import filedialog, messagebox
import os
class JSBundler:
    def __init__(self, master):
        self.master = master
        master.title("JS Bundler")
        master.geometry("600x400")
        self.file_list = []
        self.listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=80)
        self.listbox.pack(pady=10, expand=True)
        btn_frame = tk.Frame(master)
        btn_frame.pack()
        self.add_button = tk.Button(btn_frame, text="Add JS Files", command=self.add_files)
        self.add_button.grid(row=0, column=0, padx=5)
        self.remove_button = tk.Button(btn_frame, text="Remove Selected", command=self.remove_selected)
        self.remove_button.grid(row=0, column=1, padx=5)
        self.clear_button = tk.Button(btn_frame, text="Clear All", command=self.clear_files)
        self.clear_button.grid(row=0, column=2, padx=5)
        self.bundle_button = tk.Button(master, text="Bundle JS", command=self.bundle_files, bg="green", fg="white")
        self.bundle_button.pack(pady=15)
    def add_files(self):
        files = filedialog.askopenfilenames(filetypes=[("JavaScript Files", "*.js")])
        for file in files:
            if file not in self.file_list:
                self.file_list.append(file)
                self.listbox.insert(tk.END, os.path.basename(file))
    def remove_selected(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.file_list.pop(index)
            self.listbox.delete(index)
    def clear_files(self):
        self.file_list.clear()
        self.listbox.delete(0, tk.END)
    def bundle_files(self):
        if not self.file_list:
            messagebox.showwarning("No Files", "Please add some JS files first.")
            return
        output_path = filedialog.asksaveasfilename(defaultextension=".js", filetypes=[("JavaScript Files", "*.js")])
        if not output_path:
            return
        try:
            with open(output_path, 'w', encoding='utf-8') as outfile:
                for file in self.file_list:
                    with open(file, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(f"\n// ---- {os.path.basename(file)} ----\n")
                        outfile.write(content)
                        outfile.write("\n")
            messagebox.showinfo("Success", f"Bundled {len(self.file_list)} JS files into:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
if __name__ == "__main__":
    root = tk.Tk()
    app = JSBundler(root)
    root.mainloop()