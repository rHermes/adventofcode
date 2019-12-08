#!/bin/bash

tr -d '\n' \
	| split -b 150 - --filter 'grep -o . | sort | uniq -c | sed "s/^ *//;s/ *[0-9]* *$//" | xargs -n3 echo' \
	| sort -n \
	| head -1 \
	| cut -d' ' -f2,3 \
	| tr ' ' '*' \
	| bc
