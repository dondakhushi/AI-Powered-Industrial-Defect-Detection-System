# Requirements — AI-Powered Industrial Defect Detection System

## 1. Functional Requirements

### FR1. Image Upload
The system shall allow a user to upload an industrial surface image through the web interface.

### FR2. Image Analysis
The system shall analyze the uploaded image using a trained YOLO object detection model.

### FR3. Defect Detection and Classification
The system shall detect and classify industrial surface defects into the following six categories:

- Crazing
- Inclusion
- Patches
- Pitted Surface
- Rolled-in Scale
- Scratches

### FR4. Detection Result Display
The system shall display detected defects using bounding boxes, defect class labels, and confidence scores.

### FR5. Inspection Result Storage
The system shall store inspection results, including the uploaded image, detected defects, confidence scores, and timestamp in the MongoDB Atlas database.

### FR6. Inspection History
The system shall provide a history page that displays previously performed inspections.

### FR7. Inspection Details
The system shall allow the user to view the details of a selected inspection record.

### FR8. Inspection Record Deletion
The system shall allow the user to delete an inspection record from the system.

### FR9. Dashboard Statistics
The system shall display aggregate inspection statistics such as:

- Total number of inspections
- Number of defective inspections
- Number of non-defective inspections
- Distribution of detected defect classes

---

## 2. Non-Functional Requirements

### NFR1. Performance
The system should provide an image prediction within an acceptable time on CPU-based hardware.

### NFR2. Usability
The system shall provide a simple and user-friendly interface that does not require technical training.

### NFR3. Reliability
The system shall handle invalid file types, missing files, and corrupted images gracefully without crashing.

### NFR4. Scalability
The database design shall support an increasing number of inspection records without requiring major structural changes.

### NFR5. Maintainability
The project shall be organized into separate frontend, backend, database, and model components to simplify maintenance and future development.

### NFR6. Portability
The system should be capable of running in standard development environments without requiring a dedicated GPU.

### NFR7. Security
The system shall validate uploaded files and protect database credentials and other sensitive configuration information from being exposed in source code.

---

## 3. Hardware Requirements

- Development computer with at least 8 GB RAM recommended
- Multi-core CPU recommended
- GPU is optional
- Sufficient storage for the dataset, model files, and application files

---

## 4. Software Requirements

- Python 3.x
- Node.js 18+
- MongoDB Atlas
- Flask
- Ultralytics YOLO
- OpenCV
- PyMongo
- python-dotenv
- React
- Vite
- Axios
- Git and GitHub

---

## 5. Database Requirements

The system shall use MongoDB Atlas as the database management system.

The database shall store:

- Inspection records
- Uploaded image information
- Detection results
- Defect class information
- Confidence scores
- Inspection timestamps

The project database is named:

`defect_detection`

---

## 6. Dataset Requirements

The system shall use the NEU-DET industrial surface defect dataset.

The dataset contains six defect classes:

1. Crazing
2. Inclusion
3. Patches
4. Pitted Surface
5. Rolled-in Scale
6. Scratches

The original dataset contains Pascal VOC XML bounding-box annotations.

The XML annotations are converted into YOLO-compatible annotation format for model training.

---

## 7. System Constraints

- The system should support CPU-based execution.
- The system should accept valid industrial surface images as input.
- Dataset and trained model files may require significant storage and shall not be unnecessarily committed to GitHub.
- Database credentials shall not be hard-coded in source files.