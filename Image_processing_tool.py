import tkinter as tk
import convert
import removeBG


def show_selection_screen():
    def on_select(option):
        if option == "convert":
            convert.main()
        elif option == "remove_bg":
            removeBG.main()
        
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select a task:").pack(pady=10)
    tk.Button(root, text="Convert PNG to JPG", command=lambda: on_select("convert")).pack(pady=10)
    tk.Button(root, text="Remove Image Background", command=lambda: on_select("remove_bg")).pack(pady=5)


# Tkinter GUIの設定
root = tk.Tk()
root.geometry("400x400+900+500")
root.title(u"Image Processing Tool")

input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()

show_selection_screen()

# メインループの開始
root.mainloop()