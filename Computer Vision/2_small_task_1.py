import numpy as np
import cv2
import os

os.makedirs("Outputs", exist_ok=True)

while True:
    path = input("\nEnter image name (inside Images/): ").strip()

    if not path:
        print("Path cannot be empty.")
        continue

    full_path = os.path.join("Images", path)

    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        continue

    img = cv2.imread(full_path)

    if img is None:
        print("Failed to load image.")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("Image loaded and converted to grayscale.")

    while True:
        print("\n1) Show image")
        print("2) Save image")
        print("3) Load a new image")
        print("4) Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            try:
                cv2.imshow("Grayscale", gray)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            except:
                print("Display failed (Wayland issue). Using matplotlib instead.")
                
                import matplotlib.pyplot as plt
                plt.imshow(gray, cmap='gray')
                plt.title("Grayscale Image")
                plt.axis('off')
                plt.show()

        elif choice == '2':
            save_name = input("Enter filename (e.g., result.png): ").strip()

            if not save_name:
                print("Filename cannot be empty.")
                continue

            if not save_name.lower().endswith((".png", ".jpg", ".jpeg")):
                print("Please include a valid extension (.png, .jpg, .jpeg).")
                continue

            save_path = os.path.join("Outputs", save_name)

            success = cv2.imwrite(save_path, gray)

            if success:
                print(f"Saved to {save_path}")
            else:
                print("Failed to save image.")

        elif choice == '3':
            break

        elif choice == '4':
            print("Exiting. Goodbye!")
            exit()

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")