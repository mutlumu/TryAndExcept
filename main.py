try:
    number = int(input("Bir sayi giriniz"))

except ValueError:
    print("Lütfen bir sayı giriniz")
    number = int(input("Bir sayi giriniz"))
    print(number)
