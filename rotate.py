from PIL import Image

image_path = input("Enter image path: ")
angle = float(input("Enter rotation angle (e.g., 90 or -45): "))

img = Image.open(image_path)
rotated = img.rotate(angle, expand=True)
rotated.save("rotated_output.jpg")

print(f"✅ Image rotated by {angle}° and saved as rotated_output.jpg")
rotated.show()
