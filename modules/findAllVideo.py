import requests

def findAllVideo(date):
    data_to_send = {
        "date": str(date)
    }

    return requests.post("http://127.0.0.1:8000/video", json=data_to_send).json()
