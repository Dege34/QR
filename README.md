# QR Code Detector (Python, OpenCV + pyzbar)

Real-time QR code scanner using your webcam. Draws a green polygon around detected codes and **auto-opens URLs** (`http://` or `https://`) in your default browser. Press **`q`** to quit.

> Replace this with your repo URL  
> https://github.com/Dege34/QR.git

---

## Features
- **Live detection** from your default camera (`cv2.VideoCapture(0)`).
- **Polygon overlay** around detected QR codes (convex hull when needed).
- **Auto-open URLs** in the system browser (with debounce/cooldown).
- **Press `q`** or **Esc** to exit.
- **CLI flags**: choose camera index, toggle auto-open, set cooldown, and request resolution.

---

## How it works
1. Captures frames from the webcam with OpenCV.
2. Uses `pyzbar.decode(frame)` to read QR codes.
3. Draws a convex hull or polyline around the code corners.
4. If the decoded text is a URL, opens it with `webbrowser.open()` and respects a cooldown to avoid repeated opens.

---
## Setup
1) Clone
git clone https://github.com/Dege34/QR.git

``cd your-repo``

2) (Recommended) Create & activate a virtualenv
   
``python -m venv .venv``

-Windows:

``.venv\Scripts\activate``

-macOS/Linux:

``source .venv/bin/activate``

4) Install Python deps
   
``pip install -r requirements.txt``

5) Ensure ZBar is installed (see above)

6) Run
   
``python main.py``

---

## Troubleshooting

#### -ImportError: Unable to find zbar shared library
ZBar isn’t found. Install it (see “System dependency: ZBar”). On Windows, ensure the DLL is on your PATH.

#### -Black/empty camera window
Try a different index: --camera 1. Check camera permissions or close other apps using the camera.

#### -Repeated openings
Use a higher --cooldown value or run with --no-open.

#### -Poor detection
Improve lighting, avoid glare, move closer, or increase the QR code size.
