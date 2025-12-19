# [Bronze III] 알고리즘 수업 - 알고리즘의 수행 Time 3 - 24264 

[Problem Link](https://www.acmicpc.net/problem/24264) 

### Performance Summary

Memory: 32412 KB, Time: 36 ms

### Classification

Mathematics, Implementation, 사칙연산, 시뮬레이션

### Submission Date

2025-04-10 18:42:17

### Problem Description

<p>오늘도 서준이는 알고리즘의 수행Time 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p>Input의 크기 <em>n</em>이 주어지면 MenOfPassion 알고리즘 수행 Time을 Example Output과 같은 방식으로 Output해보자.</p>

<p>MenOfPassion 알고리즘은 다음과 같다.</p>

<pre>MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}</pre>

### Input 

 <p>첫째 줄에 Input의 크기 <em>n</em>(1 ≤ <i>n</i> ≤ 500,000)이 주어진다.</p>

### Output 

 <p>첫째 줄에 코드1 의 수행 횟수를 Output한다.</p>

<p>둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 Output한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 Output한다.</p>

