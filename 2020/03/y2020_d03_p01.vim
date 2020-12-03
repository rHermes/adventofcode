" Written as what you would type in.
" Space where it is pressed not in a string will be shown with <SPACE>

:%s/#/a/g <ENTER>		" Replace all # with a. We are going to use this for toggling the case
gg						" go to top again
<CTRL-V> G $ y			" Select all the text
$
300p	" insert the pasted blocks 300 times

G o<ESC> " insert a new line so when we reach the end of the pattern we don't fack up

gg " Go to top

ql " record macro to l 
~jll " toggle the case and move one down two right
q "stop recording macro

500@l " apply the macro 500 hundred times, just to be sure

:%s/A//n <ENTER> : Read out the results

" Number of matches will be in the search bar
