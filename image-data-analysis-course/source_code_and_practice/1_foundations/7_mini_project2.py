from skimage import io
import os

images_path = "./images"

images = {}

for filename in os.listdir(images_path):
    filepath = os.path.join(images_path, filename)
    image = io.imread(filepath)
    images[filename] = image

    print()
    kind = "RGB" if image.ndim == 3 else "grayscale"
    print(f"{filename:10s} \nshape={str(image.shape):15s} \ndtype={image.dtype} \nkind={kind} \nmean={image.mean():.1f}")

# print(images.keys())