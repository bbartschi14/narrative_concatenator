# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:10:17 2020

@author: B Bartschi
"""

from moviepy.editor import *
from config import SAMPLE_INPUTS
import os


def create_final_clip(time_mappings, use_offsets=False, offsets=[]):
    """
    Uses time_mappings to select subclips from input videos and create a 
    final concatenated video.
    
    Parameters:
        time_mappings (list): a list of tuples where each element is (video_file, (start_time, end_time))
        use_offsets (boolean): defines if offsets should be used
        offsets (list): tuples (start_offset, end_offset) defining user-specified trimming
        
    Return:
        final_clip (VideoFileClip): represents all desired subclips concatenated
    """
    all_clips = []
    
    count = 0
    for mapping in time_mappings:
        source_path = os.path.join(SAMPLE_INPUTS, mapping[0])
        start = mapping[1][0]
        end = mapping[1][0] + mapping[1][1]  
        if use_offsets:
            start += offsets[count][0]
            end -= offsets[count][1]
        new_clip = VideoFileClip(source_path).subclip(start, end)
        
        all_clips.append(new_clip)
        count += 1
        
    final_clip = concatenate_videoclips(all_clips)
    return final_clip