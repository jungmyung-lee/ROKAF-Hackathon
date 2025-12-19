# [Silver I] 나이트의 이동 - 7562 

[Problem Link](https://www.acmicpc.net/problem/7562) 

### Performance Summary

Memory: 34984 KB, Time: 1128 ms

### Classification

Breadth-First Search, Graph Theory, Graph Traversal, Shortest Path, 격자 그래프

### Submission Date

2025-04-23 15:20:45

### Problem Description

<p>체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?</p>

<p><img alt="" src="" style="height:172px; width:175px"></p>

### Input 

 <p>Input의 첫째 줄에는 테스트 케이스의 개수가 주어진다.</p>

<p>각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.</p>

### Output 

 <p>각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 Output한다.</p>

