<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Bronze III] 중앙 이동 알고리즘 - 2903 

[Problem Link](https://www.acmicpc.net/problem/2903) 

### Performance Summary

Memory: 32412 KB, Time: 32 ms

### Classification

Mathematics

### Submission Date

2025-10-26 21:49:40

### Problem Description

<p>상근는 친구들and 함께 SF영화 찍으려고 한다.  영화는 외계 지형 필요하다. 실제로 우주선 타고 외계 행성in 서 촬영 할 수 없기 when문in, 컴퓨터 그래픽with CG처리 하려고 한다.</p>

<p>외계 지형은 among앙 동 알고리즘 용해서 만들려고 한다.</p>

<p>알고리즘 시작하면서 상근는 정사each형 루는 point 4 고른다. 그 후in는 nextand 같은 and정 거쳐서 지형 만든다.</p>

<ol>
	<li>정사each형of each 변of among앙in point 하나 추한다.</li>
	<li>정사each형of among심in point 하나 추한다.</li>
</ol>

<p>초기 상태in 위and 같은 and정 한  거치면 총 4of 정사each형 새로 생긴다. and 같은 and정 상근 satisfy할 when to 계속한다.</p>

<p>below 그림은 and정 총 2 거쳤 whentoof 모습다.</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td><img alt="" src="" style="width: 214px; height: 213px;"></td>
			<td><img alt="" src="" style="width: 212px; height: 213px;"></td>
			<td><img alt="" src="" style="width: 212px; height: 213px;"></td>
		</tr>
		<tr>
			<td>초기 상태 - 점 4개</td>
			<td>1번 - 점 9개</td>
			<td>2번 - 25개</td>
		</tr>
	</tbody>
</table>

<p>상근는 some point은 한  보다 많은 정사each형in 포함될 수 exists는 사실 알았다. Memory 소모량 줄기 위해서 among복하는 point 한 만 저장하려고 한다. and정 N 거친 후 point 몇  저장해야 하는지 구하는 프로그램 작성하시오.</p>

### Input 

 <p>In the first line, N are given. (1 ≤ N ≤ 15)</p>

### Output 

 <p>In the first line, and정 N 거친 후 pointof 수 Output한다.</p>

