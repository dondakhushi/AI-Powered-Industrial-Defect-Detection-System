from pathlib import Path

from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "model" / "yolo11n.pt"
DATA_PATH = ROOT / "dataset" / "processed" / "data.yaml"

model = YOLO(str(MODEL_PATH))

results = model.train(
    data=str(DATA_PATH),
    epochs=2,
    imgsz=200,
    batch=8,
    device="cpu",
    project=str(ROOT / "runs"),
    name="smoke_test",
)

print("Smoke test complete.")