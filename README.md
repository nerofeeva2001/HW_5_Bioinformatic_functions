# HW_5_Bioinformatic_functions
run_protein_tool
The following functions are implemented:
        
       -  `molecular_weight` This function takes 1-letter coded protein sequence(s) (string) and calculates molecular weight rounded to integer in g/mol. The function is not case-sensitive. 
        
        one_to_three_letter This function takes 1-letter coded protein sequence(s) (string) and returns a 3-letter coded sequence(s) without spaces (string). 
        
        amino_acid_frequency This function takes 1-letter coded protein sequence(s) (string), calculates frequency for each unique amino acid and creates a dictionary with amino acids as keys and corresponding frequencies as values. 
        
        find_motifs This function takes two string arguments: 1-letter coded protein sequence(s) and a motif of interest, where motif is any sequence which occurence will be searched for in the input protein sequence(s). The function returns position(s) of the       motif. If a motif was not found, the function will return an empty list. Please note that this function can only search for one motif at a time. 
        
утилиту для работы с fastq-последовательностями (по аналогии с ДЗ по ДНК/РНК и белкам). Главная функция принимает на вход 4 аргумента: `seqs`, `gc_bounds`, `length_bounds`, `quality_threshold`:
    -  `seqs` - словарь, состоящий из fastq-сиквенсов. Структура следующая. Ключ - строка, имя последовательности. Значение - кортеж из двух строк: последовательность и качество. По сути это содержание fastq-файла, но мы с вами пока не проходили чтение файлов. Так что пока используем python-словарь. Потом достаточно будет добавить чтение файлов и запись их в словарь такого вида, чтобы всё работало от начала и до конца. В скрипте `example_data.py` для вас сделан пример для отладки.
    - `gc_bounds` - интервал GC состава (в процентах) для фильтрации (по-умолчанию равен (0, 100), т. е. все риды сохраняются). Если в аргумент передать одно число, то считается, что это верхняя граница. Примеры: `gc_bounds = (20, 80)` - сохраняем только риды с GC составом от 20 до 80%, `gc_bounds = 44.4` - сохраняем риды с GC составом меньше, чем 44.4%.
    - `length_bounds` - интервал длины для фильтрации, всё аналогично `gc_bounds`, но по-умолчанию равен (0, 2**32).
    - `quality_threshold` - пороговое значение среднего качества рида для фильтрации, по-умолчанию равно 0 (шкала phred33). Риды со средним качеством по всем нуклеотидам ниже порогового отбрасываются. </br></br>
   
    **По итогам работы** главная функция должна возвращать аналогичный словарь, состоящий только из тех сиквенсов, которые прошли все условия. Все описанные интервалы включают и верхнюю, и нижнюю границы. Задание должно быть выполнено без использования сторонных модулей (стандартную библиотеку использовать можно). </br>
