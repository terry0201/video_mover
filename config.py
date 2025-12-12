import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.FB_ACCESS_TOKEN = os.getenv('FB_ACCESS_TOKEN')
        self.FB_PAGE_ID = os.getenv('FB_PAGE_ID')
        self.DOWNLOAD_PATH = os.getenv('DOWNLOAD_PATH', './downloads')
        self.MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', '100')) * 1024 * 1024  # 100MB
    
    def validate(self):
        if not self.FB_ACCESS_TOKEN:
            raise ValueError("請設定 FB_ACCESS_TOKEN 環境變數")
        return True