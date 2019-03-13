#!/bin/bash

declare -a List_Of_Applications=("Google Chrome" "Preview" "Excel" "iTunes" "OneNote"  "java" "WhatsApp" "Messages" "Atom") 

echo ""
echo "---Clearing Current Applications---"
echo ""

for element in "${List_Of_Applications[@]}"
do
	
	echo ""
	echo "---Searching for $element---"

	Application_Open=$(ps -Ac | grep "$element")

	if [ ! -z "$Application_Open" ]; then
		Application_To_Kill=$(ps -Ac | pgrep "$element")
		echo "---Killing "$element"---"
		kill $Application_To_Kill
		echo "---"$element" Killed Successful---"
	else
		echo "---"$element" Currently Not Running---"
	fi
done
