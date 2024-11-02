from rembg import remove
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import create_main_window


def remove_background(input_folder, output_folder):

    # 処理対象の拡張子を指定（必要に応じて追加可能）
    valid_extensions = ['.png', '.jpg', '.jpeg']

    # 入力フォルダ内のファイルをループ処理
    for filename in os.listdir(input_folder):
        # ファイルの拡張子をチェックして画像ファイルのみ処理
        if any(filename.lower().endswith(ext) for ext in valid_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # 入力画像を読み込んで背景を除去
            with open(input_path, 'rb') as input_file:
                input_image = input_file.read()

            # 背景除去処理
            output_image = remove(input_image)

            # 結果を保存
            with open(output_path, 'wb') as output_file:
                output_file.write(output_image)


def start_background_removal(input_folder_var, output_folder_var):
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders.")
        return
    
    remove_background(input_folder, output_folder)    
    messagebox.showinfo('Success', "Background removal completed succesfully!")

def select_input_folder(input_folder_var):
    """入力フォルダを選択するダイアログを表示"""
    folder_selected = filedialog.askdirectory()
    input_folder_var.set(folder_selected)

def select_output_folder(output_folder_var):
    """出力フォルダを選択するダイアログを表示"""
    folder_selected = filedialog.askdirectory()
    output_folder_var.set(folder_selected)

def close_window(root):
    root.destroy()
    create_main_window.main()

def main():
    # Tkinter GUIの設定
    root = tk.Tk()
    root.geometry("400x400+900+500")
    root.title("Background remover")

    input_folder_var = tk.StringVar()
    output_folder_var = tk.StringVar()

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Input Folder:").pack(pady=5)
    tk.Entry(root, textvariable=input_folder_var, width=50).pack(pady=5)
    tk.Button(root, text="Browse", command=lambda: select_input_folder(input_folder_var)).pack(pady=5)

    tk.Label(root, text="Output Folder:").pack(pady=5)
    tk.Entry(root, textvariable=output_folder_var, width=50).pack(pady=5)
    tk.Button(root, text="Browse", command=lambda: select_output_folder(output_folder_var)).pack(pady=5)

    tk.Button(root, text="Remove Background", command=lambda: start_background_removal(input_folder_var, output_folder_var)).pack(pady=20)

    tk.Button(root, text="Back", command=lambda: close_window(root)).pack(pady=5)
    tk.Button(root, text="Quit", command=lambda: root.destroy()).pack(pady=5)
    # メインループの開始
    root.mainloop()



if __name__ == "__main__":
    main()