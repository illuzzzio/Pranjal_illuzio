import cv2
import mediapipe
import pyautogui
import win32com.client as wincom
x = input("press f")
if x =="f":
 speak = wincom.Dispatch("SAPI.SpVoice")
 text = ("you are looking beautiful today")
 speak.speak(text)
face_mesh_landmark = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks = True)
cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()
while True:
  _,image = cam.read()
  image = cv2.flip(image,1)
  window_h, window_w,window_depth = image.shape
  rgb_img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
  processed_image = face_mesh_landmark.process(rgb_img)
  all_face_landmarks_points = processed_image.multi_face_landmarks
  if all_face_landmarks_points:
    one_face_landmark_points = all_face_landmarks_points[0].landmark
    for id,landmark_point in enumerate(one_face_landmark_points[474:478]):
      x = int(landmark_point.x*window_w)
      y = int(landmark_point.y*window_h)
      if id ==1:
        eyellio_x = int(screen_w/window_w * x)
        eyellio_y = int(screen_h/window_h * y)
        pyautogui.moveTo(eyellio_x,eyellio_y)
      cv2.circle(image,(x,y),3,(0,0,266))
    left_eye = [one_face_landmark_points[145], one_face_landmark_points[159]]  
    for landmark_point in left_eye:
      x = int(landmark_point.x*window_w)
      y = int(landmark_point.y*window_h)
      cv2.circle(image,(x,y),3,(266,0,266))
    if(left_eye[0].y - left_eye[1].y<0.01):  
      pyautogui.click()
      pyautogui.sleep(2)
      print("mouse is clicked")
  key = cv2.imshow('eyeelio', image)
  cv2.waitKey(100)
  if key ==20:
   break
cam.release()
cv2.destroyAllWindows()