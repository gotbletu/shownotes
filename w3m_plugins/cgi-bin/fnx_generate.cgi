#!/usr/bin/env sh
# generate w3m functions to proper formatting for fzf menu
cat /usr/share/doc/w3m/README.func | while read -r line; do 
  func_name="$(echo "$line" | awk '{print $1;}')"
  description="$(echo "$line" | awk '{for (i=2; i<NF; i++) printf $i " "; print $NF}')"
  echo "${func_name}#@${func_name}\\\$#-- ${description}"
done
