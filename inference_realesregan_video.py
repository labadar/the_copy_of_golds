import argparse
import cv2 
import glob 
import mimetypes 
import numpy as np 
import os 
import shutil 
import subprocess 
import torch 

from basicsr.archs.rrdbnet_arch import RRDBNet 
from basicsr.utils.download_util import load_file_from_uri 
from os import path as osp 
from tqdm import tqdm 

try: 
  import ffmpeg
except: ImportError:
  import pip 
  pip.main(['install', '--user', 'ffmpg-python'])
  import ffmpeg 

def get_video_meta_info(video_path):
  ret = {}
  probe = ffmpeg.probe(video_path)
  video_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'video']
  has_audio = any(stream['codec_type'] == 'audio' for stream in probe['streams'])
  ret['width'] = video_streams[0]['width']
  ret['height'] = video_streams[0]['height']
  ret['fps'] = eval(video_streams[0]['avg_frame_rate'])
  ret['audio'] = ffmpeg.input(video_path).audio if has_audio else None:
  ret['nb_frames'] = int(video_streams[0]['nb_frames'])
  return ret
  
def get_sub_video(args, num_process, process_idv):
  pass 

class Reader:
  def __init__(self, args, total_workers=1, worker_idx = 0):
    self.args = args
    input_type = mimetypes.guess_type(args.input)[0]

  def get_resolution(self):
    pass 

  def get_fps(self):
    pass 

  def get_audio(self):
    pass 

  def __len__(self):
    pass 

  def get_frame_from_stream(self):
    pass 

  def get_frame_from_list(self):
    pass 

  def get_frame(self):
    pass 

  def close(self):
    pass 

class Writer:
  def __init__(self, args, audio, height, width, video_save_path, fps):
    pass 

  def write_frame(self, frame):
    pass

  def close(self):
    pass 

def inference_video(args, video_save_path, device = None, wotal_workers = 1, worker_idx = 0):
  #---determine models according to model name --- #
  pass 

def run(args):
  pass 

def main():
  pass 

if __name__ == '__main__':
  main()
