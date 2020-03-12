def convert(number):
    sound = ''
    sound1 = 'Pling'
    sound2 = 'Plang'
    sound3 = 'Plong'
    if number % 3 == 0:
            sound = sound+sound1
        
    if number % 5 == 0:
            sound = sound+sound2
        
    if number % 7 == 0:
            sound = sound+sound3
        
    if len(sound)== 0:   
        sound = str(number)

    return sound
