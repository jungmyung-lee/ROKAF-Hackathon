# [Silver IV] 덱 - 10866 

[Problem Link](https://www.acmicpc.net/problem/10866) 

### Performance Summary

Memory: 32412 KB, Time: 44 ms

### Classification

Implementation, 자료 구조, 덱

### Submission Date

2025-04-13 18:48:39

### Problem Description

<p>정수를 저장하는 덱(Deque)를 Implementation한 다음, Input으로 주어지는 명령을 처리하는 프로그램을 작성하시오.</p>

<p>명령은 총 여덟 가지이다.</p>

<ul>
	<li>push_front X: 정수 X를 덱의 앞에 넣는다.</li>
	<li>push_back X: 정수 X를 덱의 뒤에 넣는다.</li>
	<li>pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 Output한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 Output한다.</li>
	<li>pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 Output한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 Output한다.</li>
	<li>size: 덱에 들어있는 정수의 개수를 Output한다.</li>
	<li>empty: 덱이 비어있으면 1을, 아니면 0을 Output한다.</li>
	<li>front: 덱의 가장 앞에 있는 정수를 Output한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 Output한다.</li>
	<li>back: 덱의 가장 뒤에 있는 정수를 Output한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 Output한다.</li>
</ul>

### Input 

 <p>첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.</p>

### Output 

 <p>Output해야하는 명령이 주어질 때마다, 한 줄에 하나씩 Output한다.</p>

