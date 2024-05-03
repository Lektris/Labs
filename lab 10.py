#3.	Написати програму, яка вводить масив записів про мобільні телефони (виробник, модель, об’єм пам’яті, наявність ширококутної фотокамери, наявність NFC, ціна). Програма повинна знайти і вивести на екран дані про телефони фірми Motorola без ширококутної камери і з NFS.
phones_data = [
    {'manufacturer': 'Motorola', 'model': 'Moto G9', 'memory': '64', 'has_wide_camera': False, 'has_nfc': True, 'price': '250'},
    {'manufacturer': 'Samsung', 'model': 'Galaxy S20', 'memory': '128', 'has_wide_camera': True, 'has_nfc': True, 'price': '800'},
    {'manufacturer': 'Motorola', 'model': 'Moto E7', 'memory': '32', 'has_wide_camera': False, 'has_nfc': False, 'price': '150'},
    {'manufacturer': 'Apple', 'model': 'iPhone 12', 'memory': '256', 'has_wide_camera': True, 'has_nfc': True, 'price': '1000'}
]

def filter_phones(phones):
    filtered_phones = []
    for phone in phones:
        if phone['manufacturer'] == 'Motorola' and not phone['has_wide_camera'] and phone['has_nfc']:
            filtered_phones.append(phone)
    return filtered_phones

filtered_phones = filter_phones(phones_data)

print("Телефони фірми Motorola без ширококутної камери і з NFC:")
for phone in filtered_phones:
    print(f"\nВиробник: {phone['manufacturer']}, Модель: {phone['model']}, Ціна: {phone['price']}")
