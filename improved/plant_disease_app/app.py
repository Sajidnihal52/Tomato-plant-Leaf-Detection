from flask import Flask, render_template, request, url_for
import torch
import torch.nn as nn
from torchvision import transforms, datasets
from PIL import Image
import os
import torch.nn.functional as F  # for softmax

# =========================
# 1. APP SETUP
# =========================
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# =========================
# 2. DEVICE
# =========================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# =========================
# 3. CNN MODEL DEFINITION
# =========================
class CNN(nn.Module):
    def __init__(self, num_classes):
        super(CNN, self).__init__()
        
        self.conv = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),
            
            nn.Conv2d(32, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),
            
            nn.Conv2d(64, 128, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        
        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128*16*16, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        x = self.conv(x)
        x = self.fc(x)
        return x

# =========================
# 4. LOAD CLASS NAMES AUTOMATICALLY
# =========================
dataset_dir = r"G:\12 Semester\CVPR\MID\CNN_Project\improved\dataset\New Plant Diseases Dataset(Augmented)\train"
train_data = datasets.ImageFolder(dataset_dir)
class_names = train_data.classes
print("Classes:", class_names)

# =========================
# 5. LOAD MODEL
# =========================
model = CNN(num_classes=len(class_names)).to(device)
model.load_state_dict(torch.load("cnn_model.pth", map_location=device))
model.eval()

# =========================
# 6. IMAGE TRANSFORM
# =========================
transform = transforms.Compose([
    transforms.Resize((128,128)),
    transforms.ToTensor()
])

# =========================
# 7. PREDICTION FUNCTION WITH CONFIDENCE
# =========================
def predict_image(image_path, threshold=0.5):
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(device)
    
    with torch.no_grad():
        output = model(image)
        probs = F.softmax(output, dim=1)
        confidence, predicted = torch.max(probs, 1)
        
        if confidence.item() < threshold:
            return "Warning: This may not be a tomato leaf. Please upload a tomato leaf image."
        
        return class_names[predicted.item()]

# =========================
# 8. ROUTES
# =========================
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    uploaded_file = ""
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("index.html", prediction="No file uploaded")
        
        file = request.files["file"]
        if file.filename == "":
            return render_template("index.html", prediction="No file selected")
        
        # Save uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        uploaded_file = file.filename
        
        # Make prediction
        prediction = predict_image(filepath)
    
    return render_template("index.html", prediction=prediction, uploaded_file=uploaded_file)

# =========================
# 9. RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)