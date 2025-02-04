
#Матрица 7 Скала 5 4 Схватка Бэтман
films = input().split()
filmsum=0
filmsum1=0
for film in films:
    if film.isalpha():
        filmsum=filmsum+len(film)
        # print(film)
        # print(len(film))
        print(filmsum)
        # continue
    elif not film.isalpha():
        film=int(film)
        filmsum1+=film
        # print(film)
        print(filmsum1)

print(filmsum+filmsum1)
