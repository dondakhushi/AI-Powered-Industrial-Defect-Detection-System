import os
import random
import shutil

random.seed(42)  # ensures the same split every time we run this

IMAGES_DIR = "NEU-DET-raw/NEU-DET/train/images"
LABELS_DIR = "processed/labels/train"

OUTPUT_BASE = "."  # dataset/ folder itself

SPLITS = {
    "train": 0.7,
    "val": 0.2,
    "test": 0.1,
}

# Create target folders
for split in SPLITS:
    os.makedirs(f"images/{split}", exist_ok=True)
    os.makedirs(f"labels/{split}", exist_ok=True)

# Get all image filenames recursively (from subfolders by class)
all_images = []
for root, dirs, files in os.walk(IMAGES_DIR):
    for f in files:
        if f.endswith(".jpg"):
            all_images.append(os.path.join(root, f))
random.shuffle(all_images)

total = len(all_images)
train_end = int(total * SPLITS["train"])
val_end = train_end + int(total * SPLITS["val"])

split_map = {}
for i, filename in enumerate(all_images):
    if i < train_end:
        split_map[filename] = "train"
    elif i < val_end:
        split_map[filename] = "val"
    else:
        split_map[filename] = "test"

for filename, split in split_map.items():
    # filename is now a full path, extract just the image filename
    img_filename = os.path.basename(filename)
    base_name = img_filename.replace(".jpg", "")

    src_img = filename  # filename is already the full path
    dst_img = f"images/{split}/{img_filename}"
    shutil.copy(src_img, dst_img)

    src_label = os.path.join(LABELS_DIR, base_name + ".txt")
    dst_label = f"labels/{split}/{base_name}.txt"
    if os.path.exists(src_label):
        shutil.copy(src_label, dst_label)
    else:
        # create empty label file if none exists (image with no defects)
        open(dst_label, "w").close()

print(f"Total images: {total}")
print(f"Train: {train_end}, Val: {val_end - train_end}, Test: {total - val_end}")