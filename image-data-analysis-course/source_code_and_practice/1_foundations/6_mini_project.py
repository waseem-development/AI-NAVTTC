from skimage import data

images = {
    "astronaut": data.astronaut(),
    "chelsea":   data.chelsea(),
    "coffee":    data.coffee(),
    "camera":    data.camera(),
    "coins":     data.coins(),
}

for name, img in images.items():
    kind = "RGB" if img.ndim == 3 else "grayscale"
    print()
    print(f"{name:10s} \nshape={str(img.shape):15s} \ndtype={img.dtype} \nkind={kind} \nmean={img.mean():.1f}")
