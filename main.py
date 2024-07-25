import os
from pathlib import Path

def count_images(folder_path):
    # 画像ファイルの拡張子リスト
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    
    # 画像ファイルの数をカウントする変数
    image_count = 0
    
    # フォルダ内のファイルを走査
    for file in Path(folder_path).iterdir():
        if file.is_file() and file.suffix.lower() in image_extensions:
            image_count += 1
    
    return image_count

# メイン処理
if __name__ == "__main__":
    folder_path = input("画像ファイルを数えるフォルダのパスを入力してください: ")
    
    if os.path.isdir(folder_path):
        num_images = count_images(folder_path)
        print(f"フォルダ内の画像ファイル数: {num_images}")
    else:
        print("無効なフォルダパスです。正しいパスを入力してください。")