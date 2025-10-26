<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Bronze I] 세로읽기 - 10798 

[Problem Link](https://www.acmicpc.net/problem/10798) 

### Performance Summary

Memory: 32412 KB, Time: 32 ms

### Classification

Implementation, String

### Submission Date

2025-04-24 21:21:13

### Problem Description

<p>아직 글 모르는 영석 벽in 걸린 칠판in 자석 붙어있는 글자들 붙는 장난감 지고 놀고 exists. </p>

<p> 장난감in 있는 글자들은 영어 대문자 ‘A’from ‘Z’, 영어 소문자 ‘a’from ‘z’, 숫자 ‘0’from ‘9’다. 영석는 칠판in 글자들 수평with 일렬로 붙여서 단어 만든다. 다시 그 below쪽in 글자들 붙여서 또 다른 단어 만든다. 런 식with 다섯 of 단어 만든다. below 그림 1은 영석 칠판in 붙여 만든 단어들of 예다. </p>

<pre>A A B C D D
a f z z 
0 9 1 2 1
a 8 E W g 6
P 5 h 3 k x</pre>

<p><그림 1></p>

<p>한 줄of 단어는 글자들 빈칸 없 연속with 나열해서 maximum 15of 글자들로 루어진다. 또한 만들어진 다섯 of 단어들of 글자 number는 서로 다 수 exists. </p>

<p>심심해진 영석는 칠판in 만들어진 다섯 of 단어 세로로 읽으려 한다. 세로로 읽 when, each 단어of 첫  글자들 위in below로 세로로 읽는다. nextin 두  글자들 세로로 읽는다. 런 식with 왼쪽in 오른쪽with 한 자리씩 동 하면서 동일한 자리of 글자들 세로로 읽어 나간다. 위of 그림 1of 다섯  자리 보면 두  줄of 다섯  자리of 글자는 does not exist. 런 경우처럼 세로로 읽 when 해당 자리of 글자 없으면, 읽지 않고 그 next 글자 계속 읽는다. 그림 1of 다섯  자리 세로로 읽으면 D1gk로 읽는다. </p>

<p>그림 1in 영석 세로로 읽은 in order 글자들 공백 없 Output하면 nextand 같다:</p>

<p>Aa0aPAf985Bz1EhCz2W3D1gkD6x</p>

<p>칠판in 붙여진 단어들 주어질 when, 영석 세로로 읽은 in order 글자들 Output하는 프로그램 작성하시오.</p>

### Input 

 <p>총 다섯줄of Input are given. in each line,는 minimum 1, maximum 15of 글자들 빈칸 없 연속with are given. 주어지는 글자는 영어 대문자 ‘A’from ‘Z’, 영어 소문자 ‘a’from ‘z’, 숫자 ‘0’from ‘9’ among 하나다. each 줄of 시작and 마지막in 빈칸은 does not exist.</p>

### Output 

 <p>영석 세로로 읽은 in order 글자들 Output한다. when, 글자들 공백 없 연속해서 Output한다. </p>

