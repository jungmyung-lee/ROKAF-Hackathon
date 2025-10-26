<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver II] 에디터 - 1406 

[Problem Link](https://www.acmicpc.net/problem/1406) 

### Performance Summary

Memory: 43420 KB, Time: 308 ms

### Classification

자료 구조, Stack, 연결 리스트

### Submission Date

2025-04-13 17:30:18

### Problem Description

<p>한 줄로 된 간단한 in디터 Implementation하려고 한다.  편house기는 영어 소문자만 기록할 수 있는 편house기로, maximum 600,000글자to Inputcan.</p>

<p> 편house기in는 '커서'라는 것 있는데, 커서는 문장of 맨 앞(첫  문자of 왼쪽), 문장of 맨 뒤(마지막 문자of 오른쪽), or 문장 among간 임ofof 곳(all 연속된 두 문자 사)in positioncan. 즉 length L인 String current 편house기in Input되어 있으면, 커서 position할 수 있는 곳은 L+1지 경우 exists.</p>

<p> 편house기 지원하는 명령어는 nextand 같다.</p>

<table class="table table-bordered" style="width:100%">
	<tbody>
		<tr>
			<th style="width:20%">L</th>
			<td style="width:80%">커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)</td>
		</tr>
		<tr>
			<th>D</th>
			<td>커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)</td>
		</tr>
		<tr>
			<th>B</th>
			<td>커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)<br>
			삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임</td>
		</tr>
		<tr>
			<th>P \$</th>
			<td>\$라는 문자를 커서 왼쪽에 추가함</td>
		</tr>
	</tbody>
</table>

Write a program to find <p>초기in 편house기in Input되어 있는 String are given and, 그 후 Input한 명령어 차례로 when given, all 명령어 수행하고 난 후 편house기in Input되어 있는 String. 단, 명령어 수행되기 전in 커서는 문장of 맨 뒤in positionis고 한다.</p>

### Input 

 <p>In the first line,는 초기in 편house기in Input되어 있는 String are given.  String은 length N고, 영어 소문자로만 루어져 있으며, length는 100,000 넘지 않는다. In the second line,는 Input할 명령어of number 나타내는 integer M(1 ≤ M ≤ 500,000) are given. 셋 lines onwards, Mlines, 걸쳐 Input할 명령어 in order are given. 명령어는 위of 네 지 among 하나of 형태로만 are given.</p>

### Output 

 <p>In the first line, all 명령어 수행하고 난 후 편house기in Input되어 있는 String Output한다.</p>

