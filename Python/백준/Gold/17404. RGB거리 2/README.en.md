<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Gold IV] RGB거리 2 - 17404 

[Problem Link](https://www.acmicpc.net/problem/17404) 

### Performance Summary

Memory: 33432 KB, Time: 36 ms

### Classification

Dynamic Programming

### Submission Date

2025-04-19 20:22:33

### Problem Description

<p>RGB Streetin는 house N exists. street는 선분with can be represented, 1 housefrom N house in order exists.</p>

Let's find <p>house은 red, green, blue among 하나of colorwith must be painted. each house red, green, bluewith of painting cost when given, below rule while satisfying all house of painting costof minimum value.</p>

<ul>
	<li>1 houseof color은 2, N houseof colorand must not be the same.</li>
	<li>N houseof color은 N-1, 1 houseof colorand must not be the same.</li>
	<li>i(2 ≤ i ≤ N-1) houseof color은 i-1, i+1 houseof colorand must not be the same.</li>
</ul>

### Input 

 <p>In the first line, houseof 수 N(2 ≤ N ≤ 1,000) are given. 둘 lines onwards, Nlines,는 each house red, green, bluewith of painting cost 1 housefrom in one line, one by one are given. house of painting cost은 1,000less than or equal to natural number다.</p>

### Output 

 <p>In the first line, all house of painting costof minimum value Output한다.</p>

