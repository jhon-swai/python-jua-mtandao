import re
vodacom = re.compile(r'(76)(\d\d\d)(\d\d\d\d) | (75)(\d\d\d)(\d\d\d\d)')
tigo = re.compile(r'(71)(\d\d\d)(\d\d\d\d) | (65)(\d\d\d)(\d\d\d\d)')
airtel = re.compile(r'(78)(\d\d\d)(\d\d\d\d) | (68)(\d\d\d)(\d\d\d\d)')
input_number = input("Enter the number: +255 ")
def checkNumber(input_number_check):
    global tigo
    global airtel
    global vodacom
    vod = vodacom.search(input_number_check)
    tig = tigo.search(input_number_check) 
    air =airtel.search(input_number_check)
    if air == tig and tig ==vod and air == vod:
        #This means all the results are None
        return 'Failed'
        
    if vod is not None:
        return 'Your number is Vodacom'
    elif tig is not None:
        return 'Your number is tigo'
    elif  air is not None:
        return 'your number is airtel'
    else:
        return 'your number does not match any of my data'

print(checkNumber(str(input_number)))
