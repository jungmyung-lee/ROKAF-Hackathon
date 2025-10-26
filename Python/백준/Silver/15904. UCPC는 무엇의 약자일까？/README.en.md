<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Silver V] UCPC는 무엇의 약자일까? - 15904 

[Problem Link](https://www.acmicpc.net/problem/15904) 

### Performance Summary

Memory: 32412 KB, Time: 36 ms

### Classification

Greedy 알고리즘, String

### Submission Date

2025-04-22 19:55:10

### Problem Description

<p>UCPC는 '전국 대학생 프로그래밍 대회 동아리 연합 여름 대회'of 줄임말로 알려져exists. 하지만  줄임말 정확히 어떻게 구성되었는지는 아무도 모른다. UCPC 2018 준비하던 ntopia는 여러 사람들in게 UCPC 정확히 무엇of 줄임말인지 물어보았지만, 아무도 정확한 답 제시해주지 못했다. ntopia 들은 몇 지 답 belowin 적어보았다.</p>

<ul>
	<li>Union of Computer Programming Contest club contest</li>
	<li>Union of Computer Programming contest Club contest</li>
	<li>Union of Computer Programming contest club Contest</li>
	<li>Union of Collegiate Programming Contest club contest</li>
	<li>Union of Collegiate Programming contest Club contest</li>
	<li>Union of Collegiate Programming contest club Contest</li>
	<li>University Computer Programming Contest</li>
	<li>University Computer Programming Club contest</li>
	<li>University Computer Programming club Contest</li>
	<li>University Collegiate Programming Contest</li>
	<li>University CPC</li>
	<li>...</li>
</ul>

<p>ntopia는 렇게 다양한 답 듣고는 UCPC 무엇of 약자인지는 아무도 모른다고 결론내렸다. 적당히 슥삭해서 UCPC 남길 수 있으면 모두 UCPCof 약자인 것다!</p>

<p>String 주어지면  String 적절히 축약해서 "UCPC"로 만들 수 있는지 확인하는 프로그램 만들어보자.</p>

<p>축약라는 것은 Stringin 임ofof 문자들 제거하는 행동 뜻한다. 예 들면, "apple"in aand e 지워 "ppl"로 만들 수 exist and, "University Computer Programming Contest"in 공백and 소문자 모두 지워 "UCPC"로 만들 수 exists.</p>

<p>String 비교할 when는 대소문자 구분해 정확히 비교한다. For example "UCPC"and "UCpC"는 다른 String다. 따라서 "University Computer programming Contest" "UCPC"로 축약할 수 있는 방법은 does not exist.</p>

<p>그나저나 UCPC는 정말 무엇of 약자였까? 정확히 아시는 분은 제보 부탁드립니다.</p>

### Input 

 <p>In the first line, 알파벳 대소문자, 공백with 구성된 String are given. Stringof length는 maximum 1,000자다. Stringof 맨 앞and 맨 끝in 공백 있는 경우는 없고, 공백 연속해서 2 상 주어지는 경우도 does not exist.</p>

### Output 

 <p>In the first line, Inputwith given String 적절히 축약해 "UCPC"로 만들 수 있으면 "<code>I love UCPC</code>" Output하고, 만들 수 없으면 "<code>I hate UCPC</code>" Output한다.</p>

