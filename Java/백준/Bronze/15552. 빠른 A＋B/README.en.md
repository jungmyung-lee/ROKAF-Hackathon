<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Bronze IV] 빠른 A+B - 15552 

[Problem Link](https://www.acmicpc.net/problem/15552) 

### Performance Summary

Memory: 236856 KB, Time: 768 ms

### Classification

Implementation, 사칙연산, Mathematics

### Submission Date

2025-05-04 13:05:10

### Problem Description

<p>본격적with for문 문제 풀기 전in 주of해야 할 point exists. 입Output 방식 느리면 여러 줄 Input받거나 Output할 when Time초and 날 수 exists는 point다.</p>

<p>C++ 사용하고 exist and <code>cin</code>/<code>cout</code> 사용하고자 한다면, <code>cin.tie(NULL)</code>and <code>sync_with_stdio(false)</code> 둘 다 적용해 주고, <code>endl</code> 대신 행문자(<code>\n</code>) 쓰자. 단, 렇게 하면 더 상 <code>scanf</code>/<code>printf</code>/<code>puts</code>/<code>getchar</code>/<code>putchar</code> 등 Cof 입Output 방식 사용하면 안 된다.</p>

<p>Java 사용is면, <code>Scanner</code>and <code>System.out.println</code> 대신 <code>BufferedReader</code>and <code>BufferedWriter</code> 사용can. <code>BufferedWriter.flush</code>는 맨 마지막in 한 만 하면 된다.</p>

<p>Python 사용is면, <code>input</code> 대신 <code>sys.stdin.readline</code> 사용can. 단, when는 맨 끝of 행문자to 같 Input받기 when문in String 저장하고 싶 경우 <code>.rstrip()</code> 추로 해 주는 것 좋다.</p>

<p>또한 Inputand Output 스트림은 별므로, 테스트케스 전부 Input받아서 저장한 뒤 전부 Output할 필요는 does not exist. 테스트케스 하나 받은 뒤 하나 Output해도 된다.</p>

<p>자세한 설명 및 다른 언어of 경우는 <a href="http://www.acmicpc.net/board/view/22716"> 글</a>in 설명되어 exists.</p>

<p><a href="http://www.acmicpc.net/blog/view/55"> 블로그 글</a>in BOJof 기타 여러 지 팁 볼 수 exists.</p>

### Input 

 <p>첫 줄in 테스트케스of number T are given. T는 maximum 1,000,000다. next T줄in는 eacheach 두 integer Aand B are given. Aand B는 1 상, 1,000 하다.</p>

### Output 

 <p>each 테스트케스마다 A+B in one line, one by one in order Output한다.</p>

