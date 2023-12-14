## Pre-requisite

import glob
from moviepy.editor import VideoFileClip
import os  
import subprocess
import datetime
import re

def main():      
    process_video()
    print("done")

    
# def all_autorename():
#     """
#     This function will execute function auto_rename() from class Video on all mp4 files in the folder
#     """
#     mp4 = [file for file in glob.glob('*.mp4')]
#     for i in mp4:
#         clip = Video(i)     # instantiate class
#         clip.auto_rename()  #  call method
        
# def all_rotate():
#     """
#     1. This function will execute function rotate(self, degree: int) from class Video on all mp4 files in the folder
#     2. The rotate direction will follow the reverse of direction from filename
#     3. If not specified orientation, leave as is
#     """
#     mp4 = [file for file in glob.glob('*.mp4') if 'vr' in file.lower() or 'vl' in file.lower()]
#     for i in mp4:
#         clip = Video(i)     # instantiate class
#         clip.rotate()  #  call method
#         print(f"{clip.name} Rotated")
        
def process_video():
    """
    Perform all_rotate() and all_autorename() in one instance
    """
    mp4_files = [file for file in glob.glob('*.mp4')]

    for file in mp4_files:
        clip = Video(file)  # Instantiate class only once per file

        # Rotate video if it needs rotation
        if 'vr' in file.lower() or 'vl' in file.lower():
            clip.rotate()       # Call rotate method
            print(f"{clip.name} Rotated")

        # Rename video
        clip.auto_rename()  # Call auto_rename method

    print("All videos processed: rotation and renaming done")        
    
    
### Class for modifying each video
class Video:
    def __init__(self, filename):
        self.clip = VideoFileClip(filename)
        self.name = filename
        self.rawname = re.sub("vl|vr", "", filename, flags=re.IGNORECASE)
        self.folder = os.path.basename(os.getcwd())
#         self.fps = self.clip.fps
#         self.size = self.clip.size
#         self.width, self.height = self.size
        self.date = self.get_date() # Call the method to set the date
        self.orientation = self.determine_orientation()  # Call the method to set the orientation
        self.orientation_mini = re.match(r'(.*)_(.*)',self.orientation).group(1)
        
    ################ Methods for calling to Support Attribute ###############      
    
    def determine_orientation(self):
        """
        1. Determine video orientation from the file name (human will still have manually to lable it with "h" or "v")
        2. Vertical_Right is when the top of the video is on the right hand side of the video, and vice-versa for Vertical-Left
        
        """
        filename_lower = self.name.lower()
        if 'h' in filename_lower:
            return 'Horizontal_'
        elif 'vr' in filename_lower:
            return 'Vertical_Right'
        elif 'vl' in filename_lower:
            return 'Vertical_Left'
        elif 'v' in filename_lower:
            return 'Vertical_'         ## When didn't specify direction
        else:
            return ''
        
    def get_date(self):
        """
        get date meta data from file
        """
        # Get the time of last modification
        mod_time = os.path.getmtime(self.name)

        # Convert it to a datetime object
        date_obj = datetime.datetime.fromtimestamp(mod_time)

        # Format the date as YYYYMMDD
        formatted_date = date_obj.strftime('%Y-%m-%d')

        return f"{formatted_date}"
        
           
    def kill_ffmpeg(self):
        """
        For killing process, in case file is currently open and cannot be accessed with python
        """
        try:
            subprocess.run(['taskkill', '/f', '/im', 'ffmpeg-win64-v4.2.2.exe'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error killing ffmpeg: {e}")
        
        
        
    ################ Callable Methods ###############    
    def rotate(self):
        if self.orientation == 'Verticle_Right':
            degree = 90                                # 90 will rotate left
        elif self.orientation == 'Verticle_Left':
            degree = -90                               # -90 will rotate right
        else :
            degree = 0
        if degree is not 0 :
            rotated_clip = self.clip.rotate(degree)
            rotated_clip.write_videofile(self.name)  # replace original file
            self.kill_ffmpeg()
 
    def auto_rename(self):
            self.kill_ffmpeg()
            os.rename(self.name, f"{self.date}_{self.orientation_mini}_{self.rawname}")

        
if __name__ == "__main__":
    main()
