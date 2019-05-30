# fanqaich makes number file
# i read file
# i set the file's data as a variable
# i rewrite the file as 0
# i start the timer in this window
import time
import os

f = open('C:/Aura/sys/text/ms.txt', 'r')
unit = f.readline()
f.close
f = open('C:/Aura/sys/text/timer.txt', 'r')
data = f.readline()
f.close()

# multi = multiplier for conversion
if unit == 'sec':
    multi = 1
elif unit == 'min':
    multi = 60
elif unit == 'hour':
    multi = 3600

nums = []
for char in data:
    if char.isdigit() is True:
        nums.extend(char)
    else:
        useless = 0
        
num = float(''.join(nums))
num = (num*multi)
count = 1
while count <= num:
    print(count)
    time.sleep(1)
    count = count + 1

os.startfile('C:/Aura/sys/sounds/alarm.mp3')
time.sleep(20)
os.system('TASKKILL /F /IM wmplayer.exe')
print("TIME UP")
f = open('C:/Aura/sys/text/timer.txt', 'w')
f.write('')
f.close()
f = open('C:/Aura/sys/text/ms.txt', 'w')
f.write('')
f.close()
a = input("")


