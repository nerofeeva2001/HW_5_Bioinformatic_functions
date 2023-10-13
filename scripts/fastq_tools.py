# Функция для подсчета GC состава рида
def gc_content(read):
    gc_count = 0
    for base in read:
        if base in "GCgc":
            gc_count += 1
    return gc_count / len(read) * 100

# Функция для подсчета среднего качества рида по шкале phred33
def mean_quality(quality):
    total_score = 0
    for char in quality:
        score = ord(char) - 33  # преобразуем символ в ASCII код и вычитаем 33
        total_score += score
    return total_score / len(quality)

# Функция для фильтрации ридов по GC составу
def gc_bounds_filter(seqs, gc_bounds=(0, 100)):
    filtered_seqs = {}  # пустой словарь для отфильтрованных ридов
    # Если в аргумент передано одно число, то считаем, что это верхняя граница
    if isinstance(gc_bounds, (int, float)):
        gc_bounds = (0, gc_bounds)
    for name, (read, quality) in seqs.items():
        # Подсчет GC состава и среднего качества для каждого рида
        current_gc_content = gc_content(read)
        current_mean_quality = mean_quality(quality)
        # Проверяем, что рид удовлетворяет условию по GC составу
        if gc_bounds[0] <= current_gc_content <= gc_bounds[1]:
            # Добавляем рид в словарь отфильтрованных ридов
            filtered_seqs[name] = (read, quality)
    return filtered_seqs  # Возвращаем словарь отфильтрованных ридов

# Функция для фильтрации ридов по длине
def length_bounds_filter(seqs, length_bounds=(0, 2**32)):
    filtered_seqs = {}  # пустой словарь для отфильтрованных ридов
    # Если в аргумент передано одно число, то считаем, что это верхняя граница
    if isinstance(length_bounds, (int, float)):
        length_bounds = (0, length_bounds)
    for name, (read, quality) in seqs.items():
        # Проверяем, что рид удовлетворяет условию по длине
        if length_bounds[0] <= len(read) <= length_bounds[1]:
            # Добавляем рид в словарь отфильтрованных ридов
            filtered_seqs[name] = (read, quality)
    return filtered_seqs  # Возвращаем словарь отфильтрованных ридов

# Функция для фильтрации ридов по среднему качеству
def quality_threshold_filter(seqs, quality_threshold=0):
    filtered_seqs = {}  # пустой словарь для отфильтрованных ридов
    for name, (read, quality) in seqs.items():
        # Проверяем, что рид удовлетворяет условию по среднему качеству
        if mean_quality(quality) >= quality_threshold:
            # Добавляем рид в словарь отфильтрованных ридов
            filtered_seqs[name] = (read, quality)
    return filtered_seqs  # Возвращаем словарь отфильтрованных ридов

# Главная функция для фильтрации ридов по заданным условиям
def filter_reads(seqs, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0):
    # Применяем все три функции фильтрации последовательно к словарю seqs
    seqs = gc_bounds_filter(seqs, gc_bounds)
    seqs = length_bounds_filter(seqs, length_bounds)
    seqs = quality_threshold_filter(seqs, quality_threshold)
    return seqs  # Возвращаем итоговый словарь отфильтрованных ридов

