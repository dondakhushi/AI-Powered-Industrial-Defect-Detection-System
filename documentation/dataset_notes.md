## Selected Dataset

NEU-DET (Northeastern University Surface Defect Database)

## Dataset Description

NEU-DET is an industrial surface defect dataset containing grayscale images of hot-rolled steel surfaces.

* Number of images: 1,800
* Number of defect classes: 6
* Image type: Grayscale industrial surface images
* Annotation format: Pascal VOC XML
* Annotation type: Bounding boxes

## Defect Classes

1. Crazing
2. Inclusion
3. Patches
4. Pitted Surface
5. Rolled-in Scale
6. Scratches

## Why NEU-DET Was Selected

* It contains real industrial surface images.
* It has multiple defect classes.
* Bounding-box annotations are available.
* The annotations can be converted from Pascal VOC XML to YOLO format.
* It is suitable for object detection using YOLO.
* The dataset is manageable for this project.
* The dataset is suitable for the project's industrial surface defect detection objective.

## Dataset Structure

The downloaded dataset is organized into separate training and validation sets:

```text
NEU-DET/
├── train/
│   ├── images/
│   │   ├── crazing/
│   │   ├── inclusion/
│   │   ├── patches/
│   │   ├── pitted_surface/
│   │   └── rolled-in_scale/
│   └── annotations/
│       ├── crazing_1.xml
│       ├── crazing_10.xml
│       ├── crazing_100.xml
│       └── ...
│
└── validation/
    ├── images/
    └── annotations/
```

The `images` folders contain industrial defect images organized by defect category. The `annotations` folders contain Pascal VOC XML annotation files.

## Annotation Verification

The training annotation folder was inspected and XML files were found, including:

* `crazing_1.xml`
* `crazing_10.xml`
* `crazing_100.xml`
* `crazing_101.xml`
* `crazing_102.xml`

This confirms that the downloaded dataset contains XML annotation files.

## Dataset Verification

The following items were verified after downloading and extracting the dataset:

* Dataset downloaded successfully.
* Dataset extracted successfully.
* Training dataset is available.
* Validation dataset is available.
* Training images folder is available.
* Training annotations folder is available.
* Validation images folder is available.
* Validation annotations folder is available.
* XML annotation files are present.
* Multiple defect categories are present in the image dataset.

## Planned Use

The dataset will be used for training and evaluating the industrial defect detection model.

The existing Pascal VOC XML bounding-box annotations will later be converted into YOLO annotation format for use with the Ultralytics YOLO model.

Dataset conversion and model training are planned for later days of the project.

## Source

Kaggle — NEU-DET

Dataset URL: (https://www.kaggle.com/datasets/kaustubhdikshit/neu-surface-defect-database)

## Download Date

August 2026


