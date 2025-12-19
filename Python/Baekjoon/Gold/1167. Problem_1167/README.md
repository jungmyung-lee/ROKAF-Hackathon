# [Gold II] Tree의 지름 - 1167 

[Problem Link](https://www.acmicpc.net/problem/1167) 

### Performance Summary

Memory: 88856 KB, Time: 480 ms

### Classification

Graph Theory, Graph Traversal, Tree, Depth-First Search, Tree의 지름

### Submission Date

2025-10-27 00:33:34

### Problem Description

<p>Tree의 지름이란, Tree에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. Tree의 지름을 구하는 프로그램을 작성하시오.</p>

### Input 

 <p>Tree가 Input으로 주어진다. 먼저 첫 번째 줄에서는 Tree의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.</p>

<p>먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 Input으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.</p>

### Output 

 <p>첫째 줄에 Tree의 지름을 Output한다.</p>

