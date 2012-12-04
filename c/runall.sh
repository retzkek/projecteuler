#!/bin/zsh
{
	for src in eu*.c; do
		case=${src%.c}
		echo "Problem $case"
		echo "-------------"
		echo
		echo "::"
		echo
		make $case | awk '{printf("    %s\n",$0)}'
		echo "    time ./$case.bin"
		(time ./$case.bin)  &> tmp
		echo "    "
		cat tmp | awk '{printf("    %s\n",$0)}'
		echo
	done
} &> README.rst
