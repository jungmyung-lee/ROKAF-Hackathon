<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Bronze I] 우유가 넘어지면? - 17363 

[Problem Link](https://www.acmicpc.net/problem/17363) 

### Performance Summary

Memory: 32412 KB, Time: 36 ms

### Classification

Implementation

### Submission Date

2025-04-26 23:29:01

### Problem Description

<p>유머 감each 뛰어난 성원는 매일 재미있는 농담 준비한다. 오늘 준비한 농담은 바로 것다.</p>

<blockquote>
<p>우유 넘어질 when 뭐라고 하게? 답은 "아야"! 깔깔!</p>
</blockquote>

<p>친구들of 반응 심드렁하자, 성원는 해설 덧붙였다.</p>

<blockquote>
<p>"우유" 세로로 적혀 있는 상자 왼쪽with 툭 넘어뜨리면 "아야" 되잖아? 게 마치 우유 넘어져서 아파하는 것 같다는 point 웃음 포인트야!</p>
</blockquote>

<p style="margin-bottom: 20px;"><img alt="milk" src="" style="display: block; margin-left: auto; margin-right: auto; width: 100%; max-width: 300px;"></p>

<p>그럼in도 불구하고 친구들 웃지 않자, 성원는 친구들 공간지each력 부족해 상자 넘어뜨리는 모습 상상하지 못한다고 생each했다. 그래서 상자 넘어뜨리는 프로그램 만들어 친구들in게 결and 보여주기로 했다.</p>

<p>성원는 상자in "우유" 아니라 다른 그림 그려져 있어도 프로그램 잘 동작하기 원한다. 성원는 상자of 면 격자로 나누고 each 칸in below 문자들 among 하나 그려 넣는 방식with 그림 그린다.</p>

<table class="table table-bordered" style="margin-left: auto; margin-right: auto; width: 360px;">
	<tbody>
		<tr>
			<th style="text-align: center; width: 80px;">문자</th>
			<th style="text-align: center; width: 120px;">이름</th>
			<th style="text-align: center; width: 80px;">ASCII</th>
			<th style="text-align: center; width: 80px;">돌린 뒤</th>
		</tr>
		<tr>
			<td style="text-align: center;"><code>.</code></td>
			<td style="text-align: center;">온점</td>
			<td style="text-align: center;">46</td>
			<td style="text-align: center;"><code>.</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>O</code></td>
			<td style="text-align: center;">대문자 O</td>
			<td style="text-align: center;">79</td>
			<td style="text-align: center;"><code>O</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>-</code></td>
			<td style="text-align: center;">하이픈</td>
			<td style="text-align: center;">45</td>
			<td style="text-align: center;"><code>|</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>|</code></td>
			<td style="text-align: center;">세로 바</td>
			<td style="text-align: center;">124</td>
			<td style="text-align: center;"><code>-</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>/</code></td>
			<td style="text-align: center;">슬래시</td>
			<td style="text-align: center;">47</td>
			<td style="text-align: center;"><code>\</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>\</code></td>
			<td style="text-align: center;">역슬래시</td>
			<td style="text-align: center;">92</td>
			<td style="text-align: center;"><code>/</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>^</code></td>
			<td style="text-align: center;">캐럿</td>
			<td style="text-align: center;">94</td>
			<td style="text-align: center;"><code><</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code><</code></td>
			<td style="text-align: center;">왼쪽 부등호</td>
			<td style="text-align: center;">60</td>
			<td style="text-align: center;"><code>v</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>v</code></td>
			<td style="text-align: center;">소문자 V</td>
			<td style="text-align: center;">118</td>
			<td style="text-align: center;"><code>></code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>></code></td>
			<td style="text-align: center;">오른쪽 부등호</td>
			<td style="text-align: center;">62</td>
			<td style="text-align: center;"><code>^</code></td>
		</tr>
	</tbody>
</table>

<p>그러나 성원는 내일of 농담 생each하느라 프로그램 만들 Time does not exist. 성원 대신 프로그램 만들어 주자.</p>

### Input 

 <p>첫 줄in 그림of 세로 lengthand 로 length of미하는 integer <em>N</em>and <em>M</em>(1 ≤ <em>N</em>, <em>M</em> ≤ 100) are given.</p>

<p>next <em>N</em>lines, 걸쳐 그림of each 줄 of미하는 <em>M</em>글자of String one by one are given. String은 공백 포함하지 않으며 위of 표in given 문자로만 루어져 있음 보장된다.</p>

### Output 

 <p><em>M</em>lines, 걸쳐 Input된 그림 왼쪽with 넘어뜨렸 whenof 결and Output한다.</p>

