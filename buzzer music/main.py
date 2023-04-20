import pitch
from time import sleep

mel = {
    1: {
        'st':
        'pagal ye pagle vo pagle kr de',
        'no': [GS4, GS4, F4, DS4, DS4, F4, GS4, GS4, F4, D4],
        'ti': [
            
        ]
    },
    2: {
        'st': 'jaha bhi ye jaye',
        'no': [F4, DS4, GS4, G4, F4, DS4, C4],
        'ti': []
    },
    3: {
        'st':
        'dekho karta hai kase dewana sabko',
        'no':
        [F4, F4, F4, F4, F4, F4, F4, G4, G4, F4, G4, GS4],
        'ti': []
    },
    4: {
        'st': 'mera nam hi shinchan hai',
        'no': [C4, CS4, DS4, C4, C4, GS4, F4],
        'ti': []
    },
    5: {
        'st': 'mai sharat se bhara',
        'no': [CS4, DS4, F4, CS4, C4, F4, DS4],
        'ti': []
    },
    6: {
        'st': 'badi muskhil mai padi',
        'no': [C4, CS4, DS4, C4, C4, GS4, F4],
        'ti': []
    },
    7: {
        'st': 'meri family nohara',
        'no': [CS4, DS4, F4, DS4, CS4, G4, F4, DS4],
        'ti': []
    },
    8: {
        'st': 'come on baby come on baby',
        'no': [F4, GS4, AS4, GS4, F4, GS4, AS4, GS4],
        'ti': []
    },
    9: {
        'st': ' ao kre dance shuru',
        'no': [DS4, DS4, DS4, DS4, F4, DS4],
        'ti': []
    },
    10: {
        'st': 'zoro se ghume hum tum jhume',
        'no': [F4, GS4, GS4, AS4, GS4, F4, GS4, AS4, GS4],
        'ti': []
    },
    11: {
        'st': 'dekho sabko hila du',
        'no': [DS4, DS4, F4, F4, G4, GS4, AS4],
        'ti': []
    },
    12: {
        'st': 'kabhi ye oochalta hai',
        'no': [GS4, GS4, F4, F4, DS4, DS4, F4],
        'ti': []
    },
    13: {
        'st': 'kabhi ye machalta hai',
        'no': [GS4, GS4, F4, F4, DS4, DS4, F4],
        'ti': []
    },
    14: {
        'st': 'har dam beqabu',
        'no': [GS4, G4, F4, DS4, C4],
        'ti': []
    },
    15: {
        'st': 'roz ye karta hai nai nai gadbad',
        'no': [AS4, GS4, F4, F4, GS4, AS4, GS4, F4, GS4],
        'ti': []
    },
    16: {
        'st': 'tumoko hasa dega shinchan',
        'no': [DS4, DS4, DS4, DS4, F4, G4, AS4, GS4],
        'ti': []
    }
}

for i in range(1, 18):
    if i == 17:
        buzz.duty(0)
        break
    print(mel[i]['st'])
    # for j, k in zip(mel[i]['no'], mel[i]['ti']):
    #     if j == 0:
    #         buzz.duty(0)
    #     else:
    #         buzz.freq(j)
    #         buzz.duty(50)
    #     print('This is the freq: ', j, ' and this is the pause: ', k)
    #     sleep(k)
        
    for j in mel[i]['no']:
        buzz.freq(j)
        buzz.duty(10)
        print('This is the freq: ', j)
        sleep(0.13)
        buzz.duty(0)
        sleep(0.07)
