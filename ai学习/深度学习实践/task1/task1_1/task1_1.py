# 任务1_1: 实现一个简单的全连接网络，训练并评估 MNIST 数据集（MNIST_kaggle）
# 这里的MNIST数据集不是标准版，区别于传统的MNIST（60000张训练图，10000张测试图），对于标准版MNIST，
# 可以直接使用 torchvision.datasets.MNIST 来加载和处理数据，但这里我们需要自己实现数据加载逻辑。
# 这里的是kaggle上提供的一个变体（比赛专用版），包含训练集和测试集两部分，且测试集（28000张）没有标签。
# 我们需要训练模型在训练集上，并在测试集上做预测，提交预测结果进行评测。



import os
import re
import glob

# 解决 Windows 下 OpenMP 重复加载导致的崩溃（需在导入 torch 前设置）
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
from PIL import Image
import random

import torch.nn as nn
import matplotlib.pyplot as plt
from torchvision import transforms

print(torch.__version__)    

from torch.utils.data import Dataset, DataLoader


class MyDataset(Dataset):
    def __init__(self, data_dir, labeled=True):
        # 支持两种目录结构:
        # 1) labeled=True: trainingSet/0, trainingSet/1, ... trainingSet/9
        # 2) labeled=False: testSet/img_1.jpg, img_2.jpg, ...
        self.data_dir = data_dir # 数据目录路径
        self.labeled = labeled   # 是否有标签（训练集有标签，测试集无标签）
        self.samples = []        # 存储 (文件路径, 标签) 或 (文件路径,) 的列表

        # 图像预处理: 转灰度 -> 缩放到 28x28 -> 转为 [1, 28, 28] 的张量
        self.transform = transforms.Compose([
            transforms.Grayscale(num_output_channels=1),
            transforms.Resize((28, 28)),
            transforms.ToTensor(),
        ])

        if self.labeled:
            # 类别名直接使用子目录名，并映射到整数标签
            class_names = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))] # 获取所有子文件夹名作为类别
            class_names = sorted(class_names, key=lambda x: int(x) if x.isdigit() else x) # 按照数字顺序排序类别（假设目录名是数字）
            self.class_to_idx = {name: int(name) for name in class_names}          # 构建类别到标签的映射，例如 "0" -> 0, "1" -> 1, ..., "9" -> 9

            # 收集所有样本路径及其标签，形成 (file_path, label) 列表
            for class_name in class_names:
                class_dir = os.path.join(data_dir, class_name)
                for file_name in os.listdir(class_dir):
                    if file_name.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
                        file_path = os.path.join(class_dir, file_name)
                        label = self.class_to_idx[class_name]
                        self.samples.append((file_path, label))
        else:
            # 无标签测试集: 仅收集图片路径
            self.class_to_idx = {}
            for file_name in os.listdir(data_dir):
                file_path = os.path.join(data_dir, file_name)
                if os.path.isfile(file_path) and file_name.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
                    self.samples.append(file_path)

    def __len__(self):
        # 数据集大小 = 样本总数
        return len(self.samples)

    def __getitem__(self, idx):
        # 读取单个样本
        if self.labeled:
            file_path, label = self.samples[idx]
        else:
            file_path = self.samples[idx]
            label = None

        image = Image.open(file_path)
        image = self.transform(image)

        # 全连接网络输入要求一维向量，这里把 [1, 28, 28] 展平为 [784]
        image = image.view(-1)

        if self.labeled:
            # 返回 (特征, 标签)
            return image, torch.tensor(label, dtype=torch.long)

        # 无标签模式返回 (特征, 文件路径)
        return image, file_path


# 以脚本所在目录为基准拼接数据路径，避免受运行 cwd 影响
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
train_dir = os.path.join(script_dir, "MNIST_kaggle", "trainingSet")
test_dir = os.path.join(script_dir, "MNIST_kaggle", "testSet")

# 构建数据集与数据加载器
mydataset = MyDataset(data_dir=train_dir, labeled=True)
mydataset_loader = DataLoader(mydataset, batch_size=32, shuffle=True)
test_dataset = MyDataset(data_dir=test_dir, labeled=False)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

