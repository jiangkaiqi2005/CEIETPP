from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolo26n-seg.pt")

# Train the model with custom dataset
results = model.train(
    data=r"E:/College Students' Innovative Entrepreneurial Training Plan Program/Dataset/yolo_format/data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    device=0,
    degrees=5, # 在指定的角度范围内随机旋转图像，提高模型识别各种方向物体的能力。
    mixup=0.2, # 混合两个图像及其标签，创建一个合成图像。通过引入标签噪声和视觉变化，增强模型的泛化能力。
    shear=2, # 按指定的角度错切图像，模仿从不同角度观察物体的效果。
    patience=30, # 防过拟合
)

model = YOLO("runs/segment/train/weights/best.pt")

# Validate on training data
metrics = model.val()
print(metrics.seg.map) # mAP50-95
print(metrics.seg.map50) # mAP50
print(metrics.seg.map75) # mAP75
print(metrics.seg.maps) # list of mAP50-95 for each category