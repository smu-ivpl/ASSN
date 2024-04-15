from ultralytics import YOLO
import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--weights', type=str, default=None)
  parser.add_argument('--yaml', type=str, default='yolov8n-assn.yaml')
  parser.add_argument('--data', type=str, default='coco.yaml')
  parser.add_argument('--device', type=list, default=[0,1,2,3])
  parser.add_argument('--epochs', type=int, default=300)
  parser.add_argument('--imgsz', type=int, default=640)
  parser.add_argument('--batch', type=int, default=64)
  parser.add_argument('--resume', action='store_true', default=False)
  args = parser.parse_args()

  # Load a model,
  # when using CLI: export PYTHONPATH=$PYTHONPATH:/home/ywlee/dev/YOLOv8/
  model = YOLO(args.yaml)  # build a new model from YAML
  if args.weights is not None:
    model.load(args.weights)

  # Train the model
  results = model.train(data=args.data,
                        epochs=args.epochs,
                        imgsz=args.imgsz,
                        batch=args.batch,
                        device=args.device,
                        name=args.yaml.split('.')[0],
                        resume=args.resume)
  print(results)