from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os


def convert_png_to_jpg(input_folder, output_folder):
    """
    PNG画像をJPGに変換する関数

    Args:
    - input_folder (str): 入力フォルダのパス
    - output_folder (str): 出力フォルダのパス
    """

    # 出力フォルダが存在しない場合は作成する
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            # 画像を開く
            img = Image.open(os.path.join(input_folder, filename))
            
            # jpgファイル名を作成
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"

            # 画像をJPEG形式で保存
            img.convert("RGB").save(os.path.join(output_folder, jpg_filename), "JPEG")

            print(f"Converted {filename} to {jpg_filename}")



def select_input_folder():
    #入力フォルダを選択するダイアログを表示
    folder_selected = filedialog.askdirectory()
    input_folder_var.set(folder_selected)

def select_output_folder():
    #出力フォルダを選択するダイアログを表示
    folder_selected = filedialog.askdirectory()
    output_folder_var.set(folder_selected)

def start_conversion():
    #変換処理を開始
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders.")
        return
    
    convert_png_to_jpg(input_folder, output_folder)
    messagebox.showinfo("Success", "Conversion completed successfully!")


# Tkinter GUIの設定
root = tk.Tk()
root.title(u"PNG to JPG Converter")

input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()


tk.Label(root, text="Input Folder: ").pack(pady=5)
tk.Entry(root, textvariable=input_folder_var, width=50).pack(pady=5)
tk.Button(root, text="Browse", command=select_input_folder).pack(pady=5)

tk.Label(root, text="Output Folder:").pack(pady=5)
tk.Entry(root, textvariable=output_folder_var, width=50).pack(pady=5)
tk.Button(root, text="Browse", command=select_output_folder).pack(pady=5)

tk.Button(root, text="Convert", command=start_conversion).pack(pady=20)

# メインループの開始
root.mainloop()