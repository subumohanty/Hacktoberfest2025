import sys
from PIL import Image

def rotate_image(in_path: str, angle: float, out_path: str, expand=True):
    img = Image.open(in_path)
    rotated = img.rotate(-angle, expand=expand)  # pillow rotates counter-clockwise by default; invert if you want CW
    rotated.save(out_path)
    return out_path

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python rotate_image.py input.jpg angle output.jpg")
        sys.exit(1)
    in_p, ang, out_p = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    rotate_image(in_p, ang, out_p)
    print(f"Saved rotated image to {out_p}")
