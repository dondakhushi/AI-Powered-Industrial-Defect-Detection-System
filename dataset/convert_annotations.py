import os
import xml.etree.ElementTree as ET

# ---- CONFIG: adjust these paths only if your folder names differ ----
IMAGES_DIR = "NEU-DET-raw/NEU-DET/train/images"
ANNOTATIONS_DIR = "NEU-DET-raw/NEU-DET/train/annotations"
OUTPUT_LABELS_DIR = "processed/labels/train"

# The 6 NEU-DET classes, in a fixed order (index = class_id)
CLASSES = [
    "crazing",
    "inclusion",
    "patches",
    "pitted_surface",
    "rolled-in_scale",
    "scratches",
]

os.makedirs(OUTPUT_LABELS_DIR, exist_ok=True)

def convert_box(size, box):
    """Convert (xmin, ymin, xmax, ymax) pixel box to normalized YOLO format."""
    img_w, img_h = size
    xmin, ymin, xmax, ymax = box
    x_center = ((xmin + xmax) / 2) / img_w
    y_center = ((ymin + ymax) / 2) / img_h
    width = (xmax - xmin) / img_w
    height = (ymax - ymin) / img_h
    return x_center, y_center, width, height

converted_count = 0
skipped_count = 0

for xml_file in os.listdir(ANNOTATIONS_DIR):
    if not xml_file.endswith(".xml"):
        continue

    xml_path = os.path.join(ANNOTATIONS_DIR, xml_file)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    size_tag = root.find("size")
    img_w = int(size_tag.find("width").text)
    img_h = int(size_tag.find("height").text)

    yolo_lines = []

    for obj in root.findall("object"):
        class_name = obj.find("name").text.strip()

        if class_name not in CLASSES:
            print(f"WARNING: unknown class '{class_name}' in {xml_file} — skipping this box")
            continue

        class_id = CLASSES.index(class_name)

        bndbox = obj.find("bndbox")
        xmin = float(bndbox.find("xmin").text)
        ymin = float(bndbox.find("ymin").text)
        xmax = float(bndbox.find("xmax").text)
        ymax = float(bndbox.find("ymax").text)

        x_center, y_center, width, height = convert_box((img_w, img_h), (xmin, ymin, xmax, ymax))
        yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    txt_filename = xml_file.replace(".xml", ".txt")
    txt_path = os.path.join(OUTPUT_LABELS_DIR, txt_filename)

    with open(txt_path, "w") as f:
        f.write("\n".join(yolo_lines))

    converted_count += 1

print(f"Done. Converted {converted_count} annotation files.")
print(f"YOLO labels saved to: {OUTPUT_LABELS_DIR}")