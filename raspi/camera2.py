import cv2
import time

def main():
    capture = capture_write()
    
    
def capture_write(filename="image.jpeg", port=0, ramp_frames=30, x=1280, y=720):
    camera = cv2.VideoCapture(port)
    # Set REsolution
    camera.set(3, x)
    camera.set(4, y)
                  
    #Adjust camera lighting
    for i in range(ramp_frames):
         temp = camera.read()
    retval, im = camera.read()
    cv2.imwrite(filename,im)
    del(camera)
    return True
                  
if __name__ == '__main__':
    main()