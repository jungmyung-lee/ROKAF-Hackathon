<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver I] 스티커 - 9465 

[Problem Link](https://www.acmicpc.net/problem/9465) 

### Performance Summary

Memory: 44004 KB, Time: 596 ms

### Classification

Dynamic Programming

### Submission Date

2025-10-26 21:53:50

### Problem Description

<p>상근of 여동생 상냥는 문방구in 스티커 2n 구매했다. 스티커는 그림 (a)and 같 2행 n열로 배치되어 exists. 상냥는 스티커 용해 책상 꾸미려고 한다.</p>

<p>상냥 구매한 스티커of 품질은 매우 좋지 않다. 스티커 한 장 떼면, 그 스티커and 변 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다. 즉, 뗀 스티커of 왼쪽, 오른쪽, 위, belowin 있는 스티커는 사용할 수 없게 된다.</p>

<p><img alt="" src="" style="height:150px; width:575px"></p>

Write a program to find <p>all 스티커 붙일 수 없게된 상냥는 each 스티커in point수 매기고, point수of 합 maximum 되게 스티커 떼어내려고 한다. 먼저, 그림 (b)and 같 each 스티커in point수 매겼다. 상냥 뗄 수 있는 스티커of point수of maximum value. 즉, 2nof 스티커 among point수of 합 maximum 되면서 서로 변 공유 하지 않는 스티커 house합 구해야 한다.</p>

<p>위of 그림of 경우in point수 50, 50, 100, 60인 스티커 고르면, point수는 260 되고  것 maximum point수다. 장 높은 point수 지는 두 스티커 (100and 70)은 변 공유하기 when문in, 동시in 뗄 수 does not exist.</p>

### Input 

 <p>In the first line, 테스트 케스of number T are given. each 테스트 케스of In the first line,는 n (1 ≤ n ≤ 100,000) are given. next 두 줄in는 nof integer 주어지며, each integer는 그 positionin 해당하는 스티커of point수다. 연속하는 두 integer 사in는 빈 칸 하나 exists. point수는 0보다 크거나 같고, 100less than or equal to integer다. </p>

### Output 

 <p>each 테스트 케스 마다, 2nof 스티커 among 두 변 공유하지 않는 스티커 point수of maximum value Output한다.</p>

