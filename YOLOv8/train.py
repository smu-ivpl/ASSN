from ultralytics import YOLO

# Load a model
model = YOLO('/home/ywlee/dev/ASSN/YOLOv8/ultralytics/cfg/models/v8/yolov8n-assn.yaml')  # build a new model from YAML
model.load('/home/ywlee/weights/yolov8n.pt')
# model = YOLO('/home/ywlee/weights/yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='coco128.yaml', epochs=100, imgsz=640)