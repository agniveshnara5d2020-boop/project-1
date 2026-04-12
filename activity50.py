try:
    number = int(input('Number:'))
    print('the number entered is',number)
except ValueError as ex:
    print('Exception:',ex)