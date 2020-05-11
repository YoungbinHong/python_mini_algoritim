import time
import datetime

f = open('Body_weight_record.txt',mode='a',encoding='utf-8')
body_weight = float()
fluctation = float()

mod = input("If you want to input new data, press n\nIf you modify your old data please press m\n").lower()
if mod == 'n':
    body_weight = input("Please input your today's new body weight : ")
    f.write(f'{datetime.date.today()} : {body_weight} Kg\n')
    f.write(f'Fluctation : ')
    
f.close()
time.sleep(10)