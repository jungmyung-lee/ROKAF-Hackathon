<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver II] 쇠막대기 - 10799 

[Problem Link](https://www.acmicpc.net/problem/10799) 

### Performance Summary

Memory: 32544 KB, Time: 56 ms

### Classification

자료 구조, Stack

### Submission Date

2025-04-13 22:41:01

### Problem Description

<p>여러 of 쇠막대기 레저로 절단하려고 한다. 효율적인 작업 위해서 쇠막대기 belowin 위로 겹쳐 놓고, 레저 위in 수직with 발사하여 쇠막대기들 자른다. 쇠막대기and 레저of 배치는 next 조건 satisfy한다.</p>

<ul>
	<li>쇠막대기는 자신보다 긴 쇠막대기 위in만 놓일 수 exists. - 쇠막대기 다른 쇠막대기 위in 놓는 경우 완전히 포함되도록 놓되, 끝point은 겹치지 않도록 놓는다.</li>
	<li>each 쇠막대기 자르는 레저는 적어도 하나 존재한다.</li>
	<li>레저는 some 쇠막대기of 양 끝pointand도 겹치지 않는다. </li>
</ul>

<p>below 그림은 위 조건 satisfy하는 예 보여준다. 수평with 그려진 굵은 실선은 쇠막대기고, point은 레저of position, 수직with 그려진 point선 화살표는 레저of 발사 방향다.</p>

<p style="text-align: center;"><img alt="" src="" style="height:142px; width:267px"></p>

<p>러한 레저and 쇠막대기of 배치는 nextand 같 괄호 용하여 왼쪽from in order 표현can.</p>

<ol>
	<li>레저는 여는 괄호and 닫는 괄호of 인접한 쌍 ‘( ) ’ with 표현된다. 또한, all ‘( ) ’는 반드시 레저 표현한다.</li>
	<li>쇠막대기of 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다. </li>
</ol>

<p>위 예of 괄호 표현은 그림 위in 주어져 exists.</p>

<p>쇠막대기는 레저in of해 몇 of 조eachwith 잘려지는데, 위 예in 장 위in 있는 두 of 쇠막대기는 eacheach 3and 2of 조eachwith 잘려지고, and 같은 방식with given 쇠막대기들은 총 17of 조eachwith 잘려진다. </p>

Write a program to find <p>쇠막대기and 레저of 배치 나타내는 괄호 표현 when given, 잘려진 쇠막대기 조eachof 총 number.</p>

### Input 

 <p>in one line, 쇠막대기and 레저of 배치 나타내는 괄호 표현 공백없 are given. 괄호 문자of number는 maximum 100,000다. </p>

### Output 

 <p>잘려진 조eachof 총 number 나타내는 integer in one line, Output한다.</p>

