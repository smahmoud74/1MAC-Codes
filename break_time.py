import time
import webbrowser

total_break = 3
break_count = 0
print ("This program strted on "+time.ctime())
while(break_count < total_break):
    time.sleep(35*60)
    webbrowser.open("https://www.youtube.com/watch?v=N8luX4QjJvo")
    break_count = break_count + 1
