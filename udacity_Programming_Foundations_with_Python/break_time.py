
import time
import webbrowser

total_break = 3
break_count = 0

print("This program started on", time.ctime())
while break_count < total_break :
    time.sleep(5)
    webbrowser.open("http://www.uphone.co.kr/")
    break_count += 1
