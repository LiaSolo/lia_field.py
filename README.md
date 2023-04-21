Библиотека Field - для работы с конечными полями, где $p^n$ элементов, где p - простое число, n - натуральное число > 1. 
Возможны операции сложения, вычетания, умножения, деления, взятия противоположного (по сложению) и обратного (по умножению).  

Библиотека SimpleField предназначена для выполнения того же функционала, но с полями, где n = 1.  

Если p = 2, то есть возможность преобразовывать байты в элементы поля and vice versa.  

В случае работы с библиотекой Field нужно так же указывать неприводимый многочлен над полем из p элементов.  

Элементы поля $F_{p^n}$ представляют из себя число (n = 1) или массив чисел (n > 1), натуральных + {0}, не превосходящих p.  

Вся ответвенность в правильном вводе лежит на пользователе. 

Добавлена возможность генерировать псевдослучайные байты на основе ЛРП. 
Для этого необходимо ввести набор коэффициентов и свободный член из $F_{256}$ в формате $\[ x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8 \]$,
где $x_i \in$ {0, 1}.
