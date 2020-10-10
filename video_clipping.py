# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:10:17 2020

@author: B Bartschi
"""

from moviepy.editor import *


#clip = VideoFileClip(source_path)
#all_clips = []
#for i in range(10):  
#    new_clip = clip.subclip(i*10,i*10+2)
#    all_clips.append(new_clip)
#    
#    
#final_clip = concatenate_videoclips(all_clips)
#final_clip.write_videofile(output_path, codec='libx264', audio_codec="aac")



def create_final_clip(time_mappings):
    """
    Uses time_mappings to select subclips from input videos and create a 
    final concatenated video.
    
    Parameters:
        time_mappings (set): a set of tuples where each element is (video_file, (start_time, end_time))
        
    Return:
        VideoFileClip: represents all desired subclips concatenated
    """
    
    
    return final_clip