<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver I] 카드 합체 놀이 - 15903 

[Problem Link](https://www.acmicpc.net/problem/15903) 

### Performance Summary

Memory: 32412 KB, Time: 208 ms

### Classification

자료 구조, Greedy 알고리즘, 우선순위 Queue

### Submission Date

2025-04-22 19:26:37

### Problem Description

<p>석환는 아기다. 아기 석환는 natural number 쓰여져있는 카드 갖고 다양한 놀 하며 노는 것 좋아한다. 오늘 아기 석환는 무슨 놀 하고 있까? 바로 카드 합체 놀다!</p>

<p>아기 석환는 natural number 쓰여진 카드 n장 갖고 exists. 처음in i 카드엔 a<sub>i</sub> 쓰여exists. 카드 합체 놀는  카드들 합체하며 노는 놀다. 카드 합체는 nextand 같은 and정with 루어진다.</p>

<ol>
	<li>x 카드and y 카드 골라 그 두 장in 쓰여진 수 더한 값 계산한다. (x ≠ y)</li>
	<li>계산한 값 x 카드and y 카드 두 장 모두in 덮어 쓴다.</li>
</ol>

<p> 카드 합체 총 m 하면 놀 끝난다. mof 합체 모두 끝낸 뒤, n장of 카드in 쓰여있는 수 모두 더한 값  놀of point수 된다.  point수 장 작게 만드는 것 놀of 목표다.</p>

<p>아기 석환는 Mathematics 좋아하긴 하지만, 아직 아기기 when문in point수 얼마나 작게 만들 수 있는지 알 수는 없었다(어른 석환는 당연히 쉽게 알 수 exists). 그래서 문제 해결 능력 뛰어난 여러분in게 도움 요청했다. 만들 수 있는 smallest point수 계산하는 프로그램 만들어보자.</p>

### Input 

 <p>In the first line, 카드of number 나타내는 수 n(2 ≤ n ≤ 1,000)and 카드 합체 몇  하는지 나타내는 수 m(0 ≤ m ≤ 15×n) are given.</p>

<p>두  줄in 맨 처음 카드of 상태 나타내는 nof natural number a<sub>1</sub>, a<sub>2</sub>, …, a<sub>n</sub> 공백with 구분되어 are given. (1 ≤ a<sub>i</sub> ≤ 1,000,000)</p>

### Output 

 <p>In the first line, 만들 수 있는 smallest point수 Output한다.</p>

