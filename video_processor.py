import os
import yt_dlp
import requests
from pathlib import Path
from config import Config

class VideoProcessor:
    def __init__(self):
        self.config = Config()
        os.makedirs(self.config.DOWNLOAD_PATH, exist_ok=True)
    
    def download_youtube_video(self, url):
        """下載YouTube影片"""
        ydl_opts = {
            'format': 'best[height<=720][ext=mp4]',
            'outtmpl': f'{self.config.DOWNLOAD_PATH}/%(title)s.%(ext)s',
            'noplaylist': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return filename, info.get('title', ''), info.get('description', '')
    
    def upload_to_facebook(self, video_path, title, description=""):
        """上傳影片到Facebook"""
        self.config.validate()
        
        # 檢查檔案大小
        if os.path.getsize(video_path) > self.config.MAX_FILE_SIZE:
            raise ValueError(f"檔案大小超過限制 ({self.config.MAX_FILE_SIZE/1024/1024}MB)")
        
        # 使用用戶個人帳號上傳影片
        upload_url = "https://graph-video.facebook.com/v18.0/me/videos"
        
        with open(video_path, 'rb') as video_file:
            files = {'source': video_file}
            data = {
                'access_token': self.config.FB_ACCESS_TOKEN,
                'description': f"{title}\n\n{description}"[:2200],
                'published': 'false'
            }
            
            response = requests.post(upload_url, files=files, data=data)
            
        if response.status_code == 200:
            video_data = response.json()
            video_id = video_data.get('id')
            
            # 發佈影片
            publish_url = f"https://graph.facebook.com/v18.0/{video_id}"
            publish_data = {
                'access_token': self.config.FB_ACCESS_TOKEN,
                'published': 'true'
            }
            
            publish_response = requests.post(publish_url, data=publish_data)
            
            if publish_response.status_code == 200:
                return {'id': video_id, 'published': True}
            else:
                return {'id': video_id, 'published': False}
        else:
            raise Exception(f"上傳失敗: {response.text}")
    
    def process_video(self, youtube_url):
        """完整處理流程"""
        try:
            # 下載影片
            video_path, title, description = self.download_youtube_video(youtube_url)
            
            # 上傳到Facebook
            result = self.upload_to_facebook(video_path, title, description)
            
            # 清理檔案
            os.remove(video_path)
            
            return {
                'success': True,
                'video_id': result.get('id'),
                'title': title
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }