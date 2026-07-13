import base64

with open("images.jpg", "rb") as image:
    encoded = base64.b64encode(image.read()).decode()

print(encoded)