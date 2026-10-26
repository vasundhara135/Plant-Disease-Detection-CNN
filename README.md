# 🌿 Plant Disease Detection Using CNN

A deep learning application that predicts plant disease classes from leaf images using a Convolutional Neural Network (CNN). The application provides a simple web interface built with Streamlit.

## 📌 Project Overview

Plant diseases can affect crop health and agricultural productivity. This project uses image classification to identify plant disease categories from uploaded leaf images.

Users can upload a leaf image and view the predicted class along with the model's confidence score.

## ✨ Features

- Upload leaf images in JPG, JPEG, or PNG format.
- Classify images into 38 plant disease categories.
- Display the predicted disease class.
- Show the model's prediction confidence.
- Interactive web interface using Streamlit.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Deep Learning:** TensorFlow, Keras
- **Image Processing:** Pillow, NumPy
- **Web Application:** Streamlit
- **Dataset:** New Plant Diseases Dataset (PlantVillage)

## 🧠 Model Details

The CNN model consists of convolutional layers, max-pooling layers, a fully connected dense layer, dropout regularization, and a softmax output layer for multi-class classification.

- **Input image size:** 128 × 128 pixels
- **Number of classes:** 38
- **Training epochs:** 5
- **Validation accuracy:** 91.46%

The reported validation accuracy is from the training experiment. Individual predictions may be incorrect, and the displayed confidence score is not a guarantee of correctness.

## 📂 Project Structure

```text
Plant-Disease-Detection-CNN/
├── app.py
├── class_names.json
├── plant_disease_model.h5
├── requirements.txt
├── README.md
└── Plant_Disease_Detection_CNN.ipynb
```

The notebook is optional. Include it only if you have retained the notebook used for your training workflow.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Plant-Disease-Detection-CNN
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL shown in your terminal, usually `http://localhost:8501`.

## 📊 Dataset

This project uses the New Plant Diseases Dataset, containing images of healthy and diseased plant leaves.

Dataset source: [New Plant Diseases Dataset on Kaggle](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

The dataset is used for model training and validation. Please refer to the dataset provider's terms and licensing information before redistributing dataset images.

## ⚠️ Limitations

- Predictions depend on image quality and the training data.
- The model may misclassify images taken under different lighting or backgrounds.
- Predictions should not be treated as a definitive agricultural diagnosis.

## 🙏 Acknowledgements

Thanks to the dataset contributors and the authors of the referenced plant disease detection project and learning resources.

This repository includes a trained model and a Streamlit interface. Refer to the original project and dataset sources when reusing their materials.

## 👩‍💻 Author

**Vasundhara Naga Durga Addala**

- GitHub: [vasundhara135](https://github.com/vasundhara135)