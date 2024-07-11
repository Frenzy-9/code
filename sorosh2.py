import time,subprocess,threading,os
#khali ya por o neshon bede? cancel vasate vorode etelaat? 

def check():
    while True:
        time.sleep(31)
        with open(...) as f:
            for xx in f.readlines():
                if time.strftime('%H:%M',time.localtime()) == xx.split(',')[2]:
                    subprocess.run(f'start {os.environ["HOME"]}\\Desktop\\alarm.mp3',\
                                   shell=True)
                
threading.Thread(target=check).start()            

liste = [[x,0,0,0] for x in range(1,15)]

while True:
    input('barname amade ast, dokme ENTER ra bezanid')
    while True:
        try:
            nafar = int(input('tedade nafar: '))
            break
        except ValueError:
            print('adad vared konid')

    qeym = (nafar-1)+40
    print(str(qeym)+' hezar toman har saat')

    while True:
        try:
            shom = int(input('shomare system: '))
            if 1>shom>14:
                print('adad beyne 1 va 14 bashad')
                continue
            break
        except ValueError:
            print('adad vared konid')

    while True:
        print('hour:minute')
        print('mesal: 2:45')
        zaman = input('saat dar samte rast : daqiqe dar samte chap')
        if zaman.isdecimal():
            zamsa, zamdaq = int(zaman), 0
            break
        elif len(zaman.split(':'))!=2 or not zaman.split(':')[0].isdecimal() or \
           not zaman.split(':')[1].isdecimal():
            continue
        else:
            zamsa, zamdaq = int(zaman.split(':')[0])*qeym,\
                            (int(zaman.split(':')[1])/60)*qeym
            break

    liste[shom-1][1] = time.strftime('%H:%M',time.localtime())
    liste[shom-1][2] = str(int(time.strftime('%H',time.localtime()))+zamsa)+':'\
                           str(int(time.strftime('%M',time.localtime()))+zamdaq)
    liste[shom-1][3] = (zamsa*qeym)+((zamdaq/60)*qeym)
    print('NEVESHTE SHOD   : )')
            
