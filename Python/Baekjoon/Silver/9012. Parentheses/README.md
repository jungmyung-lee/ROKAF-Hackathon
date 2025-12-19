# [Silver IV] 괄호 - 9012 

[Problem Link](https://www.acmicpc.net/problem/9012) 

### Performance Summary

Memory: 32412 KB, Time: 40 ms

### Classification

자료 구조, String, Stack

### Submission Date

2025-10-26 21:53:11

### Problem Description

<p>괄호 String(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 String이다. 그 중에서 괄호의 모양이 바르게 구성된 String을 올바른 괄호 String(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” String은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 String “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 String xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 String이다. </p>

<p>여러분은 Input으로 주어진 괄호 String이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. </p>

### Input 

 <p>Input 데이터는 표준 Input을 사용한다. Input은 T개의 테스트 데이터로 주어진다. Input의 첫 번째 줄에는 Input 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 String이 한 줄에 주어진다. 하나의 괄호 String의 길이는 2 이상 50 이하이다. </p>

### Output 

 <p>Output은 표준 Output을 사용한다. 만일 Input 괄호 String이 올바른 괄호 String(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 Output해야 한다. </p>

