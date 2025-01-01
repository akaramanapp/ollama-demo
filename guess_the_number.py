import random

def guess_the_number():
    secret_number = random.randint(1, 10)
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 10 arasında bir sayı tutuldu. Tahmin etmeye çalışın.")
    
    attempts = 0
    
    while True:
        try:
            guess = int(input("Tahmininizi yapın: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Tebrikler! Doğru tahmin ettiniz. {secret_number} sayısı bildiniz.")
                print(f"Toplam denemeniz {attempts} oldu.")
                break
            elif guess < secret_number:
                print("Daha büyük bir sayı deneyin.")
            else:
                print("Daha küçük bir sayı deneyin.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    guess_the_number()