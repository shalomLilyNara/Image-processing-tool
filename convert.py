from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def convert_png_to_jpg(input_folder, output_folder):
    """
    PNG画像をJPGに変換する関数（フォルダ内のフォルダも再帰的に処理）

    Args:
    - input_folder (str): 入力フォルダのパス
    - output_folder (str): 出力フォルダのパス
    """

    # os.walk()を使用して再帰的にフォルダ内を探索
    for root, dirs, files in os.walk(input_folder):
        # 出力先のフォルダパスを現在のrootに合わせて更新
        relative_path = os.path.relpath(root, input_folder)
        current_output_folder = os.path.join(output_folder, relative_path)

        # 出力フォルダが存在しない場合は作成する
        if not os.path.exists(current_output_folder):
            os.makedirs(current_output_folder)

        # PNGファイルの変換処理
        for filename in files:
            if filename.endswith(".png"):
                img = Image.open(os.path.join(root, filename))
                jpg_filename = os.path.splitext(filename)[0] + ".jpg"
                img.convert("RGB").save(os.path.join(current_output_folder, jpg_filename), "JPEG")
                print(f"Converted {filename} to {jpg_filename}")


def select_input_folder(input_folder_var):
    """入力フォルダを選択するダイアログを表示"""
    folder_selected = filedialog.askdirectory()
    input_folder_var.set(folder_selected)

def select_output_folder(output_folder_var):
    """出力フォルダを選択するダイアログを表示"""
    folder_selected = filedialog.askdirectory()
    output_folder_var.set(folder_selected)

def start_conversion(input_folder_var, output_folder_var):
    """変換処理を開始する"""
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    
    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders.")
        return
    
    convert_png_to_jpg(input_folder, output_folder)
    messagebox.showinfo("Success", "Conversion completed successfully!")

def main():
    # Tkinter GUIの設定
    root = tk.Tk()
    root.geometry("400x400+900+500")
    root.title("PNG to JPG Converter (Recursive)")

    input_folder_var = tk.StringVar()
    output_folder_var = tk.StringVar()

    # フォルダ選択ボタン
    tk.Label(root, text="Input Folder:").pack(pady=5)
    tk.Entry(root, textvariable=input_folder_var, width=50).pack(pady=5)
    tk.Button(root, text="Browse", command=lambda: select_input_folder(input_folder_var)).pack(pady=5)

    tk.Label(root, text="Output Folder:").pack(pady=5)
    tk.Entry(root, textvariable=output_folder_var, width=50).pack(pady=5)
    tk.Button(root, text="Browse", command=lambda: select_output_folder(output_folder_var)).pack(pady=5)

    tk.Button(root, text="Convert", command=lambda: start_conversion(input_folder_var, output_folder_var)).pack(pady=20)

    # メインループの開始
    root.mainloop()


if __name__ == "__main__":
    main()