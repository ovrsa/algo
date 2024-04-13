import logging

# ロガーの設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# ログの出力先（ハンドラ）を標準出力に設定
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# ログのフォーマットを設定
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# ロガーにハンドラを追加
logger.addHandler(handler)