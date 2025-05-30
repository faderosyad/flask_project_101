from datetime import datetime, timedelta

def getTimestamp():
    nowDateTime = datetime.now() + timedelta(hours=7)
    formatDateTime = nowDateTime.strftime("%d-%m-%Y %H:%M:%S")
    return formatDateTime