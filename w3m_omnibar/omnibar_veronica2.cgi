#!/usr/bin/env sh
GOPHER_PROTOCOL_ENABLE=$(w3m -version | grep -c "gopher")
echo "w3m-control: BACK"
if [ "$GOPHER_PROTOCOL_ENABLE" = 0 ] ; then
  echo "w3m-control: TAB_GOTO https://gopher.floodgap.com/gopher/gw?ss=gopher%3A%2F%2Fgopher.floodgap.com%2F7%2Fv2%2Fvs&sq=$QUERY_STRING"
else
  echo "w3m-control: TAB_GOTO gopher://gopher.floodgap.com/7/v2/vs?$QUERY_STRING"
fi
