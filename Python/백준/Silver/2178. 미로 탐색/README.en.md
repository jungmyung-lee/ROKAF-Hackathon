<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver I] 미로 탐색 - 2178 

[Problem Link](https://www.acmicpc.net/problem/2178) 

### Performance Summary

Memory: 34968 KB, Time: 64 ms

### Classification

Graph Theory, Graph Traversal, Breadth-First Search, 격자 그래프

### Submission Date

2025-10-26 21:43:38

### Problem Description

<p>N×Msizeof array로 표현되는 미로 exists.</p>

<table class="table table-bordered" style="width:18%">
	<tbody>
		<tr>
			<td style="width:3%">1</td>
			<td style="width:3%">0</td>
			<td style="width:3%">1</td>
			<td style="width:3%">1</td>
			<td style="width:3%">1</td>
			<td style="width:3%">1</td>
		</tr>
		<tr>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

Write a program to find <p>미로in 1은 동할 수 있는 칸 나타내고, 0은 동할 수 없는 칸 나타낸다. 러한 미로 when given, (1, 1)in 출발하여 (N, M)of position로 동할 when 지나야 하는 minimumof 칸 수. 한 칸in 다른 칸with 동할 when, 서로 인접한 칸with만 동can.</p>

<p>위of 예in는 15칸 지나야 (N, M)of position로 동can. 칸 셀 whenin는 시작 positionand 도착 position도 포함한다.</p>

### Input 

 <p>In the first line, 두 integer N, M(2 ≤ N, M ≤ 100) are given. next Nlines,는 Mof integer로 미로 are given. each 수들은 <strong>붙어서</strong> Inputwith are given.</p>

### Output 

 <p>In the first line, 지나야 하는 minimumof 칸 수 Output한다. 항상 도착position로 동할 수 있는 경우만 Inputwith are given.</p>

