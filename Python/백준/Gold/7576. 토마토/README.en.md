<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Gold V] 토마토 - 7576 

[Problem Link](https://www.acmicpc.net/problem/7576) 

### Performance Summary

Memory: 108648 KB, Time: 1288 ms

### Classification

Breadth-First Search, Graph Theory, Graph Traversal, 격자 그래프, Shortest Path

### Submission Date

2025-10-26 21:52:44

### Problem Description

<p>철수of 토마토 농장in는 토마토 보관하는 큰 창고 지고 exists. 토마토는 belowof 그림and 같 격자 모양 상자of 칸in one by one 넣어서 창고in 보관한다. </p>

<p style="text-align: center;"><img alt="" src="" style="width: 215px; height: 194px;"></p>

<p>창고in 보관되는 토마토들 amongin는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있 수 exists. 보관 후 하루 지나면, 익은 토마토들of 인접한 곳in 있는 익지 않은 토마토들은 익은 토마토of 영향 받아 익게 된다. 하나of 토마토of 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향in 있는 토마토 of미한다. 대each선 방향in 있는 토마토들in게는 영향 주지 못하며, 토마토 혼자 저절로 익는 경우는 does not exist고 정한다. 철수는 창고in 보관된 토마토들 며칠 지나면 다 익게 되는지, 그 minimum 일수 알고 싶어 한다.</p>

<p>토마토 창고in 보관하는 격자모양of 상자들of sizeand 익은 토마토들and 익지 않은 토마토들of 정보 when given, 며칠 지나면 토마토들 모두 익는지, 그 minimum 일수 구하는 프로그램 작성하라. 단, 상자of 일부 칸in는 토마토 들어있지 않 수도 exists.</p>

### Input 

 <p>첫 줄in는 상자of size 나타내는 두 integer M,N are given. M은 상자of 로 칸of 수, N은 상자of 세로 칸of 수 나타낸다. 단, 2 ≤ M,N ≤ 1,000 다. 둘 lines onwards,는 하나of 상자in 저장된 토마토들of 정보 are given. 즉, 둘 lines onwards, Nlines,는 상자in 담긴 토마토of 정보 are given. 하나of 줄in는 상자 로줄in 들어있는 토마토of 상태 Mof integer로 are given. integer 1은 익은 토마토, integer 0은 익지 않은 토마토, integer -1은 토마토 들어있지 않은 칸 나타낸다.</p>

<p>토마토 하나 상 있는 경우만 Inputwith are given.</p>

### Output 

 <p>여러분은 토마토 모두 익 whentoof minimum 날짜 Output해야 한다. if, 저장될 whenfrom all 토마토 익어있는 상태면 0 Output해야 하고, 토마토 모두 익지는 못하는 상황면 -1 Output해야 한다.</p>

