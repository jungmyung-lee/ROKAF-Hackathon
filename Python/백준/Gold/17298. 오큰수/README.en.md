<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Gold IV] 오큰수 - 17298 

[Problem Link](https://www.acmicpc.net/problem/17298) 

### Performance Summary

Memory: 135836 KB, Time: 1032 ms

### Classification

자료 구조, Stack

### Submission Date

2025-04-14 00:39:00

### Problem Description

<p>size N인 sequence A = A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub> exists. sequenceof each 원소 A<sub>i</sub>in 대해서 오큰수 NGE(i) 구하려고 한다. A<sub>i</sub>of 오큰수는 오른쪽in 있으면서 A<sub>i</sub>보다 큰 수 among 장 왼쪽in 있는 수 of미한다. 그러한 수 없는 경우in 오큰수는 -1다.</p>

<p>For example, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1다. A = [9, 5, 4, 8]인 경우in는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1다.</p>

### Input 

 <p>In the first line, sequence Aof size N (1 ≤ N ≤ 1,000,000) are given. In the second line, sequence Aof 원소 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub> (1 ≤ A<sub>i</sub> ≤ 1,000,000) are given.</p>

### Output 

 <p>총 Nof 수 NGE(1), NGE(2), ..., NGE(N) 공백with 구분해 Output한다.</p>

