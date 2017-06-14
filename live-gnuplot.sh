while read line; do
	lines="$lines$line\n"
	echo "plot \"-\""
	echo -n $lines
	echo "e"
done


