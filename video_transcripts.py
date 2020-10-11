# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:21:31 2020

@author: B Bartschi
"""

from youtube_transcript_api import YouTubeTranscriptApi
import random 

def find_clip_info_from_phrase(phrase, word_mapping, use_random_version=True, specified_versions=[]):
    """
    Takes in a phrase and finds times within videos when words are said.
    
    Parameter:
        phrase (string): the input phrase to search for
        word_mapping (dict): keys are individual words that map to a a list of transcript phrase.
                             For example {'trajectory' : [{'video': 'lebron1.mp4', 'text': 'trajectory of his shot', 'start': 285.84, 'duration': 5.12}]}
        use_random_version (boolean): specifies if a random clip should be chosen for multiple of the same word
        specified_versions (list): index of each clip when there are multiple of the same word   
        
    Returns:
        clip_info (list) : a list of tuples where each element is (video_file, (start_time, end_time))
        specifieds (list): index of each clip chosen there are multiple of the same word   
    """
    clip_info = []
    
    if use_random_version: 
        specifieds = []
    else:
        specifieds = specified_versions
        
    count = 0
    for word in phrase.split():
        assert word in word_mapping, word + " is not contained in the given videos"
        if (use_random_version):
            version_index = random.randint(0,len(word_mapping[word])-1)
            specifieds.append(version_index)
        else:
            version_index = specified_versions[count]
            
        entry = word_mapping[word][version_index]
        clip_info.append( (entry['video'],(entry['start'],entry['duration'])) )
        count += 1
        
    return clip_info, specifieds

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
    
    for filename, ID in youtube_ids.items():
        current_transcript = YouTubeTranscriptApi.get_transcript(ID)
        for phrase in current_transcript:
            for word in set(phrase['text'].split()):
                if word in word_mapping.keys():
                    new_phrase = {'video':filename, 'text':phrase['text'], 'start':phrase['start'], 'duration':phrase['duration']}
                    word_mapping[word].append(new_phrase)
                else:
                    word_mapping[word] = [{'video':filename, 'text':phrase['text'], 'start':phrase['start'], 'duration':phrase['duration']}]
    
    return word_mapping

