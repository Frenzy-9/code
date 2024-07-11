import time,subprocess,threading,os
#khali ya por o neshon bede? cancel vasate vorode etelaat?

##pathe = os.environ['HOME']+'\\Desktop'
pathe = 'E:'

def check():
    while True:
        time.sleep(59.9988)
        with open(pathe+'\\moshtariha.txt') as f:
            for xx in f.readlines():
                mark = xx.find('payan')
                if time.strftime('%H:%M',time.localtime()) == xx[mark+6:mark+6+5]:
                    subprocess.run(pathe+'\\alarm.mp3',shell=True)
##                if time.strftime('%H:%M',time.localtime()) == xx.split(',')[2]:
##                    subprocess.run(pathe+'\\alarm.mp3',shell=True)
                
threading.Thread(target=check).start()            

liste = [{'system':str(x),'shoro':'','payan':'','gheymat':'','tedad':''} for x in range(1,15)]

while True:
    input('barname amade ast, dokme ENTER ra bezanid')
    while True:
        try:
            nafar = int(input('tedade nafar: '))
            if 1>nafar or nafar>4:
                print('tedade afrad az 1 ta 4 ast')
                continue
            break
        except ValueError:
            print('adad vared konid')

    qeym = ((nafar-1)*10)+40
    print(str(qeym)+' hezar toman har saat')

    while True:
        try:
            shom = int(input('shomare system: '))
            if 1>shom or shom>14:
                print('adad beyne 1 va 14 bashad')
                continue
##            if liste[shom-1]['payan']:
##                hou2,min2 = liste[shom-1]['payan'].split(':')
##                if int(hou2)>int(time.strftime('%H',time.locltime())) or int(min2)>int(time.strftime('%M',time.localtime())):
##                    print('eshqal ast?')
            break
        except ValueError:
            print('adad vared konid')

    while True:
        print('hour:minute')
        print('mesal: 2:45')
        print('mesale 2: nim saat -> 0:30')
        zaman = input('saat dar samte rast : daqiqe dar samte chap')
        if zaman.isdecimal():
            zamsa, zamdaq = int(zaman), 0
            break
        elif len(zaman.split(':'))!=2 or not zaman.split(':')[0].isdecimal() or \
           not zaman.split(':')[1].isdecimal():
            continue
        else:
            zamsa, zamdaq = int(zaman.split(':')[0]),\
                            int(zaman.split(':')[1])
            break

    liste[shom-1]['shoro'] = time.strftime('%H:%M',time.localtime())
    liste[shom-1]['payan'] = str(int(time.strftime('%H',time.localtime()))+zamsa)+':'\
                            +str(int(time.strftime('%M',time.localtime()))+zamdaq)
    timeh, timem = liste[shom-1]['payan'].split(':')
    if int(timem) > 59:
        liste[shom-1]['payan'] = str(int(timeh)+1) + ':' + str(int(timem)-60)
    timeh, timem = liste[shom-1]['payan'].split(':')
    if int(timeh) > 23:
        liste[shom-1]['payan'] = f'0{int(timeh)-24}:'+timem
    timeh, timem = liste[shom-1]['payan'].split(':')
        
    if len(timeh)==1:
        liste[shom-1]['payan'] = '0'+timeh+':'+timem
    timeh, timem = liste[shom-1]['payan'].split(':')
    if len(timem)==1:
        liste[shom-1]['payan'] = timeh + ':0' + timem

    liste[shom-1]['gheymat'] = str((zamsa*qeym)+((zamdaq/60)*qeym))
    liste[shom-1]['tedad'] = str(nafar)
        
            
    with open(pathe+'\\moshtariha.txt','w') as f:
        for ab in liste:
            for ac in ab.items():
                f.write(':'.join(ac))
                f.write(', ')
            f.write('\n\n')

    print('~ NEVESHTE SHOD VA SABT GARDID ~\ ')

    #
    #print(liste)
    #
