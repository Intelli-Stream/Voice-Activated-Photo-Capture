# 🎤 Voice-Activated Photo Capture 📸

This project is a **voice-activated camera application** built using **Streamlit**, **OpenCV**, and **SpeechRecognition**. It listens for the voice command **"capture"**, captures an image using your webcam, and displays the image on a web interface.

## 🚀 Features
- 🎙️ **Voice-Activated Command**: Say **"capture"** to take a photo.
- 📷 **Live Image Capture**: Captures images using your webcam.
- 🔊 **Sound Feedback**: Plays a click sound when an image is taken.
- 🖼️ **Default Placeholder Image**: Displays a default image before capturing.
- 🎛️ **Responsive UI**: Well-aligned buttons and images using Streamlit.

## 📁 Folder Structure
```
VOICE-ACTIVATED-PHOTO-CAPTURE/
│── static/
│   └── captured_photo.jpg  # Saved captured image
│── app.py                  # Main application file
│── temp_audio.wav          # Click sound file
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
```

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/voice-activated-photo-capture.git
cd voice-activated-photo-capture
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

## 🌍 Deployment on Streamlit Cloud
1. **Push Code to GitHub**
   - Create a GitHub repository.
   - Upload all files, including `requirements.txt` and `app.py`.

2. **Deploy on Streamlit Cloud**
   - Go to [Streamlit Cloud](https://share.streamlit.io).
   - Click **"New App"** → Connect GitHub → Select your repo.
   - Set `app.py` as the entry point.
   - Click **Deploy**.

3. **Access Your App**
   - Once deployed, you’ll get a URL like:
     ```
     https://your-app-name.streamlit.app
     ```

## 📝 Notes
- Ensure your **microphone and webcam** are enabled.
- If the **click sound doesn’t play**, check if `temp_audio.wav` is in the project folder.
- If **speech recognition fails**, ensure you're connected to the internet (it uses Google Speech API).

## 📌 Future Improvements
- 🎥 Live camera preview.
- 💾 Image storage and history.
- 🌍 Multi-language support for voice commands.

---
Made with ❤️ by [Your Name]

