def shifr(text, shift):
    shifr_text = ''
    for i in text:
        if i.isalpha():
            start = ord('A') if i.isupper() else ord('a')
            shifr_char = chr((ord(i) - start + shift) % 26 + start)
            shifr_text += shifr_char
        else:
            shifr_text+=i
    return shifr_text

def rashifr(text, shift):
    rashifr_text = ''
    for i in text:
        if i.isalpha():
            start = ord('A') if i.isupper() else ord('a')
            rashifr = chr((ord(i) - start - shift) % 26 + start)
            rashifr_text += rashifr
        else:
            rashifr_text += i
    return rashifr_text

alphabet_of_exceptions = '.!?&*(|\/}]№;%:@#$%^* <>,-=~123456)_+{["7890'
ok = False
while ok == False:
        a1 = True
        a2 = True
        text = input('Введите текст: ')
        for i in text:
            if i == 'ё' or i == 'Ё':
                a1 = False
            if i not in alphabet_of_exceptions:
                if ord(i) < 1040 or ord(i) > 1103:
                    a2 = False
        if a1==False:
            print('Введите текст без буквы ё')
        elif a2==False:
            print('Введите текст на русском языке')
        else:
            ok = True
ok2 = False
while ok2 == False:
    shift = input('Введите шаг сдвига (целое число):')
    if isinstance(shift,int) and shift > 0:
        ok2 == True
    else:
        print('Шаг сдвига должен быть целым числом')

shifr_text = shifr(text, shift)
print('Зашифрованный текст:', shifr_text)
rashifr_text = rashifr(shifr_text, shift)
print('Расшифрованный текст:', text)