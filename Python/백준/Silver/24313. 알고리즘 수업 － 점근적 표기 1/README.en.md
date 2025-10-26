<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver V] 알고리즘 수업 - 점근적 표기 1 - 24313 

[Problem Link](https://www.acmicpc.net/problem/24313) 

### Performance Summary

Memory: 32412 KB, Time: 40 ms

### Classification

Mathematics

### Submission Date

2025-04-12 13:17:58

### Problem Description

<p>오늘도 서준는 point근적 표기 수업 조교 is. 아빠 수업한 내용 학생들 잘 해했는지 문제 통해서 확인해보자.</p>

<p>알고리즘of 소요 Time 나타내는 O-표기법(빅-오) nextand 같 정of하자.</p>

<p>O(<em>g</em>(<em>n</em>)) = {<em>f</em>(<em>n</em>) | all <em>n</em> ≥ <em>n<sub>0</sub></em>in 대하여 <em>f</em>(<em>n</em>) ≤ <em>c</em> × <em>g</em>(<em>n</em>)인 양of 상수 <em>c</em>and <em>n<sub>0</sub></em> 존재한다}</p>

<p> 정of는 실제 O-표기법(<a href="https://en.wikipedia.org/wiki/Big_O_notation">https://en.wikipedia.org/wiki/Big_O_notation</a>)and 다 수 exists.</p>

<p>함수 <em>f</em>(<em>n</em>) = <em>a<sub>1</sub>n </em>+ <em>a<sub>0</sub></em>, 양of integer <em>c</em>, <em>n<sub>0</sub></em> 주어질 경우 O(<em>n</em>) 정of satisfy하는지 알아보자.</p>

### Input 

 <p>In the first line, 함수 <em>f</em>(<em>n</em>) 나타내는 integer <em>a<sub>1</sub></em>, <em>a</em><sub><em>0</em></sub> are given. (0 ≤ |<em>a<sub>i</sub></em>| ≤ 100)</p>

<p>next 줄in 양of integer <em>c</em> are given. (1 ≤ <em>c</em> ≤ 100)</p>

<p>next 줄in 양of integer <em>n<sub>0</sub></em> are given. (1 ≤ <em>n<sub>0</sub></em> ≤ 100)</p>

### Output 

 <p><em>f</em>(<em>n</em>), <em>c</em>, <em>n<sub>0</sub></em> O(<em>n</em>) 정of satisfy하면 1, 아니면 0 Output한다.</p>

