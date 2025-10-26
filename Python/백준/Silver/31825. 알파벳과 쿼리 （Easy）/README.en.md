<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver V] 알파벳과 쿼리 (Easy) - 31825 

[Problem Link](https://www.acmicpc.net/problem/31825) 

### Performance Summary

Memory: 32412 KB, Time: 48 ms

### Classification

Implementation, String

### Submission Date

2025-04-28 22:43:21

### Problem Description

<p><strong>Hard 버전and $N$, $Q$of 제한 제외한 문제 차는 does not exist.</strong></p>

<p>next 조건들 satisfy하는 부분 String <strong>알파벳 묶음</strong>라고 하자.</p>

<ul>
	<li>하나of 동일한 알파벳with만 String 루어져 있어야 한다.</li>
	<li>전체 Stringin 해당 부분 String 포함한 length 더 긴 부분 String로 알파벳 묶음 만들 수 있으면 그 부분 String은 알파벳 묶음 is not.</li>
</ul>

<p>For example "<code>AAABBAAC</code>"and 같은 String 있 when, <strong>알파벳 묶음</strong>은 "<code>AAA</code>", "<code>BB</code>", "<code>AA</code>", "<code>C</code>"로 4다. 위of Stringin "<code>B</code>", "<code>AC</code>"는 조건 satisfy하지 않으므로 <strong>알파벳 묶음</strong> is not.</p>

<p>영어 알파벳 대문자로만 루어진 length $N$인 String $S = S_1 S_2 \dots S_N$ 주어질 when, next 쿼리 수행하는 프로그램 작성하자.</p>

<ul>
	<li>$1 \ l \ r$ : 부분 String $S_l S_{l+1} \dots S_r$in <strong>알파벳 묶음</strong>of number Output한다.</li>
	<li>$2 \ l \ r$ : 부분 String $S_l S_{l+1} \dots S_r$of all 알파벳 eacheach 알파벳 순서로 next인 알파벳with 변경한다. 단, <code><span color="#e74c3c">Z</span></code>인 경우 <code><span style="color:#e74c3c">A</span></code>로 변경한다.</li>
</ul>

<p>$S_l S_{l+1} \dots S_r$는 $S$of $l$ 알파벳from $r$ 알파벳to 모두 in order 포함하는 부분 String다.</p>

### Input 

 <p>In the first line, Stringof length $N$and 쿼리of number $Q$ 공백with 구분되어 are given. $(3 \leq N, Q \leq 200)$</p>

<p>두  줄in 영어 알파벳 대문자로만 루어진 length $N$인 String $S$ are given.</p>

<p>세  lines onwards, $Q$lines, 걸쳐 쿼리 in one line, one by one are given. $(1 \leq l \leq r \leq N)$</p>

<p>$1$ 쿼리는 한  상 are given.</p>

### Output 

 <p>$1$ 쿼리in 대한 결괏값 in one line, one by one Inputwith given in order Output한다.</p>

