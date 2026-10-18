🍅 Tomato Plant Leaf Disease Detection

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=25&duration=3000&pause=1000&color=2ECC71&center=true&vCenter=true&width=750&lines=AI-Powered+Plant+Disease+Detection;Deep+Learning+%7C+Computer+Vision;Building+Smarter+Agricultural+Solutions" alt="Typing SVG" />
</p><p align="center">
  <img src="https://img.shields.io/badge/Project-Tomato%20Disease%20Detection-2ECC71?style=for-the-badge&logo=leaflet&logoColor=white" alt="Project"/>
  <img src="https://img.shields.io/badge/AI-Deep%20Learning-8A2BE2?style=for-the-badge" alt="AI"/>
  <img src="https://img.shields.io/badge/Status-Under%20Development-orange?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/Domain-Agriculture-228B22?style=for-the-badge" alt="Agriculture"/>
</p><p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,flask,opencv,html,css,git,github&perline=8" alt="Technologies"/>
</p>---

🌱 About the Project

Tomato Plant Leaf Disease Detection is an AI-powered project that uses deep learning and computer vision to identify diseases in tomato plants by analyzing images of their leaves.

The system uses an image classification model to recognize different tomato leaf conditions and predict the corresponding class from an uploaded image.

The goal is to develop an accessible and user-friendly solution that can support farmers, gardeners, and agricultural enthusiasts in identifying potential plant health problems.

🎯 Project Objectives

- 🤖 Develop a deep learning model for tomato leaf disease classification.
- 🍃 Identify different tomato leaf conditions from images.
- 🧠 Apply computer vision techniques for image analysis.
- 🖥️ Build a user-friendly interface for image upload and prediction.
- 📱 Explore mobile-based disease detection using a smartphone camera.
- 🌍 Expand the system to support other plant species in the future.

---

🚀 Key Features

<p align="center">
  <img src="https://img.shields.io/badge/📷-Image%20Upload-3498DB?style=for-the-badge" alt="Image Upload"/>
  <img src="https://img.shields.io/badge/🧠-AI%20Prediction-8E44AD?style=for-the-badge" alt="AI Prediction"/>
  <img src="https://img.shields.io/badge/🍃-Leaf%20Classification-27AE60?style=for-the-badge" alt="Classification"/>
</p>- 📷 Upload tomato leaf images for analysis.
- 🔍 Predict the class of a tomato leaf image.
- ⚡ Use a trained deep learning model for inference.
- 🖥️ Access predictions through a web interface.
- 📊 Evaluate classification performance using standard metrics.
- 🔮 Plan future integration of disease information and prevention guidance.

---

🖼️ Project Preview

<!-- Add your actual application screenshot here --><p align="center">
  <img src="https://placehold.co/900x450/10251B/FFFFFF?text=Tomato+Leaf+Disease+Detection+Dashboard" width="90%" alt="Tomato Disease Detection Application Preview"/>
</p><p align="center">
  <i>Application preview placeholder — replace it with a screenshot of your actual project.</i>
</p>---

🛠️ Technology Stack

Technology| Purpose
🐍 Python| Model development and data processing
🔥 PyTorch / TensorFlow| Deep learning and image classification
👁️ OpenCV| Image processing and computer vision
🌐 Flask / FastAPI| Backend and prediction API
🖼️ HTML & CSS| Web interface
📊 NumPy & Pandas| Data handling and analysis
📈 Matplotlib| Performance visualization
🔧 Git & GitHub| Version control and project management

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3"/>
</p>---

⚙️ How It Works

flowchart TD
    A[Upload Tomato Leaf Image] --> B[Image Preprocessing]
    B --> C[Trained Deep Learning Model]
    C --> D[Image Classification]
    D --> E[Predicted Class]
    E --> F[Display Result on Web Interface]
    F --> G[Optional Disease Information]

🔬 Workflow

1. Image Input: The user uploads a tomato leaf image.
2. Preprocessing: The image is resized and transformed to match the model's input requirements.
3. Model Inference: The trained deep learning model analyzes the image.
4. Classification: The model produces class scores and selects the predicted class.
5. Result Display: The application displays the prediction to the user.

