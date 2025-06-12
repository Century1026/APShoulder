# Create and activate the Conda environment
```
conda create -n Shoulder_env python=3.8 -y
conda activate Shoulder_env
```

# Install dependencies
```
pip install -r requirements.txt
```

# Set up image folder
Place your image folders in "./images/dicom", replace DIR_IDS with the numbering of your folders.

# Run the prediction script
```
python predict_multiple_image.py
```