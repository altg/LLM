#!/bin/zsh
grep -v -e '^[[:space:]]*$' -e '^#' -e '-->' $1 | sed -e 's/<\/v>//g' -e  's/<v //' -e 's/>/: /g'


 
