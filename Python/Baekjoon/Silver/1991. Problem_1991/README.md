# [Silver I] Tree 순회 - 1991 

[Problem Link](https://www.acmicpc.net/problem/1991) 

### Performance Summary

Memory: 32412 KB, Time: 32 ms

### Classification

Tree, 재귀

### Submission Date

2025-10-27 00:28:34

### Problem Description

<p>이진 Tree를 Input받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 Output하는 프로그램을 작성하시오.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/JudgeOnline/upload/201007/trtr.png" style="height:220px; width:265px"></p>

<p>예를 들어 위와 같은 이진 Tree가 Input되면,</p>

<ul>
	<li>전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)</li>
	<li>중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)</li>
	<li>후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)</li>
</ul>

<p>가 된다.</p>

### Input 

 <p>첫째 줄에는 이진 Tree의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.</p>

### Output 

 <p>첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 Output한다. 각 줄에 N개의 알파벳을 공백 없이 Output하면 된다.</p>

