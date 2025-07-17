AUTHOR = 'KEHUEISIN'
SITEURL = ""

PATH = "content"
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = 'zh'

# --- 頁面路徑設定 ---
PAGE_PATHS = ['']  # 直接放在 content 根目錄的 .md 都會被當作頁面
ARTICLE_PATHS = []  # 沒有部落格文章功能，設空，避免混淆

# --- 靜態檔案（圖片等） ---
STATIC_PATHS = ['images']  # 你只有 images 這個資料夾，其他移除

# --- 處理 HTML 當作靜態內容，不渲染 ---
READERS = {
    'html': None,
}

# --- 網址輸出方式（讓 slug.html 變成網址） ---
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# --- 禁用首頁文章列表，避免 index.html 重複 ---
INDEX_SAVE_AS = ''

# --- 顯示自訂選單 ---
MENUITEMS = [
    ('首頁', '/home.html'),
    ('執行範例', '/run.html'),
    ('關於', '/about.html'),
]

# --- 主題選單自動列出頁面（若主題支援） ---
DISPLAY_PAGES_ON_MENU = True

# --- 關閉 RSS ---
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
