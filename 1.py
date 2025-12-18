import requests
import matplotlib.pyplot as plt
try:
    r = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat").text
except:
    print("сайт не найден, либо нет requests")

try:
    spis = r.split("\n")

    spis2 = list()
    x_coords = list()
    y_coords = list()
    summ = 0
    cnt = 0

    for i in spis:
        spis2.append(i.split(","))

    for i in spis2:
        if i[0] == "Средняя пенсия" and i[1] == "Забайкальский край" and i[2][:4] == "2018":
            print(i)
            summ += int(i[3])
            cnt += 1
            x_coords.append(i[2][5:])
            y_coords.append(i[3])
    print(summ/cnt)
    y = sorted(y_coords)
except:
    print("формат данных не подходит")
try:
    plt.plot(x_coords, y, alpha=0)
    plt.plot(x_coords, y_coords)
    plt.title("Средняя пенсия за 2018 год")
    plt.xlabel("Дата")
    plt.ylabel("Средняя пенсия")
    plt.grid(True)
    plt.show()
except:
    print("matplotlib.pyplot не установлен")
