Comparative Analysis of Sorting Algorithms

Task Description

The goal of this study was to compare the efficiency of three sorting algorithms: Insertion Sort, Merge Sort, and Python's built-in Timsort algorithm. Efficiency was evaluated by measuring execution time on random data sets of varying sizes.


Theoretical Background

| Algorithm        | Best Case  | Average Case | Worst Case   | Stability |
+------------------+------------+--------------+--------------+-----------+
| Insertion Sort   | O(N)       | O(N^2)       | O(N^2)       | Yes       |
| Merge Sort       | O(N log N) | O(N log N)   | O(N log N)   | Yes       |
| Timsort (Python) | O(N)       | O(N log N)   | O(N log N)   | Yes       |


Empirical Results
Testing was conducted on random sets of integers. Time is recorded in seconds (cumulative time for 5 runs).

Size       | Insertion Sort (sec)      | Merge Sort (sec)     | Timsort (sorted) (sec)   
-------------------------------------------------------------------------------------
100        | 0.00033                   | 0.00027              | 0.00002                  
1000       | 0.04542                   | 0.00388              | 0.00023                  
5000       | 1.19471                   | 0.02336              | 0.00148                  
10000      | 4.89537                   | 0.05040              | 0.00385      


Analysis and Conclusions

1. Insertion Sort: As predicted by theory, this algorithm demonstrates quadratic time dependence on data size ($O(N^2)$). It performs acceptably on small arrays (N=100), but its performance drops dramatically as N increases. At 10,000 elements, it is hundreds of times slower than the other algorithms. It is efficient only for very small or nearly sorted data sets.

2. Merge Sort: Demonstrates stable efficiency of $O(N \log N)$. It is significantly faster than Insertion Sort on large data sets. The execution time grows predictably and moderately with increasing data volume.

3. Timsort (Python's Built-in Sort): Timsort is the absolute leader in all tests. It is an order of magnitude faster even than pure Merge Sort.


Why is Timsort so fast?
- It is a hybrid algorithm: it uses Insertion Sort for small subarrays (where it is very fast) and Merge Sort to combine these subarrays.
- It is adaptive: it takes advantage of existing ordering in the data ("runs") to speed up operations.
- The Python implementation is written in C and highly optimized at a low level, giving it a significant advantage over pure Python implementations.


Summary: 

The empirical data fully confirms the theoretical complexity estimates. For real-world Python programming tasks, using the built-in sorted() function or list method .sort() is the best choice due to their high efficiency, stability, and optimization (Timsort algorithm). Custom algorithm implementations are useful for educational purposes but rarely outperform built-in solutions.
