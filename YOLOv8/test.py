from ultralytics import YOLO
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--weights', type=str, default='/home/ywlee/weights/yolov8n.pt')
  parser.add_argument('--yaml', type=str, default='yolov8n-assn.yaml')
  parser.add_argument('--data', type=str, default='coco.yaml')
  parser.add_argument('--device', type=int, default=1)
  parser.add_argument('--epochs', type=int, default=300)
  parser.add_argument('--imgsz', type=int, default=640)
  parser.add_argument('--resume', action='store_true', default=False)
  args = parser.parse_args()


  # Load a model
  model = YOLO(args.weights)

  # Customize validation settings
  validation_results = model.val(data=args.data,
                                 imgsz=args.imgsz,
                                 batch=1,
                                 conf=0.001,
                                 iou=0.65,
                                 device='1')