<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver IV] Deque - 10866 

[Problem Link](https://www.acmicpc.net/problem/10866) 

### Performance Summary

Memory: 32412 KB, Time: 44 ms

### Classification

Implementation, 자료 구조, Deque

### Submission Date

2025-04-13 18:48:39

### Problem Description

<p>integer 저장하는 Deque(Deque) Implementation한 next, Inputwith 주어지는 명령 처리하는 프로그램 작성하시오.</p>

<p>명령은 총 여덟 지다.</p>

<ul>
	<li>push_front X: integer X Dequeof 앞in 넣는다.</li>
	<li>push_back X: integer X Dequeof 뒤in 넣는다.</li>
	<li>pop_front: Dequeof 장 앞in 있는 수 빼고, 그 수 Output한다. if, Dequein 들어있는 integer 없는 경우in는 -1 Output한다.</li>
	<li>pop_back: Dequeof 장 뒤in 있는 수 빼고, 그 수 Output한다. if, Dequein 들어있는 integer 없는 경우in는 -1 Output한다.</li>
	<li>size: Dequein 들어있는 integerof number Output한다.</li>
	<li>empty: Deque 비어있으면 1, 아니면 0 Output한다.</li>
	<li>front: Dequeof 장 앞in 있는 integer Output한다. if Dequein 들어있는 integer 없는 경우in는 -1 Output한다.</li>
	<li>back: Dequeof 장 뒤in 있는 integer Output한다. if Dequein 들어있는 integer 없는 경우in는 -1 Output한다.</li>
</ul>

### Input 

 <p>In the first line, 주어지는 명령of 수 N (1 ≤ N ≤ 10,000) are given. 둘 lines onwards, Nlines,는 명령 one by one are given. 주어지는 integer는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제in 나and있지 않은 명령 주어지는 경우는 does not exist.</p>

### Output 

 <p>Output해야하는 명령 주어질 when마다, in one line, one by one Output한다.</p>

