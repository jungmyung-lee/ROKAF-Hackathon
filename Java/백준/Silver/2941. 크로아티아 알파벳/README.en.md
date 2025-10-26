<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver V] 크로아티아 알파벳 - 2941 

[Problem Link](https://www.acmicpc.net/problem/2941) 

### Performance Summary

Memory: 17616 KB, Time: 164 ms

### Classification

Implementation, String

### Submission Date

2025-05-05 19:23:23

### Problem Description

<p>예전in는 운영체제in 크로아티아 알파벳 Input할 수 없었다. 따라서, nextand 같 크로아티아 알파벳 변경해서 Input했다.</p>

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

<p>For example, ljes=njak은 크로아티아 알파벳 6(lj, e, š, nj, a, k)로 루어져 exists. 단어 when given, 몇 of 크로아티아 알파벳with 루어져 있는지 Output한다.</p>

<p>dž는 무조건 하나of 알파벳with 쓰고, dand ž 분리된 것with 보지 않는다. ljand nj도 마찬지다. 위 목록in 없는 알파벳은 한 글자씩 센다.</p>

### Input 

 <p>In the first line, maximum 100글자of 단어 are given. 알파벳 소문자and '-', '='로만 루어져 exists.</p>

<p>단어는 크로아티아 알파벳with 루어져 exists. Problem Descriptionof 표in 나and있는 알파벳은 변경된 형태로 Input된다.</p>

### Output 

 <p>Inputwith given 단어 몇 of 크로아티아 알파벳with 루어져 있는지 Output한다.</p>

