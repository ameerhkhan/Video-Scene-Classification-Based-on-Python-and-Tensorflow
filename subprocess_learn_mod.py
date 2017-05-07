import subprocess
import numpy as np
import cv2
import os
import time


vdo = input('Please select a file to play using a number,\n 1. 458_video.mp4\n 2. Pistol.mp4 \n 3. Typewriter \n \n')
i = int(vdo)
if i == 1:
    vdo_loc = '458_video.mp4'
elif i == 2:
    vdo_loc = 'Pistol.mp4'
elif i == 3:
    vdo_loc = 'typewriter.mp4'
else:
    print('By Default 458_video.mp4 has been chosen')
    vdo_loc = '458_video.mp4'

print(vdo_loc)
#possibs = ['sports car', 'pencil', 'typewriter']
dicti = {
    'sports car': 'ffmpeg -i 458_video.mp4 -i ferrari458.mp3 -map 0:v -map 1:a -c copy -shortest output1.mp4',
    'assault rifle': 'ffmpeg -i Pistol.mp4 -i pistol_snd.mp3 -map 0:v -map 1:a -c copy -shortest output1.mp4',
    'typewriter': 'ffmpeg -i typewriter.mp4 -i typewriter_snd.mp3 -map 0:v -map 1:a -c copy -shortest output1.mp4',
    'rifle': 'ffmpeg -i Pistol.mp4 -i pistol_snd.mp3 -map 0:v -map 1:a -c copy -shortest output1.mp4'
     }

###################################################################
##########VIDEO PLAY###############################################

cap = cv2.VideoCapture(str(vdo_loc))

while(cap.isOpened()):
    ret, frame = cap.read()
    #some calculations to retain the aspect ratio of the original video
    #r = 100.0 / frame.shape[1]
    #dim = (100,int(frame.shape[0] * r))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(frame, (480,320), interpolation = cv2.INTER_AREA)                         

    cv2.imshow('Video', resized)
    #if cv2.waitKey(1) & 0xFF == ord('q'):#20 is the best
    if cv2.waitKey(2) & 0xFF == ord('q'):
        cv2.imwrite("captured.jpg", resized)
        #break
    elif cv2.waitKey(1) & 0xFF == ord('x'):
        #cv2.imwrite("captured.jpg", resized)
        break

cap.release()
cv2.destroyAllWindows()
print("Analysis in Progress Now..")

##################################################
#ls_outpit = subprocess.check_output(['ls','l'])
#out_one = subprocess.check_output('python video_play.py', shell = True)
#print((out_one).strip())
#out_one_str = (out_one.decode("utf-8")).strip()
#print(out_one_str)
#out_one.kill()
command = 'python classify_image_mod.py --image_file=R:\Work\ext_project\renny\models\tutorials\image\imagenet\captured.jpg'
#out_two = subprocess.check_output('python classify_image_mod.py --image_file=R:\Work\ext_project\renny\models\tutorials\image\imagenet\captured.jpg', shell = True)
out_two = subprocess.Popen('python classify_image_mod.py --image_file=captured.jpg',
                                    shell = True,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    )
std_val = out_two.communicate(timeout=15)[0]
#print((out_two).strip())
#out = out_two.stdout.read()
#print((std_val).strip())
val_str=std_val.decode("utf-8")
print('The Object has been identified as '+val_str)
#val_str = sport
#print(type(val_str))
#print(type(sport))
#print(out)
#print(dicti[(val_str).strip()])
vdo_cmd = dicti[(val_str).strip()]
subprocess.call(vdo_cmd, shell=True)
    
    
p = subprocess.Popen("R:/Work/ext_project/renny/models/tutorials/image/imagenet/output1.mp4", shell=True)
    
time.sleep(20)
os.remove('output1.mp4')
os.remove('captured.jpg')
    

"""if (val_str == possibs[1]):
    print(dicti['sports car'])
    subprocess.call(dicti['sports car'], shell=True)

elif val_str == 'pencil':
    print(dicti['pencil'])
        
elif val_str == 'typewriter':
    print(dicti['typewriter'])
else:
    print('No sound available for '+val_str)
"""
"""capn = cv2.VideoCapture('output1.mp4')
    
while(capn.isOpened()):
    retu, framee = capn.read()
    #some calculations to retain the aspect ratio of the original video
    #r = 100.0 / frame.shape[1]
    #dim = (100,int(frame.shape[0] * r))
    
    #graye = cv2.cvtColor(framee, cv2.COLOR_BGR2GRAY)
    resizede = cv2.resize(framee, (480,320), interpolation = cv2.INTER_AREA)                         
    
    cv2.imshow('New MUSIC Appended', resizede)
    if cv2.waitKey(20) & 0xFF == ord('s'): #20 is the best
458_video.mp4break
    
capn.release()
cv2.destroyAllWindows()
"""
