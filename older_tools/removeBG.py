import os
from rembg import remove

# 入力フォルダと出力フォルダのパスを指定
input_folder = input("Input folder: ")  # 入力フォルダのパス
output_folder = input("Output folder: ")  # 出力フォルダのパス

# 出力フォルダが存在しない場合は作成
os.makedirs(output_folder, exist_ok=True)

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

        print(f'背景除去後の画像を {output_path} に保存しました。')

print('すべての画像の処理が完了しました。')