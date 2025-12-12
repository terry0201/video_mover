#!/usr/bin/env python3
import click
from video_processor import VideoProcessor

@click.command()
@click.argument('youtube_url')
@click.option('--verbose', '-v', is_flag=True, help='顯示詳細輸出')
def main(youtube_url, verbose):
    """YouTube影片搬運到Facebook Reels CLI工具"""
    
    if verbose:
        click.echo(f"處理影片: {youtube_url}")
    
    processor = VideoProcessor()
    
    try:
        result = processor.process_video(youtube_url)
        
        if result['success']:
            click.echo(f"✅ 成功上傳: {result['title']}")
            if verbose:
                click.echo(f"Facebook影片ID: {result['video_id']}")
        else:
            click.echo(f"❌ 失敗: {result['error']}")
            
    except Exception as e:
        click.echo(f"❌ 錯誤: {str(e)}")

if __name__ == '__main__':
    main()