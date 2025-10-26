<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Gold IV] Tree의 지름 - 1967 

[Problem Link](https://www.acmicpc.net/problem/1967) 

### Performance Summary

Memory: 37992 KB, Time: 64 ms

### Classification

Graph Theory, Graph Traversal, Tree, Depth-First Search, Tree의 지름

### Submission Date

2025-10-27 00:32:53

### Problem Description

<p>Tree(tree)는 사클 없는 무방향 그래프다. Treein는 some 두 node 선택해도 둘 사in path 항상 하나만 존재하게 된다. Treein some 두 node 선택해서 양쪽with 쫙 당길 when, 장 길게 늘어나는 경우 있 것다. 럴 when Treeof all node들은  두 node 지름of 끝 pointwith 하는 원 안in 들어게 된다.</p>

<p><img alt="" height="123" src="https://www.acmicpc.net/JudgeOnline/upload/201007/ttrrtrtr.png" width="310"></p>

<p>런 두 node 사of pathof length Treeof 지름(called). 정확히 정of하자면 Treein 존재하는 all path들 among longest 것of length 말한다.</p>

<p>Inputwith 루트 있는 Tree among치 있는 edge들로 줄 when, Treeof 지름 구해서 Output하는 프로그램 작성하시오. belowand 같은 Tree are given면 Treeof 지름은 45 된다.</p>

<p><img alt="" height="152" src="https://www.acmicpc.net/JudgeOnline/upload/201007/tttttt.png" width="312"></p>

<p>Treeof node는 1from nto 호 매겨져 exists.</p>

### Input 

 <p>파일of 첫  줄은 nodeof number n(1 ≤ n ≤ 10,000)다. 둘 lines onwards, n-1lines, each edgein 대한 정보 들어온다. edgein 대한 정보는 세 of integer로 루어져 exists. 첫  integer는 edge 연결하는 두 node among 부모 nodeof 호 나타내고, 두  integer는 자식 node, 세  integer는 edgeof among치 나타낸다. edgein 대한 정보는 부모 nodeof 호 작은 것 먼저 Input되고, 부모 nodeof 호 같으면 자식 nodeof 호 작은 것 먼저 Input된다. 루트 nodeof 호는 항상 1라고 정하며, edgeof among치는 100보다 크지 않은 양of integer다.</p>

### Output 

 <p>In the first line, Treeof 지름 Output한다.</p>

