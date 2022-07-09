import pyautogui as auto
import time

print("MCT OwO Bot | 5 Saniye Sonra Aktif Edilecektir.")
print("----------------------------------------------------")
print("Developer > Athenax#8928 ")
print("----------------------------------------------------")
print("Bu Bot Python İle Geliştirilmiştir.")
time.sleep(5)
x=0
while True:
    auto.write("owo hunt")
    auto.press("Enter")
    time.sleep(4)
    auto.write("owo battle")
    auto.press("Enter")
    time.sleep(15)
    x+=1
    if x == 4:
        x=0
        auto.write("MCT OwO Bot | 1 Dakikalıgına Durdurulmustur!")
        auto.press("Enter")
        time.sleep(60)
        auto.write("MCT OwO Bot | Yeniden Baslatılmıstır!")
        auto.press("Enter")