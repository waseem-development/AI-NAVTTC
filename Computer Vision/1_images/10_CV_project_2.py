import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("Outputs", exist_ok=True)

# ---------------------------
# Show Image
# ---------------------------
def show_image(img):
    try:
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title("Image")
        plt.axis("off")
        plt.show()


# ---------------------------
# Save Image
# ---------------------------
def save_image(img):
    name = input("Enter output filename (e.g., result.png): ").strip()

    if not name:
        print("Filename cannot be empty.")
        return img

    if not name.lower().endswith((".png", ".jpg", ".jpeg")):
        print("Invalid extension.")
        return img

    path = os.path.join("Outputs", name)

    if cv2.imwrite(path, img):
        print(f"Saved to {path}")
    else:
        print("Failed to save image.")

    return img


# ---------------------------
# Draw Line
# ---------------------------
def draw_line(img):
    pt1 = (int(input("pt1 x: ")), int(input("pt1 y: ")))
    pt2 = (int(input("pt2 x: ")), int(input("pt2 y: ")))

    color = (
        int(input("Blue: ")),
        int(input("Green: ")),
        int(input("Red: "))
    )

    thickness = int(input("Thickness: "))

    cv2.line(img, pt1, pt2, color, thickness)
    return img


# ---------------------------
# Draw Rectangle
# ---------------------------
def draw_rectangle(img):
    pt1 = (int(input("pt1 x: ")), int(input("pt1 y: ")))
    pt2 = (int(input("pt2 x: ")), int(input("pt2 y: ")))

    color = (
        int(input("Blue: ")),
        int(input("Green: ")),
        int(input("Red: "))
    )

    thickness = int(input("Thickness: "))

    cv2.rectangle(img, pt1, pt2, color, thickness)
    return img


# ---------------------------
# Draw Circle
# ---------------------------
def draw_circle(img):
    center = (int(input("center x: ")), int(input("center y: ")))
    radius = int(input("Radius: "))

    color = (
        int(input("Blue: ")),
        int(input("Green: ")),
        int(input("Red: "))
    )

    thickness = int(input("Thickness: "))

    cv2.circle(img, center, radius, color, thickness)
    return img


# ---------------------------
# Put Text
# ---------------------------
def put_text(img):
    text = input("Enter text: ")

    org = (int(input("org x: ")), int(input("org y: ")))

    scale = float(input("Font scale: "))

    color = (
        int(input("Blue: ")),
        int(input("Green: ")),
        int(input("Red: "))
    )

    thickness = int(input("Thickness: "))

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(img, text, org, font, scale, color, thickness)
    return img


# ---------------------------
# Rotate Image
# ---------------------------
def rotate_image(img):
    h, w = img.shape[:2]

    center = (w // 2, h // 2)

    angle = float(input("Enter angle: "))
    scale = float(input("Enter scale: "))

    M = cv2.getRotationMatrix2D(center, angle, scale)

    rotated = cv2.warpAffine(img, M, (w, h))

    return rotated


# ---------------------------
# Flip Image
# ---------------------------
def flip_image(img):
    print("Flip Codes: 0=vertical, 1=horizontal, -1=both")

    flip_code = int(input("Enter flip code: "))

    flipped = cv2.flip(img, flip_code)

    return flipped


# ---------------------------
# MAIN PROGRAM
# ---------------------------
while True:

    path = input("\nEnter image name (inside Images/): ").strip()

    if not path:
        print("Path cannot be empty.")
        continue

    full_path = os.path.join("Images", path)

    if not os.path.exists(full_path):
        print("Image not found.")
        continue

    img = cv2.imread(full_path)

    if img is None:
        print("Failed to load image.")
        continue

    while True:

        print("""
1) Show image
2) Save image
3) Load new image
4) Draw Line
5) Draw Rectangle
6) Draw Circle
7) Put Text
8) Rotate Image
9) Flip Image
10) Exit
""")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_image(img)

        elif choice == "2":
            img = save_image(img)

        elif choice == "3":
            break

        elif choice == "4":
            img = draw_line(img)
            show_image(img)

        elif choice == "5":
            img = draw_rectangle(img)
            show_image(img)

        elif choice == "6":
            img = draw_circle(img)
            show_image(img)

        elif choice == "7":
            img = put_text(img)
            show_image(img)

        elif choice == "8":
            img = rotate_image(img)
            show_image(img)

        elif choice == "9":
            img = flip_image(img)
            show_image(img)

        elif choice == "10":
            print("Exiting...")
            exit()

        else:
            print("Invalid choice.")