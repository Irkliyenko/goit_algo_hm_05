import timeit

import KMP
import Boyer_Moore
import Rabin_Karp

if __name__ == '__main__':
    with open('file1.txt', 'r') as f1:
        file1 = f1.read()
    with open('file2.txt', 'r') as f2:
        file2 = f2.read()

    pattern1 = 'алгоритм'
    pattern2 = 'алгртм'

    kmp_file1_pattern1_time = timeit.timeit(
        lambda: KMP.kmp_search(file1, pattern1), number=1)
    kmp_file1_pattern2_time = timeit.timeit(
        lambda: KMP.kmp_search(file1, pattern2), number=1)
    kmp_file2_pattern1_time = timeit.timeit(
        lambda: KMP.kmp_search(file2, pattern1), number=1)
    kmp_file2_pattern2_time = timeit.timeit(
        lambda: KMP.kmp_search(file2, pattern2), number=1)

    boyer_moore_file1_pattern1_time = timeit.timeit(
        lambda: Boyer_Moore.boyer_moore_search(file1, pattern1), number=1)
    boyer_moore_file1_pattern2_time = timeit.timeit(
        lambda: Boyer_Moore.boyer_moore_search(file1, pattern2), number=1)
    boyer_moore_file2_pattern1_time = timeit.timeit(
        lambda: Boyer_Moore.boyer_moore_search(file2, pattern1), number=1)
    boyer_moore_file2_pattern2_time = timeit.timeit(
        lambda: Boyer_Moore.boyer_moore_search(file2, pattern2), number=1)

    rabin_karp_file1_pattern1_time = timeit.timeit(
        lambda: Rabin_Karp.rabin_karp_search(file1, pattern1), number=1)
    rabin_karp_file1_pattern2_time = timeit.timeit(
        lambda: Rabin_Karp.rabin_karp_search(file1, pattern2), number=1)
    rabin_karp_file2_pattern1_time = timeit.timeit(
        lambda: Rabin_Karp.rabin_karp_search(file2, pattern1), number=1)
    rabin_karp_file2_pattern2_time = timeit.timeit(
        lambda: Rabin_Karp.rabin_karp_search(file2, pattern2), number=1)

    print(f'| {"Algorithm": <15} | {"File1 pattern1": <15} | {"File1 pattern2": <15} | {"File2 pattern1": <15} | {"File2 pattern2": <15} |')
    print(f'| {"-"*15} | {"-"*15} | {"-"*15} | {"-"*15} | {"-"*15} |')
    print(f'| {"KMP": <15} | {kmp_file1_pattern1_time: <15.5f} | {kmp_file1_pattern2_time: <15.5f} | {kmp_file2_pattern1_time: <15.5f} | {kmp_file2_pattern2_time: <15.5f} |')
    print(f'| {"Boyer–Moore": <15} | {boyer_moore_file1_pattern1_time: <15.5f} | {boyer_moore_file1_pattern2_time: <15.5f} | {boyer_moore_file2_pattern1_time: <15.5f} | {boyer_moore_file2_pattern2_time: <15.5f} |')
    print(f'| {"Rabin–Karp": <15} | {rabin_karp_file1_pattern1_time: <15.5f} | {rabin_karp_file1_pattern2_time: <15.5f} | {rabin_karp_file2_pattern1_time: <15.5f} | {rabin_karp_file2_pattern2_time: <15.5f} |')
