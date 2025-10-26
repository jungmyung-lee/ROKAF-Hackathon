<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver I] 튜터-튜티 관계의 수 - 24542 

[Problem Link](https://www.acmicpc.net/problem/24542) 

### Performance Summary

Memory: 68692 KB, Time: 472 ms

### Classification

자료 구조, 분리 집합, Graph Theory, Graph Traversal

### Submission Date

2025-04-27 15:29:36

### Problem Description

<p style="text-align: center;"><img alt="" src="" style="height: 333px; width: 466px;"></p>

<blockquote>
<p>퓨처테크아케데미(주)는 올해로 4년 엘리트 알고리즘 SW교육-「헬로알고」라는 브랜드로 <strong>국내는 물론 해외 14국 청소년들 대상with SW교육 실시하고 있는 교육회사</strong>입니다. 또한 among소벤처기업부and 한국교육학술정보원 선정한 '2021비대면스타트업 교육회사', 동국대학교 'SW코딩역량강화캠프 교육회사' 선정 등 <strong>늘 새로운 것in 도전하는 젊은 열정of in듀테크 회사</strong>기도 합니다. 2022 국내외 온·오프라인 사업of 새로운 도전 위해 SW교육 지도 및 컨텐츠 연구발 분야in 함께할 젊고 패기있는 SW인재 찾습니다!</p>
</blockquote>

<p>대학생 찬솔는  학기from 헬로알고in 멘토로 활동하게 되었다. current 찬솔 담당한 반in는 총 $N$명of 교육생 exists.</p>

<p>사전 정보 통해 찬솔는 헬로알고 교육생 간of 친분 관계 나타내는 양방향 그래프 하나 획득할 수 있었다. 정말 특하게도  친분 관계 나타낸 그래프는 포레스트 형태였다. 포레스트란 사클 없는 그래프 of미한다.</p>

<p>찬솔는  교육생 간 친분관계 토대로 교육생들끼리 튜터-튜티 관계 구성하고자 한다. 튜터-튜티 관계는 기존in 친분 관계 있던 두 사람 사in만 정할 수 있으며 단방향with만 지정can.</p>

<p>찬솔 배포한 교육 자료는 튜터 튜티in게만 전달할 수 있도록 하였다. 런 방식with all 교육생in게 교육 자료 전달되어야만 한다. 렇게 되면 부득하게 찬솔로from 최초로 교육 자료 받는 인원 생길 수밖in does not exist. <strong>찬솔는 수줍음 많은 성격기 when문in 런 인원수 minimum 되기 희망한다.</strong></p>

<p>위 조건 while satisfying 교육생of 튜터-튜티 관계 정하는 경우of 수 $1\,000\,000\,007$로 나눈 나머지 Output하자.</p>

### Input 

 <p>교육생of 수 $N$and 친분 관계of 수 $M$ 공백with 구분되어 are given. ($2 \leq N \leq 200\,000$, $1 \leq M \leq N - 1$)</p>

<p>next $M$lines, 친분 관계 맺고 있는 두 교육생인 $u$, $v$ 공백with 구분되어 are given. ($1 \leq u, v \leq N$, $u \neq v$)</p>

<p>교육생of 호는 $1$ 상 $N$ 하of integer며, 주어지는 그래프는 포레스트다.</p>

### Output 

 <p>In the first line, 튜터-튜티 관계 정하는 경우of 수 $1\,000\,000\,007$로 나눈 나머지 Output한다.</p>