print(f"Train samples: {len(mydataset)}")
print(f"Test samples: {len(test_dataset)}")

# 简单检查前两个 batch 的形状是否符合预期
for batch_idx, (images, labels) in enumerate(mydataset_loader):
    print(f"Batch {batch_idx}: images={images.shape}, labels={labels.shape}")
    if batch_idx == 1:
        break


class MyNetwork(nn.Module):
    def __init__(self):
        super(MyNetwork, self).__init__()
        # 输入 784 维，隐藏层 128 维，输出 10 类 logits
        self.layer1 = nn.Linear(784, 128)
        self.act1= nn.ReLU()
        self.layer2 = nn.Linear(128, 10)

    def forward(self, x):
        # 前向传播: Linear -> ReLU -> Linear
        x = self.act1(self.layer1(x))
        x = self.layer2(x)
        return x


def evaluate(model, data_loader):
    if len(data_loader.dataset) == 0 or not data_loader.dataset.labeled:
        print("Warning: test set has no labels, skip accuracy evaluation.")
        return None

    # 评估模式: 关闭 dropout/bn 的训练行为（当前网络虽未使用，仍建议保留）
    model.eval()
    correct = 0
    total = 0

    # 评估阶段不需要计算梯度，可减少显存和加速
    with torch.no_grad():
        for images, labels in data_loader:
            outputs = model(images)
            preds = torch.argmax(outputs, dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

    # 切回训练模式，避免影响后续训练
    model.train()
    if total == 0:
        print("Warning: test set is empty, skip accuracy evaluation.")
        return None
    return correct / total


def single_sample_check(model, dataset):
    if len(dataset) == 0:
        print("Single image validation skipped: test dataset is empty.")
        return

    # 从测试集中随机抽取 1 张图，做一次单样本推理
    sample_idx = random.randint(0, len(dataset) - 1)
    sample = dataset[sample_idx]
    if dataset.labeled:
        image, label = sample
        image_path, _ = dataset.samples[sample_idx]
    else:
        image, image_path = sample
        label = None

    model.eval()
    with torch.no_grad():
        logits = model(image.unsqueeze(0))
        probs = torch.softmax(logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()
        confidence = probs[0, pred].item()
    model.train()

    print("\nSingle Image Validation")
    print(f"Image: {image_path}")
    if label is not None:
        print(f"True Label: {label.item()}, Pred Label: {pred}, Confidence: {confidence:.4f}")
    else:
        print(f"Pred Label: {pred}, Confidence: {confidence:.4f} (no ground-truth label)")
    
# 交叉熵损失: 输入是 logits，标签是 LongTensor 的类别索引
loss_fn = nn.CrossEntropyLoss()
out = MyNetwork()

# 快速做一次随机输入的前向和损失计算，验证网络可用
loss = loss_fn(out(torch.randn(32, 784)), torch.randint(0, 10, (32,)))

# Adam 优化器
optimizer = torch.optim.Adam(out.parameters(), lr=0.001)

# 训练循环（集成动态可视化）
epoch_losses = []
epoch_accs = []
epochs = 10

# 确保保存目录存在（固定到脚本所在目录）
checkpoint_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "checkpoints")
os.makedirs(checkpoint_dir, exist_ok=True)

# 让图窗口保持并在训练中持续更新
plt.ion()
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
loss_line, = axes[0].plot([], [], marker="o")
acc_line, = axes[1].plot([], [], marker="o", color="green")
axes[0].set_title("Training Loss (Live)")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Loss")
axes[0].grid(True, linestyle="--", alpha=0.4)
axes[1].set_title("Validation Accuracy (Live)")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Accuracy")
axes[1].grid(True, linestyle="--", alpha=0.4)

for epoch in range(epochs):
    out.train()
    running_loss = 0.0
    sample_count = 0
    for batch_idx, (images, labels) in enumerate(mydataset_loader):
        # 前向计算
        output = out(images)
        loss = loss_fn(output, labels)

        # 反向传播与参数更新
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # 累计 loss（按样本数加权更稳定）
        batch_size = labels.size(0)
        running_loss += loss.item() * batch_size
        sample_count += batch_size

        print(f"Epoch {epoch}, Batch {batch_idx}, Loss: {loss.item()}")

    # 记录每个 epoch 的平均 loss
    epoch_loss = running_loss / max(sample_count, 1)
    epoch_losses.append(epoch_loss)

    # 每个 epoch 结束后在测试集上评估一次准确率
    test_acc = evaluate(out, test_loader)
    epoch_accs.append(test_acc)
    if test_acc is not None:
        print(f"Epoch {epoch}, Test Accuracy: {test_acc * 100:.2f}%")

    # 每 2 个 epoch 保存一次模型参数
    if epoch % 1 == 0:
        torch.save(out.state_dict(), os.path.join(checkpoint_dir, f"model_epoch_{epoch}.pth"))

    # 动态更新曲线（每个 epoch 刷新一次）
    epochs_axis = list(range(1, len(epoch_losses) + 1))
    loss_line.set_data(epochs_axis, epoch_losses)
    axes[0].relim()
    axes[0].autoscale_view()

    valid_acc = [a for a in epoch_accs if a is not None]
    valid_epochs = [i + 1 for i, a in enumerate(epoch_accs) if a is not None]
    if valid_acc:
        acc_line.set_data(valid_epochs, valid_acc)
        axes[1].set_ylim(0, 1)
        axes[1].relim()
        axes[1].autoscale_view()

    fig.tight_layout()
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.001)

