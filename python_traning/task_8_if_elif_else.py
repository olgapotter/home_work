num_float = 3.4

# Также попробуйте варианты
# num_float = 0
# num_float = -4.5

if num_float > 0:
   print('Положительное число')

elif num_float == 0:
   print('Ноль')
else:
   print('Число отрицательное')


def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
       print("Вы - бакалавар")
    elif year_of_study == 5 or year_of_study == 6:
       print("Вы - магистр")
    elif 7 <= year_of_study <= 9:
       print("Вы - аспирант")
    else:
       print("Введите корректный год обучения")

student_rank(6)