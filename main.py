# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:24:12 2020

@author: Benjamin Bartschi

"""
import os
from config import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import video_transcripts
import video_clipping

output_filename = "phrase"
output_path = os.path.join(SAMPLE_OUTPUTS, output_filename + ".mp4" )

# TODO: populate youtube_ids dictionary mapping filename -> youtube ID
YOUTUBE_IDS = {"lebron1.mp4":"3FEKp4f7z8Q",
               "vanvleet1.mp4":"6q4NBAvru3c",
               "giannis1.mp4":"RxvA3ZEsrU8",
               "lebron2.mp4":"8ZrHJtYRhv0",
               "zion1.mp4":"3VQaPayG6zc",
               "kawhi1.mp4":"Ywhj4zlKHJE",
               "durant1.mp4":"MN5YnVlDnIQ",
               "family1.mp4":"0fnGeIl2BCM",
               "butler1.mp4":"TO6RgM_pIN0",
               "funny1.mp4":"PBjwjHeyyyM",
               "funny2.mp4":"5pieLIlPgWY",
               "funny3.mp4":"5VecZkE1onQ",
               }

word_mapping = video_transcripts.get_word_mapping_from_transcripts(YOUTUBE_IDS)

# Use to constrain clip search
specified_versions = [120,1,1]
use_random_version = True

clip_info, specifieds = video_transcripts.find_clip_info_from_phrase("and and and and " , word_mapping, use_random_version, specified_versions)

print(specifieds)

# Use to post-process clip compositing
use_offsets = False
offsets = []
final_clip = video_clipping.create_final_clip(clip_info, use_offsets, offsets)

final_clip.write_videofile(output_path, codec='libx264', audio_codec="aac")