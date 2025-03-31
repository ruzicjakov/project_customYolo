from ultralytics import YOLO

model = YOLO("yolov11_custom.pt")

model.predict(source = "", show=True, save=True)