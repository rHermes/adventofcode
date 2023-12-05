# Advent of code

My solutions, in various languages, mostly python.

I write more detailed notes in the commit messages!

## Task notes

### 2022

This was a bit of a tame year, but there where some tasks which really had a bit
of kick to them. Day 17, 19 and 22 was quite hard. Especially day 19 was the high
point for me. I think overall the year was too easy, but that has been the trend
for the last few years now.

I only placed on day this year, but I could have placed another one too, if I hadn't
decided to sleep in that day.

This was the first year where I had some real competition from colleagues, which
is really nice.

#### 23

Wasted a loooottttttttt of time on part 1, because I didn't do adjancency correctly and included
the position itself, just not the eight positions around.

Part 1: 00:39:23
Part 2: 00:01:46
Total : 00:41:09

### 22

Part two here is quite cool,  I haven't made this generic yet, I just hardcoded it for
my input. I look forward to seeing how other people solved it.

I got a really bad time on part 2 here, because I made 1 mistake on part one. Just one
fucking letter off, but that was all it took.

I solved it by actually drawing the cube on a piece of paper, and folding that, to figure
out how the edges connected. It was a good move, but I made one typo, and that was all it took.


#### 20

Kind of a cool task, where I had to use bidict to get things working. pypy
made a real difference here, but I know this can be done much faster, if
I just figure out where my bug is in the indexing.

#### 19

Well, fuck me side ways, this was a real hard one! I spent a lot of time trying
to solve both part 1 and part 2 one this one. I had to resort to using something
called "codon" to be able to do this fast enough.

In the beginning I tried to do a normal dynamic programming setup, but it didn't
work, not even for part one. After switching to codon, I was able to get part 1,
with the basic approach, but part two just wouldn't fall.

I actually solved this on a plane to Doha!, 11km up in the air! I also submitted it
there, as there was 1 hour of free wifi! This is really cool, as I have now done it
in -5 degrees in a hammock and on a plane!

One of the breakthroughs was realizing that I could most likely only consider
buying one robot at a time. The text is kind of vague on this, but you can read
from the fact that it says: "We have one fabricator". This allowed me to get
part 1.

For part two, the thing that made it feasible was me dropping the amount of states
I have to discover. The key is that we always just have to think about what
the next robot we are going to build is. And so we only have to consider when
we can do that. The logic goes like this:

If the next robot to build is an ore robot, then it makes no sense to wait longer
than necessary. We gain nothing by doing it later than when we can do it. So we
either buy it right now if we can, or we can skip ahead to a time when we can do
it. This skips a lot of states in between

Even with this, it take a long time, so I'll be interested in seeing how other people
solved this fast!


#### 17

Very nice task, but it's not that hard once you realize what the trick is. One
thing I got stumped on, was the fact that the example input creates no "floors"
like the other inputs does. I initially discarded the idea of using memoization,
because it didn't work on the example.

Once I got that down, it's a matter of reducing the question down to a graph and
then finding the loop step. once your done with that, just just have to do the last
few cycles yourself.

This took some time figuring out, and it also showed the advantage of using typing
in python. It made some of these long types much more managable.


#### 16 LEADERBOARD MOFOS

Well, this was a really nice surprise, given that I would have placed very
well yesterday. It really surprised me that I placed at all here, I didn't
expect it, as I felt rather slow on part 1. For part two, I should have
pivoted to another strategy earlier, but that ended up not happening.

The problem is quite nice, part 1 can be done by simply using good old
memoziation, but part two needs to be done somewhat smarter. I tried
everything I could to find a way, but in the end what ended up working
was calculating the distance between all the nodes and only focusing on
those nodes which had a valve with a rate of more than 0.

This allowed me to skip a lot of the intermediate steps, as there is no
point in moving anywhere, if we are not actually going to open that
valve. I also changed it so that the time is tracked independently for
each player.

I'm sure this can be optimized more, and it still takes a long time,
but I got it in the end.

#### 15 ( WOULD HAVE BEEN LEADERBOARD)

FUUUUUUUUUUUUUUUUUCCCCCCCCCCCCCKKKKKKKKKKKKKKKKKKKKKKK

I decided that on this day I would sleep in, to try to get back on my feet
sleep wise. I thought to myself: "I'm not going to get on the leaderboard
anyway". I guess I should have known better than to jinks myself like that,
but nothing to do about it now. My time was:

Part one: 00:09:19 (Rank 58)
Part two: 00:09:19 (Rank 19)
Total:    00:18:39

I even had a stupid mistake on part one, so I could potentially have gotten 60
seconds earlier than that too.

This one really hurts. But I guess I should just take it with me that I would have
placed on at least one task this year.

The task itself is quite nice. For part 1 I just focused on just the single row,
and in part two I actually used z3 to solve it!

Having read the mega thread, this has a really nice solution!


#### 11

This is both a cool parsing task, but the twist in part two is really enjoyable
here. We have to keep the numbers we are working with small, but how do we do
that? The key is to recognize that since all tests are done with divisibility,
we can use the fact that all operators are the same under modulo to keep them bounded.

