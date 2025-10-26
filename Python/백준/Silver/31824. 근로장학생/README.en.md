<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver III] 근로장학생 - 31824 

[Problem Link](https://www.acmicpc.net/problem/31824) 

### Performance Summary

Memory: 32412 KB, Time: 664 ms

### Classification

Implementation, 자료 구조, String, Sorting, 집합과 맵, 해시를 사용한 집합과 맵

### Submission Date

2025-04-28 20:10:05

### Problem Description

<p>하루는 문장 내in 있는 영어 단어 찾아 그 뜻 알려주는 프로그램 만드는 근로장학생 되었다.</p>

<p>하지만 하루는 너무 귀찮은 나머지 프로그램 만들지 않았고, 제작 마감일 $1$일전 당신in게 급하게 프로그램 만드는 걸 도and달라고 요청했다. 하루 도and주자.</p>

<ul>
	<li>each 정보는 $(Q_i, A_i)$로 루어져 있으며, $Q_i$는 영어 단어, $A_i$는 그 단어of 뜻 of미한다.</li>
	<li>프로그램in게 $N$of 정보and $M$of 문장 주어질 when, each 문장in 대해 프로그램 답하는 and정은 nextand 같다.
	<ul>
		<li>문장 $S$of 장 왼쪽in 있는 문자of position $1$, 장 오른쪽in 있는 문자of position $|S|$라고 하자. when $|S|$는 문장 $S$of length of미한다.</li>
		<li>프로그램은 each 문장 $S$of 첫  문자from, 마지막 문자to $S_1,$ $S_2,$ $\cdots,$ $S_{|S|-1},$ $S_{|S|}$of 순서로 읽는다.</li>
		<li>문장 읽는 도among, if position $k$in position $k$, $k+1$, $\cdots$, $k+|Q_i|-1$in 있는 문자 in order 어 붙였 when $Q_i$ 만들 수 exists면 $A_i$로 답해야 하며, $k$in 대해 만들 수 있는 $Q_i$ 여러 라면, 사전순with 앞선 $Q_i$from $A_i$로 답하면 된다.</li>
		<li>한 문장in 대해 답해야 하는 $A_i$는 여러일 수 exists.</li>
	</ul>
	</li>
</ul>

<p>For example, 정보 $(Q_i, A_i)$ (<span style="color:#e74c3c;"><code>ABC</code></span>, <span style="color:#e74c3c;"><code>X</code></span>), (<span style="color:#e74c3c;"><code>A</code></span>, <span style="color:#e74c3c;"><code>Y</code></span>), (<span style="color:#e74c3c;"><code>CDE</code></span>, <span style="color:#e74c3c;"><code>Z</code></span>)고 질문 <code><span style="color:#e74c3c;">ABCDE</span></code>라면 프로그램은 <span style="color:#e74c3c;"><code>YXZ</code></span>로 답해야 한다.</p>

### Input 

 <p>In the first line, 정보of number 나타내는 integer $N$and 문장of number 나타내는 integer $M$ 공백with 구분되어 are given. ($1 \leq N \leq 1\ 000$; $1 \leq M \leq 10$)</p>

<p>두  lines onwards, $N$lines, 걸쳐 $(Q_i, A_i$) 나타내는 String $Q_i$and $A_i$ 공백with 구분되어 are given. ($1 \leq |Q_i|, |A_i| \leq 10$; $i \neq j$면 $Q_i \neq Q_j$)</p>

<p>그next lines onwards, $M$lines, 걸쳐 String $S_i$ are given. ($1 \leq |S| \leq 100$)</p>

<p>Input되는 all String은 영어 대문자로만 루어져 exist and, 공백은 does not exist.</p>

### Output 

 <p>each String $S_i$in 대해 당신 만든 프로그램 답해야 하는 String in one line, one by one Output하라.</p>

<p>if 프로그램 답할 수 있는 String does not exist면 <span style="color:#e74c3c;"><code>-1</code></span> 대신 Output하라.</p>

