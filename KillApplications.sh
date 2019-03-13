#!/bin/bash

#Contains a list of applications that should all be closed
#Checks if the application has any processes that are currently running
#if there are applications open kill them
#if there is no instances open display a message to terminal
#Tell the terminal when the process is complete
#(this is a simple modular for a larger project)

#list of applications (update as needed)
declare -a List_Of_Applications=("Google Chrome" "Preview" "Excel" "iTunes" "OneNote"  "java" "WhatsApp" "Messages" "Atom") 

#Message to terminal
echo ""
echo "---Clearing Current Applications---"
echo ""

for element in "${List_Of_Applications[@]}"
do
	#Message to terminal
	echo ""
	echo "---Searching for $element---"
	
	#checks if current Application is running
	Application_Open=$(ps -Ac | grep "$element")
	
	#if open tell terminal and close it
	#else tell terminal it is not running
	if [ ! -z "$Application_Open" ]; then
		Application_To_Kill=$(ps -Ac | pgrep "$element")
		echo "---Killing "$element"---"
		kill $Application_To_Kill
		echo "---"$element" Killed Successful---"
	else
		echo "---"$element" Currently Not Running---"
	fi
done
