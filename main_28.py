# Тест скорости Интернета с использованием Python
# необходимо установить библиотеку Python, известную как  speedtest .
# pip install speedtest-cli

import speedtest  # библиотека для получения скорости проверки интернета

wifi = speedtest.Speedtest()  # инициализация объекта для получения скорости проверки интернета
print("Wifi Download Speed is ",
      wifi.download())  # вывод значения скорости проверки интернета
print("Wifi Upload Speed is ",
      wifi.upload())  # вывод значения скорости проверки интернета
