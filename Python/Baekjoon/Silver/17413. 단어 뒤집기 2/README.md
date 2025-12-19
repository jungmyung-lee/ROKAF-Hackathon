# [Silver III] 단어 뒤집기 2 - 17413 

[Problem Link](https://www.acmicpc.net/problem/17413) 

### Performance Summary

Memory: 34908 KB, Time: 220 ms

### Classification

Implementation, 자료 구조, String, Stack

### Submission Date

2025-04-28 16:38:59

### Problem Description

<p>String S가 주어졌을 때, 이 String에서 단어만 뒤집으려고 한다.</p>

<p>먼저, String S는 아래와과 같은 규칙을 지킨다.</p>

<ol>
	<li>알파벳 소문자('<code>a</code>'-'<code>z</code>'), 숫자('<code>0</code>'-'<code>9</code>'), 공백('<code> </code>'), 특수 문자('<code><</code>', '<code>></code>')로만 이루어져 있다.</li>
	<li>String의 시작과 끝은 공백이 아니다.</li>
	<li>'<code><</code>'와 '<code>></code>'가 String에 있는 경우 번갈아가면서 등장하며, '<code><</code>'이 먼저 등장한다. 또, 두 문자의 개수는 같다.</li>
</ol>

<p>태그는 '<code><</code>'로 시작해서 '<code>></code>'로 끝나는 길이가 3 이상인 부분 String이고, '<code><</code>'와 '<code>></code>' 사이에는 알파벳 소문자와 공백만 있다. 단어는 알파벳 소문자와 숫자로 이루어진 부분 String이고, 연속하는 두 단어는 공백 하나로 구분한다. 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.</p>

### Input 

 <p>첫째 줄에 String S가 주어진다. S의 길이는 100,000 이하이다.</p>

### Output 

 <p>첫째 줄에 String S의 단어를 뒤집어서 Output한다.</p>

