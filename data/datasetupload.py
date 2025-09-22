import os
import zipfile
import subprocess
from PIL import Image

# -----------------------------
# 1️⃣ Kaggle credentials
# -----------------------------
KAGGLE_USERNAME = 'yasirumadhushan'
KAGGLE_KEY = 'a41c4a3a5e5d97980f2c3c655e1582fd'

# -----------------------------
# 2️⃣ Dataset info and paths
# -----------------------------
dataset = 'yasirumadhushan/sinhala-letter-454'
project_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(project_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

zip_path = os.path.join(data_dir, 'sinhala-letter-454.zip')

# -----------------------------
# 3️⃣ Download dataset using subprocess
# -----------------------------
if not os.path.exists(zip_path):
    print("Downloading dataset...")
    env = os.environ.copy()
    env['KAGGLE_USERNAME'] = KAGGLE_USERNAME
    env['KAGGLE_KEY'] = KAGGLE_KEY

    subprocess.run(
        ['kaggle', 'datasets', 'download', '-d', dataset, '-p', data_dir, '--force'],
        check=True,
        env=env
    )
    print("Download complete.")
else:
    print("Dataset zip already exists, skipping download.")

# -----------------------------
# 4️⃣ Unzip dataset
# -----------------------------
print("Extracting dataset...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(data_dir)
print("Dataset extracted to:", data_dir)

# -----------------------------
# 5️⃣ Load images into memory
# -----------------------------
dataset_folder = os.path.join(data_dir, 'sinhala-letter-454')  # adjust if unzip creates a different folder
images = []
image_filenames = []

for root, dirs, files in os.walk(dataset_folder):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(root, file)
            try:
                img = Image.open(img_path)
                images.append(img)
                image_filenames.append(img_path)
            except Exception as e:
                print(f"Error loading {img_path}: {e}")

print(f"Loaded {len(images)} images into memory.")
print("Sample images:", image_filenames[:5])