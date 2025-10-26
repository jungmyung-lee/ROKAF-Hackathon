<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Bronze III] 공 넣기 - 10810 

[Problem Link](https://www.acmicpc.net/problem/10810) 

### Performance Summary

Memory: 32412 KB, Time: 36 ms

### Classification

Implementation, Simulation

### Submission Date

2025-10-26 21:55:50

### Problem Description

<p>도현는 바구니 총 N 지고 exist and, each 바구니in는 1from Nto 호 매겨져 exists. 또, 1from Nto 호 적혀있는 공 매우 많 지고 exists. 장 처음 바구니in는 공 들어있지 않으며, 바구니in는 공 1만 넣 수 exists.</p>

<p>도현는 앞with M 공 넣으려고 한다. 도현는 한  공 넣 when, 공 넣 바구니 범위 정하고, 정한 바구니in 모두 같은 호 적혀있는 공 넣는다. if, 바구니in 공 미 있는 경우in는 들어있는 공 빼고, 새로 공 넣는다. 공 넣 바구니는 연속되어 있어야 한다.</p>

<p>공 어떻게 넣지 when given, M 공 넣은 후in each 바구니in some 공 들어 있는지 구하는 프로그램 작성하시오.</p>

### Input 

 <p>In the first line, N (1 ≤ N ≤ 100)and M (1 ≤ M ≤ 100) are given.</p>

<p>둘 lines onwards, Mlines, 걸쳐서 공 넣는 방법 are given. each 방법은 세 integer i j k로 루어져 있으며, i 바구니from j 바구니toin k 호 적혀져 있는 공 넣는다는 뜻다. For example, 2 5 6은 2 바구니from 5 바구니toin 6 공 넣는다는 뜻다. (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)</p>

<p>도현는 Inputwith given in order 공 넣는다.</p>

### Output 

 <p>1 바구니from N 바구니in 들어있는 공of 호 공백with 구분해 Output한다. 공 들어있지 않은 바구니는 0 Output한다.</p>