I had the gut that this would work, as the problem kind of reminded me of the 
[Chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
which I have done in an earlier task. It turned out to be right. For a more through
explanation, read in that task.

Real time spent on this was:

Part one: 00:25:38
Part two: 00:06:20

#### 9

Interesting task, but not that hard to solve if you don't make any mistakes.

#### 7

Quite a fun task, involves building a filetree and calculating sizes of the
directories. I didn't perform too well on this, but it was very fun :)

### 2021

A year of mostly too simple tasks, but the latter ones where really good.
Especially day 24 was a banger! I placed 4 times this year, which was
awesome! I'm going to continue training, so I might be able to place
higher next year!

This was also the first year where I had more than one private leaderboard!
Pexip ran an internal leaderboard and I was able to place number one there,
which is nice :D

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

#### 11

This one is not so fun, but it's noteworthy, because I coded it in -2 degrees
Celsius, with freezing hands, in the woods. I decided to sleep outside the day
before and I took my laptop with me! I decided I wouldn't wake up on time, since
it would be cold, but I did it once I had woken up and eaten.

#### 14

This was the second ok problem of the year. My placing was bad, but at this point
I care more about getting more good problems.

#### 15

And I placed again! On part two, I got 57 place! I didn't expect this as I was doing
very not so well on part one, but I guess a bunch of factors played in my advantage.
I didn't actually extend the grid, I just calculated the values for each field. I also
noticed that we wrapped back to 1, instead of 0. Instead of trying to figure out how to
do that neatly, I just did it with a range expression.

I got some sad news today, that a winter half marathon I was running got canceled, I
guess this is some sort of consolation price :P

#### 16

Third ok problem of the year, a fun parsing task.

#### 18

Really nice adhoc task! Involves adding together lists with custom rules, quite complex logic.

#### 19

Best task of the year, by a long shot so far. You are trying to triangulate the positon of some
scanners based on their distances to some probes. I had a bad time here, but I had a blast solving it.

#### 20

This was a fun task, which I could have placed very high on, but I made one silly little mistake, that
cost me 1 and a half minutes! Either way, first time this year I felt like I really just
killed the task from the first second!


#### 22

Most challenging task this year, I spent a lot of time on this to try to solve it
with a library and so on, but ended up hacking something together with the
`intervaltree` library.

#### 23

Another banger! It's some mix of a graph problem and a "hanoi" game. I could have solved
part two faster, but I ended up making a mistake, where I didn't update my "done"
function to account for the extra creatures.

#### 24

What a day! One of the best days in AoC history! It's a reverse engineering problem, that I don't
know a general solution for, but instead I've found a solution for my input.


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

### 2023

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  5   00:12:04    355      0   00:35:39    284      0
  4   00:13:34   4916      0   00:21:58   2611      0
  3   05:57:00  28244      0   06:04:21  22241      0
  2   00:10:07   1293      0   00:12:00    878      0
  1   00:01:50    153      0   00:19:10   1624      0
```

### 2022

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 25   00:15:31    510      0   00:15:35    429      0
 24   00:40:18    537      0   00:48:46    555      0
 23   04:25:17   4870      0   04:27:03   4640      0
 22   00:30:35    390      0       >24h   9323      0
 21   00:14:08   1351      0   00:27:44    458      0
 20   01:30:37   2424      0   02:02:29   2507      0
 19       >24h  10912      0       >24h  11056      0
 18   00:05:18    472      0   00:22:46    583      0
 17   00:26:26    140      0       >24h  13817      0
 16   00:16:11     27     74   01:22:08    192      0
 15   05:12:15  12374      0   05:21:36   7458      0
 14   00:15:10    313      0   00:20:04    336      0
 13   00:15:17    494      0   00:21:06    495      0
 12   00:32:54   2296      0   00:49:11   2976      0
 11   00:47:03   4246      0   00:53:23   2183      0
 10   07:07:06  29886      0   07:15:43  25352      0
  9   00:16:01   1168      0   00:27:42   1087      0
  8   00:23:39   4041      0   00:37:11   3218      0
  7   00:30:11   2041      0   00:34:46   1667      0
  6   00:47:59  17337      0   00:49:52  16516      0
  5   00:12:41    925      0   00:13:17    612      0
  4   00:03:28    530      0   00:05:40    640      0
  3   00:05:17    655      0   00:08:25    498      0
  2   00:05:49    667      0   00:08:18    377      0
  1   00:01:47    301      0   00:03:46    663      0
```

### 2021

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 25   00:12:54    303      0   00:12:58    261      0
 24   04:58:40   1901      0   04:59:14   1793      0
 23   00:46:37    703      0   01:39:37    352      0
 22   00:08:03    283      0   03:13:50   2014      0
 21   00:12:49   1096      0   00:25:44    227      0
 20   00:18:35    153      0   00:19:01    102      0
 19   02:47:04   1243      0   02:49:42   1108      0
 18   00:50:48    277      0   00:53:34    251      0
 17   00:11:45    294      0   00:13:29    133      0
 16   00:31:20    399      0   00:38:02    362      0
 15   00:06:59    185      0   00:12:27     57     44
 14   00:06:51    287      0   00:27:04    778      0
 13   00:09:52    353      0   00:11:45    184      0
 12   00:08:41    239      0   00:28:05   1048      0
 11   04:22:30  13127      0   04:24:38  12822      0
 10   00:08:07    971      0   00:12:46    535      0
  9   00:04:03    150      0   00:10:31    100      1
  8   00:06:39    650      0   01:24:50   3815      0
  7   00:08:07   3423      0   00:09:12   1480      0
  6   00:04:01    290      0   00:07:37    232      0
  5   00:04:01     49     52   00:09:04    107      0
  4   00:07:08     55     46   00:09:02     41     60
  3   01:04:09  14883      0   01:13:03   7981      0
  2   00:01:47    158      0   00:05:41   1272      0
  1   00:01:13    142      0   00:03:12    183      0
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
