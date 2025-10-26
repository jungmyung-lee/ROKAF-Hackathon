<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver I] Tree 순회 - 1991 

[Problem Link](https://www.acmicpc.net/problem/1991) 

### Performance Summary

Memory: 32412 KB, Time: 32 ms

### Classification

Tree, 재귀

### Submission Date

2025-10-27 00:28:34

### Problem Description

<p>진 Tree Input받아 전위 순회(preorder traversal), among위 순회(inorder traversal), 후위 순회(postorder traversal)한 결and Output하는 프로그램 작성하시오.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/JudgeOnline/upload/201007/trtr.png" style="height:220px; width:265px"></p>

<p>For example 위and 같은 진 Tree Input되면,</p>

<ul>
	<li>전위 순회한 결and : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)</li>
	<li>among위 순회한 결and : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)</li>
	<li>후위 순회한 결and : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)</li>
</ul>

<p> 된다.</p>

### Input 

 <p>In the first line,는 진 Treeof nodeof number N(1 ≤ N ≤ 26) are given. 둘 lines onwards, Nlines, 걸쳐 each nodeand 그of 왼쪽 자식 node, 오른쪽 자식 node are given. nodeof 름은 Afrom 차례대로 알파벳 대문자로 매겨지며, 항상 A 루트 node 된다. 자식 node 없는 경우in는 .with 표현한다.</p>

### Output 

 <p>In the first line, 전위 순회, In the second line, among위 순회, In the third line, 후위 순회한 결and Output한다. in each line, Nof 알파벳 공백 없 Output하면 된다.</p>

