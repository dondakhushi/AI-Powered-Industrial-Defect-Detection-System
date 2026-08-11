import os
import shutil
import xml.etree.ElementTree as ET

# Project paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "dataset", "NEU-DET-raw", "NEU-DET")
OUTPUT_DIR = os.path.join(BASE_DIR, "dataset", "processed")

# Class mapping
CLASS_NAMES = [
    "crazing",
    "inclusion",
    "patches",
    "pitted_surface",
    "rolled-in_scale",
    "scratches"
]

CLASS_MAP = {
    name: index
    for index, name in enumerate(CLASS_NAMES)
}


def convert_xml_to_yolo(xml_path, txt_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    size = root.find("size")

    image_width = int(size.find("width").text)
    image_height = int(size.find("height").text)

    yolo_lines = []

    for obj in root.findall("object"):
        class_name = obj.find("name").text.strip()

        if class_name not in CLASS_MAP:
            print(f"WARNING: Unknown class '{class_name}' in {xml_path}")
            continue

        class_id = CLASS_MAP[class_name]

        bbox = obj.find("bndbox")

        xmin = float(bbox.find("xmin").text)
        ymin = float(bbox.find("ymin").text)
        xmax = float(bbox.find("xmax").text)
        ymax = float(bbox.find("ymax").text)

        # Convert Pascal VOC to YOLO
        center_x = ((xmin + xmax) / 2) / image_width
        center_y = ((ymin + ymax) / 2) / image_height

        width = (xmax - xmin) / image_width
        height = (ymax - ymin) / image_height

        yolo_lines.append(
            f"{class_id} "
            f"{center_x:.6f} "
            f"{center_y:.6f} "
            f"{width:.6f} "
            f"{height:.6f}"
        )

    with open(txt_path, "w", encoding="utf-8") as file:
        file.write("\n".join(yolo_lines))


def process_split(split_name):
    source_dir = os.path.join(RAW_DIR, split_name)

    image_source = os.path.join(source_dir, "images")
    annotation_source = os.path.join(source_dir, "annotations")

    output_split = "val" if split_name == "validation" else "train"

    image_output = os.path.join(
        OUTPUT_DIR, "images", output_split
    )

    label_output = os.path.join(
        OUTPUT_DIR, "labels", output_split
    )

    os.makedirs(image_output, exist_ok=True)
    os.makedirs(label_output, exist_ok=True)

    xml_files = []

    for root_dir, _, files in os.walk(annotation_source):
        for file in files:
            if file.lower().endswith(".xml"):
                xml_files.append(
                    os.path.join(root_dir, file)
                )

    print(f"\nProcessing {split_name}...")
    print(f"XML files found: {len(xml_files)}")

    converted = 0

    for xml_path in xml_files:

        filename = os.path.splitext(
            os.path.basename(xml_path)
        )[0]

        txt_path = os.path.join(
            label_output,
            filename + ".txt"
        )

        # Find matching image
        image_path = None

        for extension in [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]:
            candidate = os.path.join(
                image_source,
                filename + extension
            )

            if os.path.exists(candidate):
                image_path = candidate
                break

        # Some dataset versions organize images by class folder
        if image_path is None:
            for root_dir, _, files in os.walk(image_source):
                for file in files:
                    if os.path.splitext(file)[0] == filename:
                        image_path = os.path.join(root_dir, file)
                        break

                if image_path:
                    break

        if image_path is None:
            print(f"WARNING: Image not found for {filename}")
            continue

        convert_xml_to_yolo(xml_path, txt_path)

        shutil.copy2(
            image_path,
            os.path.join(
                image_output,
                os.path.basename(image_path)
            )
        )

        converted += 1

    print(f"Converted: {converted}")


def create_data_yaml():
    yaml_path = os.path.join(
        OUTPUT_DIR,
        "data.yaml"
    )

    with open(yaml_path, "w", encoding="utf-8") as file:
        file.write(
            "path: " + OUTPUT_DIR.replace("\\", "/") + "\n"
        )
        file.write("train: images/train\n")
        file.write("val: images/val\n")
        file.write("\n")
        file.write("names:\n")

        for index, name in enumerate(CLASS_NAMES):
            file.write(f"  {index}: {name}\n")

    print(f"\nCreated: {yaml_path}")


def main():
    print("=" * 60)
    print("NEU-DET XML TO YOLO CONVERTER")
    print("=" * 60)

    if not os.path.exists(RAW_DIR):
        print("\nERROR: Raw dataset not found:")
        print(RAW_DIR)
        return

    process_split("train")
    process_split("validation")

    create_data_yaml()

    print("\nConversion completed successfully.")


if __name__ == "__main__":
    main()