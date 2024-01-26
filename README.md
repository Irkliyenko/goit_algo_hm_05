# **Performance Analysis of Searching Algorithms**

In this analysis, I compared the performance of three search algorithms: Knuth–Morris–Pratt (KMP) algorithm, Boyer-Moore algorithm, and Rabin-Karp algorithm. I utilized two different .txt files and searched for two patterns, one present in the text (Pattern 1) and the other absent in the text (Pattern 2). The performance time for each algorithm is summarized in Table 1.

**Table 1: Searching Performance of Knuth–Morris–Pratt algorithm, Boyer-Moore algorithm, and Rabin-Karp algorithm**

| Algorithm   | File1 pattern1 | File1 pattern2 | File2 pattern1 | File2 pattern2 |
| ----------- | -------------- | -------------- | -------------- | -------------- |
| KMP         | 0.00003        | 0.00123        | 0.00030        | 0.00185        |
| Boyer–Moore | 0.00002        | 0.00079        | 0.00016        | 0.00115        |
| Rabin–Karp  | 0.00005        | 0.00195        | 0.00046        | 0.00289        |

These findings revealed that when patterns were found in the text, the Boyer-Moore algorithm consistently demonstrated superior performance, followed by KMP, while Rabin-Karp exhibited slower execution times. This pattern held true for both Pattern 1 and Pattern 2 scenarios. The observed outcomes can be attributed to the underlying complexities of these algorithms:

Boyer-Moore boasts O(n) complexity in the best case, providing efficient skipping strategies, and O(n*m) in the worst case.
KMP exhibits O(n+m) complexity in both best and worst cases, leveraging its sophisticated failure function to optimize pattern matching.
Rabin-Karp has O(n+m) complexity in the best case, leveraging hashing, but shows increased time consumption in the worst case with O(n*m).

These results underscore the importance of considering algorithmic characteristics and complexities when selecting a searching algorithm for specific use cases. The Boyer-Moore algorithm, with its linear-time best-case complexity, emerges as a robust choice for scenarios where patterns are likely to be found early in the text. KMP, with consistent linear time complexity, proves to be a reliable performer across various scenarios. Rabin-Karp, while demonstrating efficiency in certain cases, may face challenges with larger datasets and specific patterns.
