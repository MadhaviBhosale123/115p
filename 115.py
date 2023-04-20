import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = "F:/Madhavi Folder/mark"             
dest = "F:/Madhavi Folder/mark1" 


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print('Downloaded'+file_name)
                
                path1 = source+'/'+file_name
                path2 = dest + '/' + key
                path3 = dest + '/' + key + file_name
                
                if os.path.exists(path2):
                    print("Directory Exists ...")
                    time.sleep(1)
                    
                    if os.path.exists(path3):
                        print("File Already Exists in"+key+"....")
                        print("Renaming File"+file_name+"....")
                        
                        new_file_name = os.path.splitext(file_name)[0]+str(random.randint(0,999))+os.path.splitext(file_name)[1]
                        
                        path4 = dest + "/" + key + "/" + new_file_name
                        
                        print("Moving" + new_file_name + "....")
                        shutil.move(path1,path4)
                        time.sleep(1)
                        
                    else:
                        print("Moving" + file_name + "....")
                        shutil.move(path1,path3)
                        time.sleep(1)
                
                else:
                    print("Making Directory....")
                    os.makedirs(path2)
                    print("Moving"+file_name+"....")
                    shutil.move(path1,path3)
                    time.sleep(1)

            
event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, source, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

