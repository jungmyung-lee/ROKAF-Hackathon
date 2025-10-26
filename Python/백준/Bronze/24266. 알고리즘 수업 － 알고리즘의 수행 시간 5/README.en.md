<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Bronze III] 알고리즘 수업 - 알고리즘의 수행 Time 5 - 24266 

[Problem Link](https://www.acmicpc.net/problem/24266) 

### Performance Summary

Memory: 32412 KB, Time: 36 ms

### Classification

Mathematics, Implementation, Simulation

### Submission Date

2025-04-10 20:31:14

### Problem Description

<p>오늘도 서준는 알고리즘of 수행Time 수업 조교 is. 아빠 수업한 내용 학생들 잘 해했는지 문제 통해서 확인해보자.</p>

<p>Inputof size <em>n</em> 주어지면 MenOfPassion 알고리즘 수행 Time 예제 Outputand 같은 방식with Output해보자.</p>

<p>MenOfPassion 알고리즘은 nextand 같다.</p>

<pre>MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}</pre>

### Input 

 <p>In the first line, Inputof size <em>n</em>(1 ≤ <i>n</i> ≤ 500,000) are given.</p>

### Output 

 <p>In the first line, 코드1 of 수행 횟수 Output한다.</p>

<p>In the second line, 코드1of 수행 횟수 다항식with 나타내었 when, 최고차항of 차수 Output한다. 단, 다항식with 나타낼 수 없거나 최고차항of 차수 3보다 크면 4 Output한다.</p>

