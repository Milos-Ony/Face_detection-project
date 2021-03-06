# Importing libraries 
import cv2
import vlc

# Importing .xml haarcascade model 
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)

previous = 0
current = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Variables needed for if statement
    previous = current
    current = len(faces)

    # Checking if new face entered the frame
    if (current - previous) > 0:
        player = vlc.MediaPlayer("zdezynfekuj-rece.mp3")
        player.play()
        time.sleep(6)
        player.release()
        
    # Display the resulting frame
    cv2.imshow('Video', frame)
    
    # Exit condition (press q)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
