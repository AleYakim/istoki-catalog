"""
Конвертация PNG/JPEG → WebP 
Использование: python convert_to_webp.py <папка>
Пример: python convert_to_webp.py D:\stickers\flowers
"""
import sys, glob, os
from PIL import Image

def convert(folder):
    files = glob.glob(os.path.join(folder, "*.png")) + \
            glob.glob(os.path.join(folder, "*.jpg")) + \
            glob.glob(os.path.join(folder, "*.jpeg"))
    if not files:
        print(f"Нет PNG/JPG файлов в {folder}")
        return
    for f in files:
        img = Image.open(f).convert("RGBA")
        out = os.path.splitext(f)[0] + ".webp"
        img.save(out, "WEBP", quality=80)
        size_kb = os.path.getsize(out) / 1024
        print(f"  {os.path.basename(f)} → {os.path.basename(out)} ({size_kb:.0f} KB)")
        os.remove(f)
        print(f"  Удалён {os.path.basename(f)}")
    print(f"Готово: {len(files)} файлов")

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    convert(folder)