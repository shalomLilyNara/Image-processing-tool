import tkinter as tk
import convert
import removeBG
import window_management as wm

def show_selection_screen(root):
    def on_select(option):
        if option == "convert":
            root.destroy()
            wm.create_convert_window()
        elif option == "remove_bg":
            root.destroy()
            wm.create_removebg_window()
        
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select a task:").pack(pady=10)
    #tk.Button(root, text="Convert PNG to JPG", command=lambda: on_select("convert")).pack(pady=10)
    tk.Button(root, text="Convert PNG to JPG", command=lambda: on_select("convert")).pack(pady=10)
    tk.Button(root, text="Remove Image Background", command=lambda: on_select("remove_bg")).pack(pady=5)
    tk.Button(root, text="Quit", command=lambda: root.destroy()).pack(pady=20)

def main():
    # Tkinter GUIの設定
    root = tk.Tk()
    root.geometry("400x400+900+500")
    root.title(u"Image Processing Tool")

    input_folder_var = tk.StringVar()
    output_folder_var = tk.StringVar()

    show_selection_screen(root)

    # メインループの開始
    root.mainloop()

if __name__ == "__main__":
    main()