<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver III] 단어 뒤집기 2 - 17413 

[Problem Link](https://www.acmicpc.net/problem/17413) 

### Performance Summary

Memory: 34908 KB, Time: 220 ms

### Classification

Implementation, 자료 구조, String, Stack

### Submission Date

2025-04-28 16:38:59

### Problem Description

<p>String S when given,  Stringin 단어만 뒤house으려고 한다.</p>

<p>먼저, String S는 belowandand 같은 rule 지킨다.</p>

<ol>
	<li>알파벳 소문자('<code>a</code>'-'<code>z</code>'), 숫자('<code>0</code>'-'<code>9</code>'), 공백('<code> </code>'), 특수 문자('<code><</code>', '<code>></code>')로만 루어져 exists.</li>
	<li>Stringof 시작and 끝은 공백 is not.</li>
	<li>'<code><</code>'and '<code>></code>' Stringin 있는 경우 갈아면서 등장하며, '<code><</code>' 먼저 등장한다. 또, 두 문자of number는 같다.</li>
</ol>

<p>태그는 '<code><</code>'로 시작해서 '<code>></code>'로 끝나는 length 3 상인 부분 String고, '<code><</code>'and '<code>></code>' 사in는 알파벳 소문자and 공백만 exists. 단어는 알파벳 소문자and 숫자로 루어진 부분 String고, 연속하는 두 단어는 공백 하나로 구분한다. 태그는 단어 아니며, 태그and 단어 사in는 공백 does not exist.</p>

### Input 

 <p>In the first line, String S are given. Sof length는 100,000 하다.</p>

### Output 

 <p>In the first line, String Sof 단어 뒤house어서 Output한다.</p>

