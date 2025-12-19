# [Gold IV] Bipartite Graph - 1707 

[Problem Link](https://www.acmicpc.net/problem/1707) 

### Performance Summary

Memory: 53888 KB, Time: 1200 ms

### Classification

Graph Theory, Graph Traversal, Breadth-First Search, Depth-First Search, Bipartite Graph

### Submission Date

2025-10-26 21:40:38

### Problem Description

<p>그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 Bipartite Graph (Bipartite Graph) 라 부른다.</p>

<p>그래프가 Input으로 주어졌을 때, 이 그래프가 Bipartite Graph인지 아닌지 판별하는 프로그램을 작성하시오.</p>

### Input 

 <p>Input은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. </p>

### Output 

 <p>K개의 줄에 걸쳐 Input으로 주어진 그래프가 Bipartite Graph이면 YES, 아니면 NO를 순서대로 Output한다.</p>

