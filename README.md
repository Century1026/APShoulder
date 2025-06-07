# Create and activate the Conda environment
```
conda create -n Shoulder_env python=3.8 -y
conda activate Shoulder_env
```

# Install dependencies
```
pip install -r requirements.txt
```
# Run the prediction script
```
python predict_single_image.py
```
# 生成的 NIfTI 格式分割文件位于 result 文件夹内
