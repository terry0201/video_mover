import json
import os
from video_processor import VideoProcessor

def lambda_handler(event, context):
    """AWS Lambda處理函數"""
    
    try:
        # 從event獲取YouTube URL
        youtube_url = event.get('youtube_url')
        if not youtube_url:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': '缺少youtube_url參數'})
            }
        
        # 處理影片
        processor = VideoProcessor()
        result = processor.process_video(youtube_url)
        
        if result['success']:
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': '影片上傳成功',
                    'video_id': result['video_id'],
                    'title': result['title']
                })
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': result['error']})
            }
            
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }