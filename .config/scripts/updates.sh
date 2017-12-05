#!/bin/bash
pac=$(checkupdates | wc -l)
aur=$(cower -u | wc -l)

check=$((pac + aur))
if [[ "$check" != "0" ]]
then
    echo "$pac %{F#c0a79a}%{F-} $aur"
else
		echo "0 %{F#c0a79a}%{F-} 0"
fi
