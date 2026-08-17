from pathlib import Path

from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "model" / "yolo11n.pt"
DATA_PATH = ROOT / "/workspaces/AI-Powered-Industrial-Defect-Detection-System/dataset/processed/data.yaml"

model = YOLO(str(MODEL_PATH))

results = model.train(
    data="DATA_PATH",
    epochs=80,
    imgsz=200,
    batch=16,
    device="cpu",
    patience=15,
    project="runs",
    name="neu_det_full",
)
print("Full training complete.")