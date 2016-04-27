#!/bin/bash
# Weaving with simple math in terminal
# https://bitbucket.org/livibetter/weave.sh
# Copyright (c) 2013 Yu-Jie Lin
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


VERSION=0.1.0

# Characters and colors for vertical and horizontal lines
: ${char_v:='|'}            ${char_h:='-'}
: ${color_v:='\e[32;1m'}    ${color_h:='\e[31;1m'}

# Sleep delays
: ${sleep_v:=0.01}          ${sleep_h:=0.01}
: ${sleep_end:=5}

: ${eval_h:="$1"}           Get evaluation code from '$1'
: ${eval_h:='(((x+y)%2))'}  , or set to a default pattern
: ${show_eval_h:=no}        "yes" to print out evaluation code

W=$(tput cols)              H=$(tput lines)


draw_v() {
  local line y
  printf -v line '%*s' $W ; line=${line// /$char_v}
  for ((y=1; y<=H; y++)); do
    echo -ne "\e[${y};1H${color_v}${line}"
    sleep $sleep_v
  done
}


draw_h() {
  local x y
  for ((x=1; x<=W; x++)); do
    for ((y=1; y<=H; y++)); do
      eval "$eval_h" && echo -ne "\e[${y};${x}H${color_h}${char_h}"
    done
    sleep $sleep_h
  done
}


main() {
  clear
  draw_v
  draw_h
  [[ $show_eval_h == yes ]] && echo -ne "\e[$H;1H\e[0m${eval_h:0:$W}"
  sleep $sleep_end
}


main
