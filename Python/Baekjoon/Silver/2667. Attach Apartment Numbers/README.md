# [Silver I] 단지번호붙이기 - 2667 

[Problem Link](https://www.acmicpc.net/problem/2667) 

### Performance Summary

Memory: 32488 KB, Time: 36 ms

### Classification

Graph Theory, Graph Traversal, Breadth-First Search, Depth-First Search, 격자 그래프, 플러드 필

### Submission Date

2025-04-23 18:53:39

### Problem Description

<p><그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 Input하여 단지수를 Output하고, 각 단지에 속하는 집의 수를 오름차순으로 Sorting하여 Output하는 프로그램을 작성하시오.</p>

<p style="text-align: center;"><img alt="" src="" style="height:192px; width:409px"></p>

### Input 

 <p>첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 Input되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 Input된다.</p>

### Output 

 <p>첫 번째 줄에는 총 단지수를 Output하시오. 그리고 각 단지내 집의 수를 오름차순으로 Sorting하여 한 줄에 하나씩 Output하시오.</p>

