import gradio as gr
from video_processor import VideoProcessor
import os

def process_video(youtube_url, fb_token):
    """處理影片搬運"""
    if not youtube_url:
        return "❌ 請輸入YouTube網址"
    
    if not fb_token:
        return "❌ 請設定Facebook Access Token"
    
    # 設定環境變數
    os.environ['FB_ACCESS_TOKEN'] = fb_token
    
    try:
        processor = VideoProcessor()
        result = processor.process_video(youtube_url)
        
        if result['success']:
            return f"✅ 成功上傳: {result['title']}\nFacebook影片ID: {result['video_id']}"
        else:
            return f"❌ 失敗: {result['error']}"
    except Exception as e:
        return f"❌ 錯誤: {str(e)}"

# 創建Gradio介面
with gr.Blocks(title="YouTube → Facebook Reels 搬運工具") as app:
    gr.Markdown("# 🎬 YouTube → Facebook Reels 搬運工具")
    
    with gr.Row():
        with gr.Column():
            youtube_url = gr.Textbox(
                label="🔗 YouTube影片網址",
                placeholder="https://www.youtube.com/watch?v=..."
            )
            
        with gr.Column():
            fb_token = gr.Textbox(
                label="Facebook Access Token",
                type="password"
            )
    
    submit_btn = gr.Button("🚀 開始搬運", variant="primary")
    output = gr.Textbox(label="結果", lines=3)
    
    submit_btn.click(
        fn=process_video,
        inputs=[youtube_url, fb_token],
        outputs=output
    )
    
    gr.Markdown("""
    ### 📖 使用說明
    1. 輸入YouTube影片網址
    2. 填入Facebook Access Token (需要 `user_videos`, `publish_video` 權限)
    3. 點擊「開始搬運」按鈕
    
    **注意事項:**
    - 影片大小限制: 100MB
    - 支援格式: MP4 (720p以下)
    - 需要Facebook頁面管理權限
    """)

if __name__ == "__main__":
    app.launch()