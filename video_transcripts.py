# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:21:31 2020

@author: B Bartschi
"""

from youtube_transcript_api import YouTubeTranscriptApi

#transcript = YouTubeTranscriptApi.get_transcript("3FEKp4f7z8Q")
#
#print(transcript)


def find_clip_info_from_phrase(phrase):
    """
    Takes in a phrase and finds times within videos when words are said.
    
    Parameter:
        phrase (string): the input phrase to search for
        
    Returns:
        clip_info (set) : a set of tuples where each element is (video_file, (start_time, end_time))
    """
    
    
    return clip_info

def get_word_mapping_from_transcripts(youtube_ids):
    """
    Creates a dictionary mapping individual words to transcript phrases
    
    Parameter:
        youtube_ids (dict): maps video filenames to youtube IDs
    
    Returns:
        word_mapping (dict): keys are individual words that map to a a list of transcript phrase.
                             For example {'trajectory' : [{'video': 'lebron1.mp4', 'text': 'trajectory of his shot', 'start': 285.84, 'duration': 5.12}]}
    """
    word_mapping = {}
    
    return word_mapping