# Advent of code

My solutions, in various languages, mostly python.

I write more detailed notes in the commit messages!

## Task notes

### 2021

#### 4

Second time I've placed on the leaderboard, but my best ranking so far!
55 on part one and 41 on part two!


#### 5

I actually managed to place on the leaderboard here for part one! Number 49!
I got a bit slow on the second part, so I ended up getting 107 rank there.

#### 8

This was a good task and in the solutions thread there are some really interesting solutions!

You can do masking and frequency analysis. It's important to mention that we
know that we have one of each digit on each line, this allows us to make many
assumptions.

#### 9

Simple task, but I managed to get on the leaderboard for part two! I got the
100th spot, which is quite funny. I'm stoked to place either way :D

### 2020

The first year I placed, just on a single task, and also the first year I had
an informal contest with Stensrud. This was awesome and it was real close!
The tasks this year was not that good sadly :/


#### 4

This task is very practical, maybe the most practical one of all the tasks in
AoC that I've solved so far. It also turned out very clean when I cleaned it up :)

#### 8

Real times where 00:05:49.26 for part 1 and 00:04:43.44 for part 2, for a total
of 00:10:32.7. I wouldn't have gotten on the leaderboards, but just noting it down.

#### 10

Very cool to be able to solve this with tribonacci!

#### 13

Part 2 of this day was the first good task this year and I really liked it!

#### 20

Best task of the year so far, even if it is sort of simple once you know the trick.

#### 21

First time I placed on the leaderboard in AoC, with 89 on part one and 83 on part two.
The task is quite ok.

#### 23

Had to use C++ for this one, python didn't quite cut it.

### 2019

My first year and still the best year I've done so far. The use of intcode throughout
was mega awesome and the tasks where difficult!

#### 12

I got frustrated and read the hint that the axis are independent. Felt bad
about this one, since I could have puzzled this out, but I guess I learned
a lesson about what the real fun is.

#### 13

I ended up reverse engineering this task, using my own dissassembler and
everything! It was beyond awesome, one of the tasks I'm the proudest about.

#### 16

Had to get a hint about area summation tables to finish it.

#### 18

Had to copy a solution to get it done. Learned a lot.

#### 22

Had to get the explanation about how it worked from redditor. Learned a lot
by doing this.

### Year 2017

#### Day 10

I liked this task, not because it was so difficult, but because it was novel to
implement a hashing algorithm.

#### Day 16

Nice task, which includes loop detection.

#### Day 23

Requires reverse engineering the algorithm in a small ISA program. Very fun!

### Year 2016


#### Day 11

This one took a long time to get right, it ended up being my "hash" implementation
for the "State" that made it not work.

I'm proud that I was able to solve this without looking anything up. Coming up with the
heuristic and such was very nice.

#### Day 12

The `solve_with_c_compiler.py` file includes a solution that transpiles the input
to C and then compiles the program and executes it. Due to the loop being set, the
compiler is able to optimize it away.

This is pretty cool :)


### Year 2015

#### Day 19

For part two I used `Lark` to create a solution. It's a robust and fast solution
to all inputs, even malicously crafted ones.

## Personal Stats

### 2021

```
      --------Part 1--------   -------Part 2--------
Day       Time   Rank  Score       Time  Rank  Score
  9   00:04:03    150      0   00:10:31   100      1
  8   00:06:39    650      0   01:24:50  3815      0
  7   00:08:07   3423      0   00:09:12  1480      0
  6   00:04:01    290      0   00:07:37   232      0
  5   00:04:01     49     52   00:09:04   107      0
  4   00:07:08     55     46   00:09:02    41     60
  3   01:04:09  14883      0   01:13:03  7981      0
  2   00:01:47    158      0   00:05:41  1272      0
  1   00:01:13    142      0   00:03:12   183      0
```

### 2020

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 25   00:14:07    790      0   00:14:14    658      0
 24   00:26:31   1560      0   00:33:54    760      0
 23   00:20:36    523      0   01:28:49    935      0
 22   00:13:48   1801      0   00:55:02   1498      0
 21   00:11:06     89     12   00:15:12     83     18
 20   03:26:09   3552      0   13:45:26   4073      0
 19   00:28:37    516      0   01:16:27    964      0
 18   00:30:32   1523      0   00:43:14   1196      0
 17   00:35:06   1426      0   00:43:08   1397      0
 16   00:08:48    258      0   00:23:15    145      0
 15   00:13:08    916      0   00:13:58    329      0
 14   00:20:37   1622      0   02:36:01   5622      0
 13   00:05:29    311      0   01:21:29   2157      0
 12   00:46:57   5644      0   00:56:39   3695      0
 11   00:16:06    665      0   00:26:48    647      0
 10   00:44:05   8561      0   01:03:06   3448      0
  9   00:04:17    276      0   00:07:16    148      0
  8   02:26:23  14118      0   02:31:06  11216      0
  7   00:09:42    160      0   00:14:45    136      0
  6   00:06:51   2075      0   00:13:39   2134      0
  5   00:28:39   5190      0   00:35:20   4589      0
  4   00:06:13    483      0   00:19:12    376      0
  3   00:06:02   1000      0   00:08:34    620      0
  2   00:05:45    954      0   00:08:40    763      0
  1   00:07:01    127      0   00:07:46    112      0
```

### 2019

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 25   01:39:49    557      0   01:40:10    420      0
 24   00:12:34    136      0   01:14:46    347      0
 23   00:37:06    464      0   01:51:11    751      0
 22   17:56:55   3428      0       >24h   1600      0
 21   05:24:35   1519      0   05:35:29   1184      0
 20       >24h   2877      0       >24h   2207      0
 19   04:48:56   2542      0   07:17:19   2013      0
 18   07:49:09    820      0       >24h   2824      0
 17   03:50:55   2736      0       >24h   5109      0
 16       >24h   6725      0       >24h   6038      0
 15   02:00:38    895      0   02:06:07    685      0
 14   03:26:48   1413      0   05:23:54   1538      0
 13   03:34:19   4093      0       >24h   6761      0
 12   00:15:40    282      0   00:47:01    216      0
 11   00:16:03    244      0   00:21:24    218      0
 10   01:00:44   1216      0   01:33:00    623      0
  9   00:43:45    893      0   00:44:17    839      0
  8   00:47:02   2534      0   01:17:53   2494      0
  7   05:49:39   5995      0   06:10:53   3290      0
  6   04:59:55   7225      0   05:06:23   6073      0
  5       >24h  17587      0       >24h  16129      0
  4   00:04:35    316      0   00:11:06    396      0
  3   00:16:58    374      0   00:20:46    275      0
  2   00:25:03   1991      0   00:32:32   1467      0
  1   07:47:10  10793      0   07:54:00   9515      0
```
