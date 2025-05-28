import cv2
import webbrowser
from pyzbar.pyzbar import decode
import time
import numpy as np

def detect_qr_code():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    
    print("Starting QR code detection...")
    print("Press 'q' to quit")
    
    while True:
        # Read frame from camera
        ret, frame = cap.read()
        
        # Decode QR codes in the frame
        decoded_objects = decode(frame)
        
        # Process each detected QR code
        for obj in decoded_objects:
            # Extract the data from QR code
            data = obj.data.decode('utf-8')
            
            # Draw rectangle around QR code
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                cv2.polylines(frame, [hull], True, (0, 255, 0), 2)
            else:
                cv2.polylines(frame, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)
            
            # Display the data
            print(f"QR Code detected: {data}")
            
            # Open the URL in default browser
            if data.startswith(('http://', 'https://')):
                webbrowser.open(data)
                print(f"Opening URL: {data}")
                time.sleep(2)  # Wait for 2 seconds before next detection
        
        # Display the frame
        cv2.imshow('QR Code Detector', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_qr_code()
