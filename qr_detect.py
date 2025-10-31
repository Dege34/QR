import cv2
import webbrowser
from pyzbar.pyzbar import decode
import time
import numpy as np

def detect_qr_code():
    cap = cv2.VideoCapture(0)
    
    print("Starting QR code detection...")
    print("Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        
        decoded_objects = decode(frame)
        
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                cv2.polylines(frame, [hull], True, (0, 255, 0), 2)
            else:
                cv2.polylines(frame, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)
            
            print(f"QR Code detected: {data}")
            
            if data.startswith(('http://', 'https://')):
                webbrowser.open(data)
                print(f"Opening URL: {data}")
                time.sleep(2)
        
        cv2.imshow('QR Code Detector', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_qr_code()