plt.ioff()
plt.show()

# 训练完成后，做一次单张图片验证
single_sample_check(out, test_dataset)


# ========================= 额外功能：推理全测试集并导出提交文件 =========================
# 说明：以下代码不会改动上面已有训练流程，只是在训练结束后追加推理与导出。
# 你可以直接运行脚本生成 kaggle_submit.csv，再提交到 Kaggle。

# 这里用到 pandas，仅在该段功能中导入，避免影响上面代码结构
import pandas as pd

# 选择 checkpoint 推理（可选："latest" 或指定文件名）
ckpt_choice = "latest"  # 例如: "model_epoch_8.pth"
ckpt_dir = checkpoint_dir

if ckpt_choice == "latest":
    ckpt_list = glob.glob(os.path.join(ckpt_dir, "model_epoch_*.pth"))
    if not ckpt_list:
        raise FileNotFoundError("No checkpoint found in 'checkpoints' directory.")

    def _epoch_num(path):
        match = re.search(r"model_epoch_(\d+)\.pth", os.path.basename(path))
        return int(match.group(1)) if match else -1

    ckpt_path = max(ckpt_list, key=_epoch_num)
else:
    ckpt_path = os.path.join(ckpt_dir, ckpt_choice)
    if not os.path.exists(ckpt_path):
        raise FileNotFoundError(f"Checkpoint not found: {ckpt_path}")

infer_model = MyNetwork()
infer_model.load_state_dict(torch.load(ckpt_path, map_location="cpu"))
infer_model.eval()
pred_records = [] 

# 测试集推理建议更大的 batch_size，提高速度
infer_loader = DataLoader(test_dataset, batch_size=128, shuffle=False) 

with torch.no_grad():
    for images, file_paths in infer_loader:
        # 前向推理得到 logits
        logits = infer_model(images)
        # 取概率最大的类别作为预测结果
        preds = torch.argmax(logits, dim=1).cpu().numpy().tolist()
        # 从文件名中解析 ImageId（如 img_123.jpg -> 123）
        for path, pred in zip(file_paths, preds):
            base = os.path.basename(path)
            match = re.search(r"\d+", base)
            if match is None:
                raise ValueError(f"Cannot parse image id from filename: {base}")
            image_id = int(match.group())
            pred_records.append((image_id, pred))

# 按 ImageId 数值升序排序，符合 Kaggle 的常见提交要求
pred_records.sort(key=lambda x: x[0])
submit_df = pd.DataFrame(pred_records, columns=["ImageId", "Label"])

# 保存 CSV 提交文件
submit_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kaggle_submit.csv")
submit_df.to_csv(submit_path, index=False)
print(f"Saved submission file: {submit_path}")

