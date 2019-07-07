import re

vodacom = re.compile(r'(76)(\d\d\d)(\d\d\d\d)')
vodacom2 = re.compile(r'(75)(\d\d\d)(\d\d\d\d)')

tigo = re.compile(r'(71)(\d\d\d)(\d\d\d\d)')
tigo2 = re.compile(r'(65)(\d\d\d)(\d\d\d\d)')

airtel = re.compile(r'(78)(\d\d\d)(\d\d\d\d)')
airtel2 = re.compile(r'(68)(\d\d\d)(\d\d\d\d)')

halotel = re.compile(r'(62)(\d\d\d)(\d\d\d\d)')

ttcl = re.compile(r'(73)(\d\d\d)(\d\d\d\d)')


def checkNumber(input_number_check):
    global tigo
    global airtel
    global vodacom
    global vodacom2
    global airtel2
    global tigo2
    global halotel
    global ttcl
    
    vod = vodacom.search(input_number_check)
    vod2 = vodacom2.search(input_number_check)
    tig = tigo.search(input_number_check) 
    tig2 = tigo2.search(input_number_check)
    air =airtel.search(input_number_check)
    air2 =airtel2.search(input_number_check)
    halo = halotel.search(input_number_check)
    ttc = ttcl.search(input_number_check)
    if air == tig and tig ==vod and air == vod and air2 == vod2 and vod2 == tig2 and tig2 == air2 and ttc ==halo:
        return 'No match'
        
    if  vod is not None:
        return 'Your number is Vodacom'
    elif vod2 is not None:
        return 'Your number is Vodacom'
    elif tig is not None:
        return 'Your number is tigo'
    elif tig2 is not None:
        return 'Your number is tigo'
    elif  air is not None:
        return 'your number is airtel'
    elif air2 is not None:
        return 'Your number is airtel'
    elif halo is not None:
        return 'Your number is halotel'
    elif ttc is not None:
        return 'Your number is ttcl'
    else:
        return 'your number does not match any of my data'
while True:
    try:
        input_number = input("Enter the number or nothing to end the program: +255 ")
    except Exception:
        break
        
    if str(input_number) == '':
        break
    elif len(str(input_number)) >9:
        print('Your phone number is too long')
        continue
    elif len(str(input_number)) < 9:
        print('Your phone number is too short')
        continue
    else:    
        try:
            print(checkNumber(str(input_number)))
        except Exception:
            print('You have entered invalid data')
