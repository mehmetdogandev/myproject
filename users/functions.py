def buyuk_harf_var_mi(text):
    for char in text:
        if char.isupper():
            return True
    return False

def kucuk_harf_var_mi(text):
    for char in text:
        if char.islower():
            return True
    return False

def ozel_karakter_var_mi(text):
    for char in text:
        if not char.isalnum():  # isalnum() metodu harf veya rakam içermeyen karakterler için True döndürür
            return True
    return False
