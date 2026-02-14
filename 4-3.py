import re

def normalize_phone(phone_number):
    """
    Нормалізує номер телефону: залишає тільки цифри, 
    виправляє префікс та додає міжнародний код +38.
    """
    cleaned_number = re.sub(r'[^\d+]', '', phone_number.strip())
    
   
    if cleaned_number.startswith('+'):
       
        if not cleaned_number.startswith('+38'):
          
            pass
    elif cleaned_number.startswith('380'):
    
        cleaned_number = '+' + cleaned_number
    else:
        
        cleaned_number = '+38' + cleaned_number
        
    return cleaned_number

raw_phones = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

normalized_phones = [normalize_phone(p) for p in raw_phones]

print("Результати нормалізації:")
for original, result in zip(raw_phones, normalized_phones):
    print(f"{original.strip()}  =>  {result}")