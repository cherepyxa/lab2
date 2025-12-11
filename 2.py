import requests
class MyFile:
    def __init__(self, path_or_name, action):
        self.path_or_name = path_or_name
        self.action = action
        if self.action == "read": self.action = "r"
        elif self.action == "write": self.action = "w"
        elif self.action == "append": self.action = "a"

    def read(self):
        with open(self.path_or_name, self.action) as f:
            return f.read()

    def write(self, txt):
        with open(self.path_or_name, self.action) as f:
                return f.write(txt)
    
    def read_url(self):
         try:
            return requests.get(self.path_or_name).text
         except print("невозможно получить данные с страницы"):
                return "ошибка при запросе"
    
    def count_urls(self):
        cnt = 0
        a = requests.get(self.path_or_name).text
        b = a.split(" ")
        for i in b:
             if i[:4] == "href":
                  cnt += 1
        return cnt
    
    def write_url(self, txt2):
         try:
            content = requests.get(self.path_or_name).text
         except print("невозможно получить данные с страницы"):
                return "ошибка при запросе"
         with open(txt2, "w") as f:
                return f.write(content)

try:
    file = MyFile("text.txt", "read")
    text = file.read() # происходит чтение в виде str
    print(text)
except: print("неправильно переданы параметры в класс")

try:
    file = MyFile("text.txt", "write")
    text = file.write("привет!") # происходит запись строки в файл
except: print("неправильно переданы параметры в класс")

try:
    file = MyFile("text.txt", "append")
    text = file.write("привет!") # происходит добавление строки в конец файла
except: print("неправильно переданы параметры в класс")

try:
    # указали URL
    file = MyFile("https://ruz.spbstu.ru/faculty/125/groups/42684", "url")
    # и может читать содержимое страницы по указанному URL
    text = file.read_url() # происходит чтение в виде str
    print(text)
except: print("неправильный параметр url, либо ссылка, либо нет доступа к сайту")

try:
    count = file.count_urls()
    print(count)
except: print("не получилось посчитать ссылки")

try:
    file.write_url("text.txt")
except: print("нет такого txt")
