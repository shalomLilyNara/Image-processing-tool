from flask import Flask, render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
from PIL import Image
import os
from rembg import remove


app = Flask(__name__)
app.secret_key = 'PNG_to_JPG'
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/convert", methods=["POST", "GET"])
def convert():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('input_folder')
        
        if not uploaded_files:
            flash('No files selected')
            return redirect(request.url)
        
        for file in uploaded_files:
            # Process only PNG files
            if file.filename.endswith(".png"):
                input_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(input_path)
                
                # Set the output path and convert the file
                output_filename = os.path.splitext(file.filename)[0] + ".jpg"
                output_path = os.path.join(OUTPUT_FOLDER, output_filename)
                convert_png_to_jpg(input_path, output_path)
        
        flash("Conversion completed.")
        return redirect(url_for('convert'))

    return render_template('convert.html')

def convert_png_to_jpg(input_path, output_path):
    """
    Converts a single PNG image to JPG.
    
    Args:
    - input_path (str): Path to the input PNG file.
    - output_path (str): Path to save the converted JPG file.
    """
    img = Image.open(input_path)
    img.convert("RGB").save(output_path, "JPEG")



@app.route("/removeBG", methods=["POST", "GET"])
def removeBG():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('input_folder')
        
        if not uploaded_files:
            flash('No files selected')
            return redirect(request.url)
        
        for file in uploaded_files:
            input_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(input_path)
            output_path = os.path.join(OUTPUT_FOLDER, file.filename)
            remove_background(input_path, output_path)
        
        flash("Removal completed.")
        return redirect(url_for('removeBG'))

    return render_template("removeBG.html")

def remove_background(input_path, output_path):
    # 入力画像を読み込んで背景を除去
    with open(input_path, 'rb') as input_file:
        input_image = input_file.read()

    # 背景除去処理
    output_image = remove(input_image)

    # 結果を保存
    with open(output_path, 'wb') as output_file:
        output_file.write(output_image)

'''
    # 処理対象の拡張子を指定（必要に応じて追加可能）
    valid_extensions = ['.png', '.jpg', '.jpeg']
    # 入力フォルダ内のファイルをループ処理
    for filename in input_path:
        # ファイルの拡張子をチェックして画像ファイルのみ処理
        if any(filename.lower().endswith(ext) for ext in valid_extensions):
            input_path = os.path.join(input_path, filename)
            output_path = os.path.join(output_path, filename)
'''