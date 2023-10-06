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
        score = ord(char) - 33 # преобразуем символ в ASCII код и вычитаем 33
        total_score += score
    return total_score / len(quality)

# Функция для фильтрации ридов по GC составу
def gc_bounds_filter(seqs, gc_bounds=(0, 100)):
    filtered_seqs = {
    # 'name' : ('sequence', 'quality')
    '@SRX079804:1:SRR292678:1:1101:21885:21885': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
    '@SRX079804:1:SRR292678:1:1101:24563:24563': ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D'),
    '@SRX079804:1:SRR292678:1:1101:30161:30161': ('GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTCTTTAGCGTTGTGCAAAGCATGTTTTGTATTACGGGCATCTCGAGCGAATC', 'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFBGGG?DE=:6@=>A<A>D?D8DCEE:>EEABE5D@5:DDCA;EEE-DCD'),
    '@SRX079804:1:SRR292678:1:1101:47176:47176': ('TGAAGCGTCGATAGAAGTTAGCAAACCCGCGGAACTTCCGTACATCAGACACATTCCGGGGGGTGGGCCAATCCATGATGCCTTTG', 'FF@FFBEEEEFFEFFD@EDEFFB=DFEEFFFE8FFE8EEDBFDFEEBE+E<C<C@FFFFF;;338<??D:@=DD:8DDDD@EE?EB'),
    '@SRX079804:1:SRR292678:1:1101:149302:149302': ('TAGGGTTGTATTTGCAGATCCATGGCATGCCAAAAAGAACATCGTCCCGTCCAATATCTGCAACATACCAGTTGGTTGGTA', '@;CBA=:@;@DBDCDEEE/EEEEEEF@>FBEEB=EFA>EEBD=DAEEEEB9)99>B99BC)@,@<9CDD=C,5;B::?@;A'),
    '@SRX079804:1:SRR292678:1:1101:170868:170868': ('CTGCCGAGACTGTTCTCAGACATGGAAAGCTCGATTCGCATACACTCGCTGAGTAAGAGAGTCACACCAAATCACAGATT', 'E;FFFEGFGIGGFBG;C6D<@C7CDGFEFGFHDFEHHHBBHHFDFEFBAEEEEDE@A2=DA:??C3<BCA7@DCDEG*EB'),
    '@SRX079804:1:SRR292678:1:1101:171075:171075': ('CATTATAGTAATACGGAAGATGACTTGCTGTTATCATTACAGCTCCATCGCATGAATAATTCTCTAATATAGTTGTCAT', 'HGHHHHGFHHHHFHHEHHHHFGEHFGFGGGHHEEGHHEEHBHHFGDDECEGGGEFGF<FGGIIGEBGDFFFGFFGGFGF'),
    '@SRX079804:1:SRR292678:1:1101:175500:175500': ('GACGCCGTGGCTGCACTATTTGAGGCACCTGTCCTCGAAGGGAAGTTCATCTCGACGCGTGTCACTATGACATGAATG', 'GGGGGFFCFEEEFFDGFBGGGA5DG@5DDCBDDE=GFADDFF5BE49<<<BDD?CE<A<8:59;@C.C9CECBAC=DE'),
    '@SRX079804:1:SRR292678:1:1101:190136:190136': ('GAACCTTCTTTAATTTATCTAGAGCCCAAATTTTAGTCAATCTATCAACTAAAATACCTACTGCTACTACAAGTATT', 'DACD@BEECEDE.BEDDDDD,>:@>EEBEEHEFEHHFFHH?FGBGFBBD77B;;C?FFFFGGFED.BBABBG@DBBE'),
    '@SRX079804:1:SRR292678:1:1101:190845:190845': ('CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC', 'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE'),
    '@SRX079804:1:SRR292678:1:1101:198993:198993': ('AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA', '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB'),
    '@SRX079804:1:SRR292678:1:1101:204480:204480': ('AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG', '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')
    }   # пустой словарь для отфильтрованных ридов
    # если в аргумент передано одно число, то считаем, что это верхняя граница
    if isinstance(gc_bounds, (int, float)):
        gc_bounds = (0, gc_bounds)
    for name, (read, quality) in seqs.items(): # перебираем все риды в словаре seqs
        # проверяем, что рид удовлетворяет условию по GC составу
        if gc_bounds[0] <= gc_content(read) <= gc_bounds[1]:
            # добавляем рид в словарь отфильтрованных ридов
            filtered_seqs[name] = (read, quality)
    return filtered_seqs # возвращаем словарь отфильтрованных ридов

# Функция для фильтрации ридов по длине
def length_bounds_filter(seqs, length_bounds=(0, 2**32)):
    filtered_seqs = {} # пустой словарь для отфильтрованных ридов
    # если в аргумент передано одно число, то считаем, что это верхняя граница
    if isinstance(length_bounds, (int, float)):
        length_bounds = (0, length_bounds)
    for name, (read, quality) in seqs.items(): # перебираем все риды в словаре seqs
        # проверяем, что рид удовлетворяет условию по длине
        if length_bounds[0] <= len(read) <= length_bounds[1]:
            # добавляем рид в словарь отфильтрованных ридов
            filtered_seqs[name] = (read, quality)
    return filtered_seqs # возвращаем словарь отфильтрованных ридов

# Функция для фильтрации ридов по среднему качеству
def quality_threshold_filter(seqs, quality_threshold=0):
    filtered_seqs = {} # пустой словарь для отфильтрованных ридов
    for name, (read, quality) in seqs.items(): # перебираем все риды в словаре seqs
        # проверяем, что рид удовлетворяет условию по среднему качеству
        if mean_quality(quality) >= quality_threshold:
            # добавляем рид в словарь отфильтрованных ридов
            filtered_seqs[name] = (read, quality)
    return filtered_seqs # возвращаем словарь отфильтрованных ридов

# Главная функция для фильтрации ридов по заданным условиям
def filter_reads(seqs, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0):
    # применяем все три функции фильтрации последовательно к словарю seqs
    seqs = gc_bounds_filter(seqs, gc_bounds)
    seqs = length_bounds_filter(seqs, length_bounds)
    seqs = quality_threshold_filter(seqs, quality_threshold)
    return seqs # возвращаем итоговый словарь отфильтрованных ридов
