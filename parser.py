from bs4 import BeautifulSoup
import requests
print('''
 _  _   __  __  __  __  ___  ____  ___    ____   __    ____  ___  ____  ____ 
( \/ ) (  \/  )(  )(  )/ __)(_  _)/ __)  (  _ \ /__\  (  _ \/ __)( ___)(  _ \
 \  /   )    (  )(__)( \__ \ _)(_( (__    )___//(__)\  )   /\__ \ )__)  )   /
 (__)()(_/\/\_)(______)(___/(____)\___)  (__) (__)(__)(_)\_)(___/(____)(_)\_)

''')
music_name = []
clean_music = []
artist_name = []
clean_artist = []
def get_html(url):
    result = requests.get(url)
    return result.text

def get_music(html):
    soup = BeautifulSoup(html, 'lxml')
    music_name = soup.findAll('a', class_='d-track__title deco-link deco-link_stronger')
    for i in range(len(music_name)):
        clean_music.append(music_name[i].text)
        
    for i in range(len(clean_music)):
        print(clean_music[i])

def get_artist(html):
    soup = BeautifulSoup(html, 'lxml')
    artist_name = soup.select('a[class=deco-link]')
    for y in range(len(artist_name)):
        clean_artist.append(artist_name[y].text)

    for y in range(len(clean_artist)):
        print(clean_artist)

def main():
    while True:
        url = input('введите пожалуйста url плейлиста. Обязательно сделайте его общедоступным в настройках! => ')
        save = input('сохранить вывод в файл? Да/Нет: ')
        yes = ['да', 'Да', 'yes', 'Yes', 'y', 'Y', 'д', 'Д']
        no = ['нет', 'Нет', 'no', 'No', 'n', 'N', 'н', 'Н']
        if save in yes:
            html = get_html(url)
            get_music(html)
            f = open('music.txt', 'w', encoding='utf8')
            music = (" - \n".join(clean_music))
            f.write(music)
            f.close()
            get_artist(html)
            f = open('artist.txt', 'w', encoding='utf8')
            artist = (" \n".join(clean_artist))
            f.write(artist)
            f.close()
            print('Запись в файл успешно завершена. Закрытие программы...')
            exit()
        elif save in no:
            html = get_html(url)
            get_music(html)
            get_artist(html)
            print('Закрытие программы...')
            exit()
        else:
            print('Введите корректные данные!')

if __name__ == '__main__':
    main()
