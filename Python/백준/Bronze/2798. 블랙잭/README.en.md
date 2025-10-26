<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Bronze II] 블랙잭 - 2798 

[Problem Link](https://www.acmicpc.net/problem/2798) 

### Performance Summary

Memory: 32412 KB, Time: 112 ms

### Classification

Brute Force 알고리즘

### Submission Date

2025-10-26 21:49:09

### Problem Description

<p>카지노in 제일 인기 있는 게임 블랙잭of rule은 상당히 쉽다. 카드of 합 21 넘지 않는 한도 내in, 카드of 합 maximum한 크게 만드는 게임다. 블랙잭은 카지노마다 다양한 규정 exists.</p>

<p>한국 최고of 블랙잭 고수 김정인은 새로운 블랙잭 rule 만들어 상근, 창영and 게임하려고 한다.</p>

<p>김정인 버전of 블랙잭in each 카드in는 양of integer 쓰여 exists. 그 next, 딜러는 N장of 카드 모두 숫자 보도록 바닥in 놓는다. 그런 후in 딜러는 숫자 M 크게 외친다.</p>

<p>제 플레어는 제한된 Time 안in N장of 카드 among 3장of 카드 골라야 한다. 블랙잭 변형 게임기 when문in, 플레어 고른 카드of 합은 M 넘지 않으면서 Mand maximum한 깝게 만들어야 한다.</p>

<p>N장of 카드in 써져 있는 숫자 when given, M 넘지 않으면서 Min maximum한 까운 카드 3장of 합 구해 Output하시오.</p>

### Input 

 <p>In the first line, 카드of number N(3 ≤ N ≤ 100)and M(10 ≤ M ≤ 300,000) are given. In the second line,는 카드in 쓰여 있는 수 주어지며,  값은 100,000 넘지 않는 양of integer다.</p>

<p>합 M 넘지 않는 카드 3장 that can be found 경우만 Inputwith are given.</p>

### Output 

 <p>In the first line, M 넘지 않으면서 Min maximum한 까운 카드 3장of 합 Output한다.</p>