---

📊 Model Evaluation

The model will be evaluated using standard classification metrics to understand its performance on unseen images.

<p align="center">
  <img src="https://img.shields.io/badge/Metrics-Accuracy-blue?style=for-the-badge" alt="Accuracy"/>
  <img src="https://img.shields.io/badge/Metrics-Precision-orange?style=for-the-badge" alt="Precision"/>
  <img src="https://img.shields.io/badge/Metrics-Recall-green?style=for-the-badge" alt="Recall"/>
  <img src="https://img.shields.io/badge/Metrics-F1--Score-purple?style=for-the-badge" alt="F1 Score"/>
</p>Evaluation Metric| Purpose
Accuracy| Measures the overall proportion of correct predictions
Precision| Measures how often predictions for a class are correct
Recall| Measures how many actual samples of a class are identified
F1-score| Balances precision and recall
Confusion Matrix| Shows correct and incorrect predictions for each class

«Note: Add your actual test results and model performance charts after evaluation. No accuracy or performance results are claimed in this README.»

---

🧪 Dataset

The project uses tomato leaf images organized by class for supervised image classification.

The dataset may contain healthy leaves and several disease categories, depending on the dataset used.

Expected dataset structure:

dataset/
├── train/
│   ├── Tomato___Bacterial_spot/
│   ├── Tomato___Early_blight/
│   ├── Tomato___Late_blight/
│   ├── Tomato___Leaf_Mold/
│   └── ...
├── valid/
│   ├── ...
└── test/
    ├── ...

The folder names above are examples. Update them to match your actual dataset.

---

🗺️ Future Roadmap

- [x] Initial project concept
- [ ] Prepare and preprocess the dataset
- [ ] Train and evaluate the classification model
- [ ] Improve generalization on unseen images
- [ ] Build a web-based prediction interface
- [ ] Add disease information and prevention guidance
- [ ] Develop a mobile application
- [ ] Extend support to additional plant species

---

🔮 Future Improvements

- 📱 Mobile application with smartphone camera support.
- 🌿 Multi-plant disease classification.
- 💡 Explainable AI to highlight important leaf regions.
- 🌦️ Testing under different lighting and environmental conditions.
- 📚 Disease information and prevention recommendations.
- ☁️ Cloud deployment for broader accessibility.

---

💻 Installation and Usage

1. Clone the repository

git clone https://github.com/Sajidnihal52/Tomato-Plant-Leaf-Disease-Detection.git
cd Tomato-Plant-Leaf-Disease-Detection

2. Create a virtual environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Activate it on Linux or macOS:

source venv/bin/activate

3. Install dependencies

pip install torch torchvision flask pillow numpy matplotlib opencv-python

4. Run the application

If your Flask entry-point file is named "app.py":

python app.py

Open the local address displayed by Flask in your browser, commonly "http://127.0.0.1:5000/".

«Adjust the repository URL, dependencies, model file path, and startup command to match your actual project structure.»

---

🤝 Contributions

Contributions, suggestions, and feedback are welcome!

You can contribute by improving the model, optimizing preprocessing, enhancing the user interface, testing new datasets, or developing additional features.

1. Fork this repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

---

👨‍💻 Developer

<p align="center">
  <b>Sajid Mahmud</b>
</p><p align="center">
  <a href="https://github.com/Sajidnihal52">
    <img src="https://img.shields.io/badge/GitHub-Sajidnihal52-181717?style=for-the-badge&logo=github" alt="GitHub Profile"/>
  </a>
</p><p align="center">
  <i>Building AI solutions for smarter agriculture and a healthier future. 🌱</i>
</p><p align="center">
  <img src="https://komarev.com/ghpvc/?username=Sajidnihal52&style=flat-square&color=2ECC71" alt="Repository README author profile views"/>
</p>---

<p align="center">
  <b>🍅 Artificial Intelligence for Better Plant Health 🌿</b>
</p>
