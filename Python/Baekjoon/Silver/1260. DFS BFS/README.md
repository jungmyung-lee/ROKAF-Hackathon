# [Silver II] DFS와 BFS - 1260 

[Problem Link](https://www.acmicpc.net/problem/1260) 

### Performance Summary

Memory: 35376 KB, Time: 64 ms

### Classification

Graph Theory, Graph Traversal, Breadth-First Search, Depth-First Search

### Submission Date

2025-04-27 16:47:15

### Problem Description

<p>그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 Output하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.</p>

### Input 

 <p>첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. Input으로 주어지는 간선은 양방향이다.</p>

### Output 

 <p>첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 Output한다. V부터 방문된 점을 순서대로 Output하면 된다.</p>

