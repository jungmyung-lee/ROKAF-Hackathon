<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver I] 나무 탈출 - 15900 

[Problem Link](https://www.acmicpc.net/problem/15900) 

### Performance Summary

Memory: 179516 KB, Time: 1872 ms

### Classification

Graph Theory, Graph Traversal, Tree, Depth-First Search

### Submission Date

2025-04-22 23:18:12

### Problem Description

<p>평소in 사 좋지 않던 성원and 형석 드디어 제대로 한 판 붙으려고 한다. 성원and 형석 둘and 모두 똑같 친한 인섭 대결 종목 정해 져왔다. 바로 '나무 탈출' 라는 보드게임다.</p>

<p>'나무 탈출' 은 Nof vertex 있는 Tree 모양with 생긴 게임판and 몇 of 게임말로 루어진다. Treeof each vertexin는 1from Nto 호 붙어exists. 1 vertex은 '루트 node' 라고 불리며,  루트 node among심with vertex 간in 부모-자식 관계 만들어진다. 자식 없는 node는 '리프 node' 라고 불린다.</p>

<p> 게임은 두 사람 갈아 면서 게임판in 놓여있는 게임말 움직는 게임다. 처음in는 Treeof all 리프 nodein 게임말 one by one 놓여있는 채로 시작한다. some 사람of 차례 오면, 그 사람은 current 존재하는 게임말 among 아무거나 하나 골라 그 말 놓여있던 nodeof 부모 node로 옮긴다.  and정in 한 nodein 여러 of 게임말 놓게 될 수도 exists. 렇게 옮긴 후in if 그 게임말 루트 nodein 도착했다면 그 게임말 즉시 제거한다. all and정 마치면 next 사람in게 차례 넘긴다. 런 식with 계속 진행하다 게임말 게임판in 존재하지 않아 고 수 없는 사람 지게 된다.</p>

<p>성원 얕본 형석는 쿨하게  게임of 선 성원in게 줘버렸다. 따라서 성원 먼저 시작하고 형석 나amongin 시작한다. 그동안 형석and 대결 하면 매 지기만 했던 성원는 마음속in 분노 득 쌓였다.  대결in는 반드시 겨서 형석of 코 꺾어주고 싶다. 그래서 게임 시작하기 전in 게임판of 모양만 보고  게임 길 수 있지 미리 알아보고 싶어졌다. 성원  게임 길 수 있지 없지 알려주는 프로그램 만들어 성원 도and주자.</p>

### Input 

 <p>In the first line, Treeof vertex number N(2 ≤ N ≤ 500,000) are given.</p>

<p>둘 lines onwards, N-1줄in 걸쳐 Treeof edge 정보 are given. 줄마다 두of natural number a, b(1 ≤ a, b ≤ N, a ≠ b) 주어지는데, 는 aand b 사in edge 존재한다는 뜻다.</p>

### Output 

 <p>성원 최선 다했 when  게임 길 수 있으면 <code>Yes</code>, 아니면 <code>No</code> Output한다.</p>

