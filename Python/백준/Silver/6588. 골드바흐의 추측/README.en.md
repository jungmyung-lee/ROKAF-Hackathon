<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver I] 골드바흐의 추측 - 6588 

[Problem Link](https://www.acmicpc.net/problem/6588) 

### Performance Summary

Memory: 40224 KB, Time: 2832 ms

### Classification

Mathematics, Number Theory, 소수 판정, 에라토스테네스의 체

### Submission Date

2025-04-28 23:17:29

### Problem Description

<p>1742년, 독일of 아마추어 Mathematics 크리스티안 골드바흐는 레온하르트 오일러in게 nextand 같은 추측 제안하는 편지 보냈다.</p>

<blockquote>4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.</blockquote>

<p>For example 8은 3 + 5로 can be represented, 3and 5는 모두 홀수인 소수다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 다.</p>

<p> 추측은 아직도 해결되지 않은 문제다.</p>

<p>백만 하of all 짝수in 대해서,  추측 검증하는 프로그램 작성하시오.</p>

### Input 

 <p>Input은 하나 or 그 상of 테스트 케스로 루어져 exists. 테스트 케스of number는 100,000 넘지 않는다.</p>

<p>each 테스트 케스는 짝수 integer n 하나로 루어져 exists. (6 ≤ n ≤ 1000000)</p>

<p>Inputof 마지막 줄in는 0 하나 are given.</p>

### Output 

 <p>each 테스트 케스in 대해서, n = a + b 형태로 Output한다. when, aand b는 홀수 소수다. 숫자and 연산자는 공백 하나로 구분되어져 exists. if, n 만들 수 있는 방법 여러 지라면, b-a largest 것 Output한다. 또, 두 홀수 소수of 합with n 나타낼 수 없는 경우in는 "Goldbach's conjecture is wrong." Output한다.</p>

