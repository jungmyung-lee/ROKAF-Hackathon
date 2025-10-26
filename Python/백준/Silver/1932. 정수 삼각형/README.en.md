<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver I] 정수 삼각형 - 1932 

[Problem Link](https://www.acmicpc.net/problem/1932) 

### Performance Summary

Memory: 42580 KB, Time: 108 ms

### Classification

Dynamic Programming

### Submission Date

2025-04-18 22:09:51

### Problem Description

<pre>        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5</pre>

<p>위 그림은 size 5인 integer 삼each형of 한 모습다.</p>

<p>맨 위층 7from 시작해서 belowin 있는 수 among 하나 선택하여 below층with 내려올 when, 제to 선택된 수of 합 maximum 되는 path 구하는 프로그램 작성하라. below층in 있는 수는 current 층in 선택된 수of 대each선 왼쪽 or 대each선 오른쪽in 있는 것 among만 선택can.</p>

<p>삼each형of size는 1 상 500 하다. 삼each형 that comprises each 수는 모두 integer며, 범위는 0 상 9999 하다.</p>

### Input 

 <p>In the first line, 삼each형of size n(1 ≤ n ≤ 500) are given and, 둘 lines onwards, n+1 줄to integer 삼each형 are given.</p>

### Output 

 <p>In the first line, 합 maximum 되는 pathin 있는 수of 합 Output한다.</p>

