# ASSN: Attention-based Scale Sequence Network

This repository contains the sources of ASSN, which improved the small object dectection performance. This includes the experimental results and the trained models on YOLOv7 and YOLOv8 based on [ssFPN](https://github.com/smu-ivpl/ssFPN), a previous study conducted on YOLOv4 and YOLOR.

This repository was created based on the official repository source of [YOLOv7](https://github.com/WongKinYiu/yolov7) and [YOLOv8](https://github.com/ultralytics/ultralytics).

----------------------------
## Performance (MS-COCO)
### Validation Set (5k images)
| Model | Test Size | AP | AP<sub>50</sub> | AP<sub>75</sub> | AP<sub>S</sub> | AP<sub>M</sub> | AP<sub>L</sub> |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| YOLOv7 | 640 | 51.2% | 69.7% | 55.5% | 35.2% | 56.0% | 66.7% |
| YOLOv7-X | 640 | 52.9% | 71.1% | 57.5% | 36.9% | 57.7% | 68.6% |
| YOLOv7-W6 | 1280 | 54.6% | 72.3% | 59.5% | 40.1% | 59.0% | 68.6% |
| YOLOv8n | 640 | 37.4% | 52.9% | 40.3% | 18.6% | 41.0% | 53.5% |
| YOLOv8s | 640 | 44.9% | 62.1% | 48.3% | 25.9% | 49.9% | 61.0% |
| [**YOLOv7 + ASSN**](https://drive.google.com/file/d/1oWQaeN-RIJINg4onkJafDyoPVq9UohcG/view?usp=drive_link) | 640 | **51.5%** | **70.0%** | **56.1%** | **35.7%** | **56.3%** | 65.8% |
| [**YOLOv7-X + ASSN**](https://drive.google.com/file/d/1KzQpplxyk3vRcP_K1CNOc0LNaVcazBfD/view?usp=drive_link) | 640 | **53.5%** | **71.6%** | **58.2%** | 36.7% | 58.3% | 69.7% |
| [**YOLOv7-W6 + ASSN**](https://drive.google.com/file/d/1a0i74WuVH5ZM9AHLDLhwq6zFUNX89RHG/view?usp=drive_link) | 1280 | **55.0%** | **72.7%** | **60.1%** | 40.0% | **59.5%** | 68.2% |
| [**YOLOv8n + ASSN**] | 640 | 37.4% | **53.2%** | **40.5%** | **20.5%** | **41.6%** | 51.6% |
| [**YOLOv8s + ASSN**] | 640 | **45.0%** | **62.3%** | **49.1%** | **27.2%** | **50.3%** | 59.7% |
### Test Set (test-dev2017, 20k images)
| Model | Test Size | AP | AP<sub>50</sub> | AP<sub>75</sub> | AP<sub>S</sub> | AP<sub>M</sub> | AP<sub>L</sub> |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| YOLOv7 | 640 | 51.4% | 69.7% | 55.9% | 31.8% | 55.5% | 65.0% |
| YOLOv7-X | 640 | 53.1% | 71.2% | 57.8% | 33.8% | 57.1% | 67.4% |
| YOLOv7-W6 | 1280 | 54.9% | 72.6% | 60.1% | 37.3% | 58.7% | 67.1% |
| [**ASSN + YOLOv7**](https://drive.google.com/file/d/1oWQaeN-RIJINg4onkJafDyoPVq9UohcG/view?usp=drive_link) | 640 | **51.9%** | **70.3%** | **56.5%** | **32.6%** | **55.7%** | **65.4%** |
| [**ASSN + YOLOv7-X**](https://drive.google.com/file/d/1KzQpplxyk3vRcP_K1CNOc0LNaVcazBfD/view?usp=drive_link) | 640 | **53.5%** | **71.5%** | **58.2%** | **34.3%** | **57.5%** | **67.4%** |
| [**ASSN + YOLOv7-W6**](https://drive.google.com/file/d/1a0i74WuVH5ZM9AHLDLhwq6zFUNX89RHG/view?usp=drive_link) | 1280 | **55.2%** | **72.9%** | **60.5%** | **37.9%** | **58.8%** | **67.5%** |
### Testing Environment
|||
| :-: | :-: |
| CPU | Intel® Core™ i9-9900K CPU @ 3.60GHz × 16 |
| GPU | NVIDIA GeForce GTX 1080 Ti (11GB) |
| OS | Ubuntu 22.04.3 LTS |
----------------------------
## ASSN Architecture
![architecture](figure/architecture.png)

----------------------------
## Comparison between the ssFPN and proposed ASSN
![comparison](figure/comparison.png)
***
