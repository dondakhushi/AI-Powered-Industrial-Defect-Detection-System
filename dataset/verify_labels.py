import cv2
import os
import random

IMAGES_DIR = "images/train"
LABELS_DIR = "labels/train"
OUTPUT_DIR = "verification_output"

CLASSES = ["crazing", "inclusion", "patches", "pitted_surface", "rolled-in_scale", "scratches"]

os.makedirs(OUTPUT_DIR, exist_ok=True)

all_images = [f for f in os.listdir(IMAGES_DIR) if f.endswith(".jpg")]
sample = random.sample(all_images, min(10, len(all_images)))

for filename in sample:
    img_path = os.path.join(IMAGES_DIR, filename)
    label_path = os.path.join(LABELS_DIR, filename.replace(".jpg", ".txt"))

    img = cv2.imread(img_path)
    h, w = img.shape[:2]

    if os.path.exists(label_path):
        with open(label_path) as f:
            lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5:
                continue
            class_id, x_c, y_c, bw, bh = parts
            class_id = int(class_id)
            x_c, y_c, bw, bh = float(x_c), float(y_c), float(bw), float(bh)

            x_center_px = x_c * w
            y_center_px = y_c * h
            box_w_px = bw * w
            box_h_px = bh * h

            xmin = int(x_center_px - box_w_px / 2)
            ymin = int(y_center_px - box_h_px / 2)
            xmax = int(x_center_px + box_w_px / 2)
            ymax = int(y_center_px + box_h_px / 2)

            cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            cv2.putText(img, CLASSES[class_id], (xmin, max(ymin - 5, 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imwrite(os.path.join(OUTPUT_DIR, filename), img)

print(f"Saved {len(sample)} verification images to {OUTPUT_DIR}/")