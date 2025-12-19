# [Silver V] 크로아티아 알파벳 - 2941 

[Problem Link](https://www.acmicpc.net/problem/2941) 

### Performance Summary

Memory: 17616 KB, Time: 164 ms

### Classification

Implementation, String

### Submission Date

2025-05-05 19:23:23

### Problem Description

<p>예전에는 운영체제에서 크로아티아 알파벳을 Input할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 Input했다.</p>

<table class="table table-bordered table-center-20 th-center td-center">
	<thead>
		<tr>
			<th>크로아티아 알파벳</th>
			<th>변경</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>č</td>
			<td>c=</td>
		</tr>
		<tr>
			<td>ć</td>
			<td>c-</td>
		</tr>
		<tr>
			<td>dž</td>
			<td>dz=</td>
		</tr>
		<tr>
			<td>đ</td>
			<td>d-</td>
		</tr>
		<tr>
			<td>lj</td>
			<td>lj</td>
		</tr>
		<tr>
			<td>nj</td>
			<td>nj</td>
		</tr>
		<tr>
			<td>š</td>
			<td>s=</td>
		</tr>
		<tr>
			<td>ž</td>
			<td>z=</td>
		</tr>
	</tbody>
</table>

<p>예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 Output한다.</p>

<p>dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.</p>

### Input 

 <p>첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.</p>

<p>단어는 크로아티아 알파벳으로 이루어져 있다. Problem Description의 표에 나와있는 알파벳은 변경된 형태로 Input된다.</p>

### Output 

 <p>Input으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 Output한다.</p>

