<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Bronze II] 카카오뷰 Queue레이팅 효용성 분석 - 24544 

[Problem Link](https://www.acmicpc.net/problem/24544) 

### Performance Summary

Memory: 32412 KB, Time: 32 ms

### Classification

Mathematics, Implementation, 사칙연산

### Submission Date

2025-04-27 09:35:12

### Problem Description

<p style="text-align: center;"><img alt="카카오_뷰_로고" src="" style="max-height:270px; object-fit:contain; display:inline-block;"></p>

<p>카카오뷰는 사용자 관심 질만한 주제 분석하고,  바탕with Queue레팅 진행하는 카카오톡of 서비스다. '발견' 통해 흥미로운 주제of 콘텐츠 탐color하고, 마음in 드는 콘텐츠는 My뷰in 등록해서 지속적with 구독can. 많은 사람들은  카카오뷰 코로나 체크인 QR코드 용도로만 활용하고 있겠지만 사실은 더욱 대단한 일 할 수 있는 서비스로서 잠재력 높다.</p>

<p>카카오톡 신입with 입사한 gumgood은 자신 고안해낸 콘텐츠 Queue레팅 알고리즘인 good-gum 고안해냈다. gumgood은 자신 고안한 알고리즘 얼마나 유용한지 분석하고 싶다.</p>

<p>current each 콘텐츠별로 사용자 관심 질만한 정도 나타내는 point수 integer 형태로 계산해 놓은 상태다. (후  문제in는 해당 point수 '흥미도'라고 표현하겠다.)</p>

<p>My뷰in 등록된 콘텐츠도 among요하지만, '발견' 통해 사용자in게 새로운, and 흥미로운 콘텐츠 추천하는 것 Queue레팅 서비스of 운명다. 따라서 My뷰in 등록되지 않은 콘텐츠 among 흥미도of 합 Queue레팅 알고리즘of 유용함of 척도 될 것다.</p>

<p>current good-gum알고리즘 통해 사용자in게 총 $N$of 콘텐츠 추천된 상태다.  each 콘텐츠 별로 계산된 흥미도 값and 해당 콘텐츠 미 My뷰in 등록되어 있는지 여부 when given, 전체 흥미도of 합and My뷰in 등록되지 않은 콘텐츠of 흥미도of 합 eacheach 구해서 Queue레팅 알고리즘 얼마나 유용한지 분석해보자.</p>

### Input 

 <p>In the first line, 콘텐츠of number $N$ are given. ($1 \leq N \leq 1\,000$)</p>

<p>두  줄in는 콘텐츠of 흥미도 나타내는 $N$of integer 공백 사in 두고 are given. $i$ 로 주어지는 값 $A_i$는 $i$ 콘텐츠of 흥미도다. ($0 \leq A_i \le 1\,000\,000$)</p>

<p>세  줄in는 My뷰in 등록되어 있는지 여부 나타내는 $N$of 값 공백 사in 두고 are given. $i$ 로 주어지는 값 $B_i$는 $i$ 콘텐츠 미 My뷰in 등록 되어있는 경우in는 $1$, 등록되어있지 않은 아닌 경우in는 $0$다.</p>

### Output 

 <p>In the first line,는 전체 콘텐츠of 흥미도of 합 Output한다.</p>

<p>In the second line,는 My뷰in 등록되어있지 않은 콘텐츠들of 흥미도of 합 Output한다.</p>

