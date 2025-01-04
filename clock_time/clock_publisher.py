# clock_publisher.py

import time

def get_time_message():
    # 現在のエポックタイム（秒単位）を取得して、必ずfloat型に変換
    epoch_time = float(time.time())
    
    # メッセージを返す
    message = {"epoch_time": epoch_time}

    return message
