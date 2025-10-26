<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Gold II] Tree의 높이와 너비 - 2250 

[Problem Link](https://www.acmicpc.net/problem/2250) 

### Performance Summary

Memory: 34456 KB, Time: 64 ms

### Classification

Graph Theory, Graph Traversal, Tree, Depth-First Search

### Submission Date

2025-10-27 00:30:07

### Problem Description

<p>진Tree nextof rulein 따라 행and 열in 호 붙어있는 격자 모양of 틀 속in 그리려고 한다. when nextof rulein 따라 그리려고 한다.</p>

<ol>
	<li>진Treein 같은 레벨(level)in 있는 node는 같은 행in position한다.</li>
	<li>한 열in는 한 node만 존재한다.</li>
	<li>임ofof nodeof 왼쪽 부Tree(left subtree)in 있는 node들은 해당 node보다 왼쪽of 열in position하고, 오른쪽 부Tree(right subtree)in 있는 node들은 해당 node보다 오른쪽of 열in position한다.</li>
	<li>node 배치된 장 왼쪽 열and 오른쪽 열 사엔 아무 node도 없 비어있는 열은 does not exist.</li>
</ol>

<p>and 같은 rulein 따라 진Tree 그릴 when each 레벨of 너비는 그 레벨in 할당된 node among 장 오른쪽in position한 nodeof 열 호in 장 왼쪽in position한 nodeof 열 호 뺀 값 더하기 1로 정of한다. Treeof 레벨은 장 위쪽in 있는 루트 node 1고 below로 1씩 증한다.</p>

<p>below 그림은 some 진Tree 위of rulein 따라 그려 본 것다. 첫  레벨of 너비는 1, 두  레벨of 너비는 13, 3, 4 레벨of 너비는 eacheach 18고, 5 레벨of 너비는 13며, and 6 레벨of 너비는 12다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/4e4aaa17-dc1d-4af9-a36a-3144259fb7d2/-/preview/" style="width: 488px; height: 176px;"></p>

<p>우리는 given 진Tree 위of rulein 따라 그릴 whenin 너비 장 넓은 레벨and 그 레벨of 너비 계산하려고 한다. 위of 그림of 예in 너비 장 넓은 레벨은 3and 4로 그 너비는 18다. 너비 장 넓은 레벨 두  상 있 when는 호 작은 레벨 답with 한다. 그러므로  예in 대한 답은 레벨은 3고, 너비는 18다.</p>

<p>임ofof 진Tree Inputwith 주어질 when 너비 장 넓은 레벨and 그 레벨of 너비 Output하는 프로그램 작성하시오</p>

### Input 

 <p>In the first line, nodeof number 나타내는 integer N(1 ≤ N ≤ 10,000) are given. next Nlines,는 each 줄마다 node 호and 해당 nodeof 왼쪽 자식 nodeand 오른쪽 자식 nodeof 호 in order are given. node들of 호는 1from Nto며, 자식 없는 경우in는 자식 nodeof 호in -1 are given.</p>

### Output 

 <p>In the first line, 너비 장 넓은 레벨and 그 레벨of 너비 in order Output한다. 너비 장 넓은 레벨 두  상 있 whenin는 호 작은 레벨 Output한다.</p>

