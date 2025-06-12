# 📘 深度学习基础入门笔记

## 🔁 深度学习训练流程概览

- 一个完整的深度学习模型训练包括**训练集与验证集的双循环**：
  - **训练集**用于模型学习；
  - **验证集**用于检测模型是否泛化。
- 常见问题：
  - **欠拟合**：训练集和验证集效果都不好；
  - **过拟合**：训练集表现优秀，但验证集表现差。

---

## 🧠 卷积神经网络（CNN）

### ➕ 卷积操作简介

```python
import torch
import torch.nn.functional as F

input = torch.tensor([[1,2,0,3,1],
                      [0,1,2,3,1],
                      [1,2,1,0,0],
                      [5,2,3,1,1],
                      [2,1,0,1,1]], dtype=torch.float32)

kernel = torch.tensor([[1,2,1],
                       [0,1,0],
                       [2,1,0]], dtype=torch.float32)

input = input.view(1,1,5,5)
kernel = kernel.view(1,1,3,3)

out = F.conv2d(input, kernel, stride=1)
```

常见卷积参数：
- `kernel_size`: 卷积核大小
- `stride`: 步长
- `padding`: 补零方式

---

### 🖼 卷积应用于图像数据（CIFAR-10）

```python
import torch.nn as nn
import torchvision

class MyConvNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3)

    def forward(self, x):
        return self.conv(x)
```

使用 `torch.utils.tensorboard.SummaryWriter` 可视化输入与输出。

---

## 📉 池化层（Pooling）

### 最大池化示例

```python
from torch.nn import MaxPool2d

pool = MaxPool2d(kernel_size=3, ceil_mode=False)
```

池化用于下采样，减少计算量，保留关键信息。

---

## 🧪 激活函数（Activation）

```python
import torch.nn as nn

class ActivationDemo(nn.Module):
    def __init__(self):
        super().__init__()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        return self.sigmoid(x)
```

常见激活函数：
- ReLU：简单有效，避免梯度消失；
- Sigmoid：可输出概率，易梯度消失；
- Tanh：平滑输出，均值为0。

---

## 🏗 搭建 AlexNet 网络结构

```python
class AlexNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 48, kernel_size=5, stride=4),
            nn.MaxPool2d(2),
            nn.Conv2d(48, 128, 3),
            nn.MaxPool2d(2),
            nn.Conv2d(128, 192, 3),
            nn.Conv2d(192, 192, 3),
            nn.Conv2d(192, 128, 3),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(128*3*3, 2048),
            nn.Linear(2048, 1024),
            nn.Linear(1024, 10)
        )

    def forward(self, x):
        return self.model(x)
```

---

## 🧰 TensorBoard 可视化

1. 安装：
   ```bash
   pip install tensorboard
   ```

2. 运行命令：
   ```bash
   tensorboard --logdir=conv_logs
   ```

3. 浏览器访问地址：
   ```
   http://localhost:6006
   ```

---

## 🧾 自定义数据集的加载与训练

### 数据集准备

- 划分训练/验证集
- 生成 `train.txt`, `val.txt` 清单文件
- 自定义 `ImageTxtDataset` 加载器

---

## 🚀 GPU 训练支持

1. 检查是否支持：
   ```python
   torch.cuda.is_available()
   ```

2. 推送到 GPU：
   ```python
   model = model.cuda()
   input = input.cuda()
   ```

---

## 📉 常见损失函数（Loss Function）

### 1. 交叉熵损失

```python
import torch.nn as nn
loss_fn = nn.CrossEntropyLoss()
```

### 2. 均方误差

```python
loss_fn = nn.MSELoss()
```

---

## 🚴 优化器（Optimizer）

```python
from torch.optim import SGD, Adam
optimizer = Adam(model.parameters(), lr=0.001)
```

---

## 🪜 学习率调整（Scheduler）

```python
from torch.optim.lr_scheduler import StepLR
scheduler = StepLR(optimizer, step_size=10, gamma=0.1)
```

---

## 🧼 数据增强（Augmentation）

```python
import torchvision.transforms as transforms
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
])
```

---

## 💾 模型保存与加载

```python
torch.save(model.state_dict(), 'model.pth')
model.load_state_dict(torch.load('model.pth'))
```

---

## 🛠 训练结构模板

```python
for epoch in range(num_epochs):
    model.train()
    for imgs, labels in train_loader:
        ...
    model.eval()
    with torch.no_grad():
        ...
```

---

## 🗺 推荐学习路线图

1. 理论：感知机、多层感知器
2. 实战：LeNet → AlexNet → VGG → ResNet
3. 工具：TensorBoard、调参技巧
4. 高级：迁移学习、目标检测等
