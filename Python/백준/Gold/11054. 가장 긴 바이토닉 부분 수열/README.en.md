<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Gold IV] 가장 긴 바이토닉 부분 수열 - 11054 

[Problem Link](https://www.acmicpc.net/problem/11054) 

### Performance Summary

Memory: 32412 KB, Time: 204 ms

### Classification

Dynamic Programming

### Submission Date

2025-04-29 18:53:09

### Problem Description

<p>sequence S some 수 S<sub>k</sub> 기준with S<sub>1</sub> < S<sub>2</sub> < ... S<sub>k-1</sub> < S<sub>k</sub> > S<sub>k+1</sub> > ... S<sub>N-1</sub> > S<sub>N</sub> if it satisfies, 그 sequence bitonic sequence(called).</p>

<p>For example, {10, 20, <strong>30</strong>, 25, 20}and {10, 20, 30, <strong>40</strong>}, {<strong>50</strong>, 40, 25, 10} 은 bitonic sequencebut,  {1, 2, 3, 2, 1, 2, 3, 2, 1}and {10, 20, 30, 40, 20, 30} 은 bitonic sequence is not.</p>

Write a program to find <p>sequence A when given, 그 sequenceof subsequence among bitonic sequence면서 longest sequenceof length.</p>

### Input 

 <p>In the first line, sequence Aof size N are given and, In the second line,는 sequence A that comprises A<sub>i</sub> are given. (1 ≤ N ≤ 1,000, 1 ≤ A<sub>i</sub> ≤ 1,000)</p>

### Output 

 <p>In the first line, sequence Aof subsequence among longest bitonic sequenceof length Output한다.</p>

