<!-- Official English translation (US) — human-reviewed -->
<!-- Original: README.md -->
<!-- Translation generated: 2025-10-26 16:46:49 UTC -->

# [Bronze III] 최댓값 - 2566 

[Problem Link](https://www.acmicpc.net/problem/2566) 

### Performance Summary

Memory: 32412 KB, Time: 32 ms

### Classification

Implementation

### Submission Date

2025-04-07 14:24:08

### Problem Description

<p><그림 1>and 같 9×9 격자판in 쓰여진 81of natural number or 0 주어질 when, 들 among maximum value 찾고 그 maximum value 몇 행 몇 열in position한 수인지 구하는 프로그램 작성하시오.</p>

<p>For example, nextand 같 81of 수 주어지면</p>

<table class="table table-bordered td-center th-center table-center-40">
	<tbody>
		<tr>
			<th> </th>
			<th>1열</th>
			<th>2열</th>
			<th>3열</th>
			<th>4열</th>
			<th>5열</th>
			<th>6열</th>
			<th>7열</th>
			<th>8열</th>
			<th>9열</th>
		</tr>
		<tr>
			<th>1행</th>
			<td>3</td>
			<td>23</td>
			<td>85</td>
			<td>34</td>
			<td>17</td>
			<td>74</td>
			<td>25</td>
			<td>52</td>
			<td>65</td>
		</tr>
		<tr>
			<th>2행</th>
			<td>10</td>
			<td>7</td>
			<td>39</td>
			<td>42</td>
			<td>88</td>
			<td>52</td>
			<td>14</td>
			<td>72</td>
			<td>63</td>
		</tr>
		<tr>
			<th>3행</th>
			<td>87</td>
			<td>42</td>
			<td>18</td>
			<td>78</td>
			<td>53</td>
			<td>45</td>
			<td>18</td>
			<td>84</td>
			<td>53</td>
		</tr>
		<tr>
			<th>4행</th>
			<td>34</td>
			<td>28</td>
			<td>64</td>
			<td>85</td>
			<td>12</td>
			<td>16</td>
			<td>75</td>
			<td>36</td>
			<td>55</td>
		</tr>
		<tr>
			<th>5행</th>
			<td>21</td>
			<td>77</td>
			<td>45</td>
			<td>35</td>
			<td>28</td>
			<td>75</td>
			<td>90</td>
			<td>76</td>
			<td>1</td>
		</tr>
		<tr>
			<th>6행</th>
			<td>25</td>
			<td>87</td>
			<td>65</td>
			<td>15</td>
			<td>28</td>
			<td>11</td>
			<td>37</td>
			<td>28</td>
			<td>74</td>
		</tr>
		<tr>
			<th>7행</th>
			<td>65</td>
			<td>27</td>
			<td>75</td>
			<td>41</td>
			<td>7</td>
			<td>89</td>
			<td>78</td>
			<td>64</td>
			<td>39</td>
		</tr>
		<tr>
			<th>8행</th>
			<td>47</td>
			<td>47</td>
			<td>70</td>
			<td>45</td>
			<td>23</td>
			<td>65</td>
			<td>3</td>
			<td>41</td>
			<td>44</td>
		</tr>
		<tr>
			<th>9행</th>
			<td>87</td>
			<td>13</td>
			<td>82</td>
			<td>38</td>
			<td>31</td>
			<td>12</td>
			<td>29</td>
			<td>29</td>
			<td>80</td>
		</tr>
	</tbody>
</table>

<p>들 among maximum value은 90고,  값은 5행 7열in position한다.</p>

### Input 

 <p>첫 lines onwards, 아홉  줄to in one line, 아홉 씩 수 are given. 주어지는 수는 100보다 작은 natural number or 0다.</p>

### Output 

 <p>In the first line, maximum value Output하고, In the second line, maximum value position한 행 호and 열 호 빈칸 사in 두고 차례로 Output한다. maximum value 두  상인 경우 그 among 한 곳of position Output한다.</p>

