import cv2 as cv
from cv2 import aruco

marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

param_markers = aruco.DetectorParameters_create()
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(
        frame, marker_dict, parameters = param_markers    
        )
    if marker_corners:
        for ids, corners in zip(marker_IDs, marker_corners):
            cv.polylines(frame, [corners.astype(np.int32)], True, (0, 244, 28), 4, cv.LINE_AA)
            
            corners = corners.reshape(4,2)
            corners = corners.astype(int)
            top_right = corners.ravel()
            cv.putText(frame, f'id: {ids[0]}', top_right, 
                cv.FONT_HERSHEY_COMPLEX, 1.3, (0,255,23), 2, cv.LINE_AA)
            
            #print(ids,"  ", corners)    
        
    cv.imshow('frame', frame)
    key = cv.waitKey(1)  #take the input form the keyboard
    if key == ord('q'):  # convert the input into uni-code
        break 

cap.release()
cv.destroyAllWindows()
