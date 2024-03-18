# ASSN: Attention-based Scale Sequence Network

This repository contains the research results of ASSN, which improved the performance of YOLOv7 based on [ssFPN](https://github.com/smu-ivpl/ssFPN), a previous study conducted on YOLOv4 and YOLOR.

----------------------------
## Performance
| Model | Test Size | AP<sup>test</sup> | AP<sub>50</sub><sup>test</sup> | AP<sub>75</sub><sup>test</sup> | AP<sub>S</sub><sup>test</sup> | AP<sub>M</sub><sup>test</sup> | AP<sub>L</sub><sup>test</sup> | Downloads |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | 
| **ASSN + YOLOv7** | 640 | **xx.x%** | **xx.x%** | **xx.x%** | **xx.x%** | **xx.x%** | **xx.x%** | [`assn_yolov7.pt`](https://drive.google.com/file/d/1oWQaeN-RIJINg4onkJafDyoPVq9UohcG/view?usp=drive_link) |
| **ASSN + YOLOv7-X** | 640 | **xx.x%** | **xx.x%** | **xx.x%** | **xx.x%** | **xx.x%** | **xx.x%** | [`assn_yolov7x.pt`](https://drive.google.com/file/d/1KzQpplxyk3vRcP_K1CNOc0LNaVcazBfD/view?usp=drive_link) |
| **ASSN + YOLOv7-W6** | 1280 | **xx.x%** | **xx.x%** | **xx.x%** | **xx.x%** | **xx.x%** | **xx.x%** | [`assn_yolov7w6.pt`](https://drive.google.com/file/d/1a0i74WuVH5ZM9AHLDLhwq6zFUNX89RHG/view?usp=drive_link) |

----------------------------
## ASSN Architecture
![architecture](figure/architecture.png)

----------------------------
## Comparison between the ssFPN and proposed ASSN
![comparison](figure/comparison.png)
***
