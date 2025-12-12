# YouTube → Facebook Reels 搬運工具

自動將YouTube影片下載並上傳到Facebook Reels的Python工具，支援UI和CLI介面。

## 功能特色

- 🎬 YouTube影片自動下載
- 📱 上傳到Facebook Reels
- 🖥️ Gradio網頁UI介面
- ⌨️ 命令列CLI介面
- ☁️ 支援AWS Lambda部署

## 安裝

```bash
pip install -r requirements.txt
```

## 設定

### 1. 取得Facebook參數

**Facebook Access Token:**
1. 前往 [Facebook開發者平台](https://developers.facebook.com/)
2. 建立應用程式 → 選擇「其他」類型
3. 新增「Facebook登入」產品
4. 工具 → 存取權杖工具 → 產生使用者存取權杖
5. 選擇權限：`user_videos`, `publish_video`
6. 複製長期權杖

**注意事項:**
- 影片將上傳到你的個人 Facebook 帳號
- 不需要 Facebook 頁面 ID

### 2. 環境設定

1. 複製環境變數範例：
```bash
cp .env.example .env
```

2. 編輯 `.env` 文件，填入上述取得的參數：
```
FB_ACCESS_TOKEN=你的Facebook存取權杖
# FB_PAGE_ID=不需要(使用個人帳號)
```

## 使用方式

### UI介面
```bash
python ui.py
```

### CLI介面
```bash
python cli.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Lambda部署
將 `lambda_handler.py` 部署到AWS Lambda，事件格式：
```json
{
  "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

## 注意事項

- 影片大小限制：100MB
- 支援格式：MP4 (720p以下)
- 需要Facebook頁面管理權限
- 遵守YouTube和Facebook的使用條款
