<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver II] 더 흔한 타일 색칠 문제 - 28298 

[Problem Link](https://www.acmicpc.net/problem/28298) 

### Performance Summary

Memory: 33332 KB, Time: 568 ms

### Classification

Implementation, Greedy 알고리즘, Brute Force 알고리즘

### Submission Date

2025-04-26 17:10:37

### Problem Description

<p>$N\times M$ sizeof 타일 exists. 타일of $i$행 $j$열in 해당하는 칸은 처음in $d_{i,j}$ colorwith color칠되어 exists. 타일of color상은 하나of 알파벳 대문자로 표현된다.</p>

<p>given 타일 $K\times K$ sizeof 작은 타일들로 겹치지 않게 나눴 when, 나눠진 타일of color상 배치 전부 동일하도록 타일of 일부 칸 골라 다시 color칠하고자 한다. some 칸 다시 colorof painting 데 사용할 수 있는 color상of 종류 또한 하나of 알파벳 대문자로 표현할 수 있는 color상 among 하나여야 한다.</p>

<p><strong>minimum 몇 of 칸</strong> 다시 color칠해야 하는지 구하고,  satisfy하는 타일of color상 배치 <strong>아무거나 하나</strong> Output하라.</p>

### Input 

 <p>In the first line, 세 integer $N$, $M$, $K$ 공백with 구분되어 are given. $(1\le N,M,K\le 500;$ $N,M$은 $K$of 배수다$)$</p>

<p>next $N$lines,는 타일of $i$행 color상 배치 of미하는 length $M$of String $d_i$ are given. $d_i$는 알파벳 대문자로만 루어져 exists.</p>

### Output 

 <p>In the first line,는 다시 칠해야 하는 타일of minimum number Output한다.</p>

<p>next $N$lines,는 새로 칠한 타일of $i$행 color상 배치 of미하는 length $M$of String Output한다. Output하는 String 역시 모두 알파벳 대문자로만 루어져 있어야 한다.</p>

