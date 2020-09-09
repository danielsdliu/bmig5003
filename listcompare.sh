#!/bin/bash

echo 'How many integers do you have?'
read total

list=""
COUNTER=0

while [ $COUNTER -lt $total ]; do
  let count=COUNTER+1
  echo 'Enter integer #'$count':'
  read value
  list=`echo "$list $value"` #combines values entered into a string separated by spaces
  let COUNTER=COUNTER+1
done

#  bash didn't seem to like sorting a string versus multiple lines so
#+ I used transform to give each entry it's own line.  Then I sorted
#+ or reverse sorted the value and stored it in a list to compare it to.

list_asc=`echo $list|tr " " "\n"|sort|tr "\n" " "`
list_desc=`echo $list|tr " " "\n"|sort -r|tr "\n" " "`

flist=`echo $list|tr " " "\n"|tr "\n" " "`

#  I had issues comparing the original with the transformed strings even
#+ though they were visually identical.  I think there's an extra null
#+ space at the end of the transformed but couldn't find a way to remove it
#+ so I just used the same string transformation on the original string
#+ to create something to compare the sorted versions to.

if [ "$flist" = "$list_asc" ]; then
  echo Your list is in ascending order.
elif [ "$flist" = "$list_desc" ]; then
  echo Your list is in descending order.
else
  echo Your list is unordered.
fi