<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Bronze III] 대지 - 9063 

[Problem Link](https://www.acmicpc.net/problem/9063) 

### Performance Summary

Memory: 36352 KB, Time: 1344 ms

### Classification

Mathematics, Implementation, 기하학

### Submission Date

2025-10-26 21:53:17

### Problem Description

<p> 임씨는 1950 년 한국전쟁with 많은 손해 본 사람들 among 하나다. 전쟁 통in 손해보지 않은 사람 어디 있까 만은 그는 6.25  일어나기 전만 해도 충청도 지방in 넓은 대지 소유한 큰 부자였다. 전쟁 나자 임씨는 땅문서and 값 나는 것들만 챙겨서 일본with 피난 지만 피난 amongin 그만 땅문서 잃어버리고 만다. 전쟁 끝난 후in 임씨of 땅은 미 다른 사람들of 논밭 되어 있었고, 임씨는 땅 되찾으려 했지만 문서 없으니 생떼 쓰는 것and 다 바 없었다. 러다 임씨는 길바닥in 나앉게 생겼다.</p>

<p>when, 임씨in게 좋은 생each 떠올랐으니 바로 자신 습관처럼 땅 깊숙 뭔 표식 해놓았던 사실다. 임씨는 한적할 when마다 자신of 논밭 거닐다 땅속 깊은 곳in 자신of 름 씌어진 옥구슬 묻어놓았던 것다. 즉, some 지pointin 그of 름 적힌 옥구슬 나온다면 그 지point은 예전in 임씨of 땅었다는 것 증명하는 것다.</p>

<p>임씨는 즉시 민사소송 통해 자신of 땅 찾고자 했고 논리적인 근거 들어 옥구슬 나오는 지point 원래 자신of 땅of 한 지point었다는 것 주장하여 결국 담당판사 설득하는 데in 성공하였다. 담당판사는 nextand 같은 판결 내렸다. “ 6.25 전of 인소유 대지들은 99% 남북, 동서 방향with 평행한 직사each형 모양었으므로, 임씨of 름 새겨진 옥구슬 나오는 all 지point 포함하는 smallest 남북, 동서 방향with 평행한 변 갖는 직사each형of 대지 임씨of 소유로 인정한다.” 임씨는 많은 손해 보는 셈but 더 상 요구할 만한 근거 없었기 when문in  판결 따르기로 했다.</p>

<p>임씨of 름 새겨진 옥구슬of position N  주어질 whenin, 임씨in게 돌아갈 대지of 넓 계산하는 프로그램 작성하시오. 단, 옥구슬of position는 2 차원 integer 좌표로 are given and 옥구슬은 같은 positionin 여러  발견될 수도 있으며, x 축of 양of방향 동쪽, y 축of 양of방향 북쪽라고 정한다. </p>

<p><img alt="" src="" style="height:182px; width:500px"></p>

<p>For example 위and 같 (2, 1), (3, 2), (5, 2), (3, 4) 네 pointin 옥구슬 발견하였다면, 임씨in게 돌아갈 대지는 (2, 1), (5, 1), (2, 4), (5, 4) 네 꼭짓pointwith 하는 직사each형며, 넓는 (5 - 2) × (4 - 1) = 9  된다. </p>

### Input 

 <p>In the first line,는 pointof number N (1 ≤ N ≤ 100,000)  are given. 어지는 N 줄in는 each pointof 좌표 두 of integer로 in one line, one by one are given. each 좌표는 -10,000 상 10,000 하of integer다. </p>

### Output 

 <p>In the first line, N of point 둘러싸는 minimum sizeof 직사each형of 넓 Output하시오. </p>

