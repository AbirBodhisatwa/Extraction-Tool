# S1 : source diry, full pathname,  for all resume files in various formats
# $2 : destination diry, full pathname,  for all converted txt files
# start by moving to dir $1; add a check for existence of this dir 
cd "$1"
# examine each file in this dir and take action based on file type
for i in *
do
# examine $i; split filename in two parts around the IFS dot(.)
   IFS='.' read -ra array <<< "$i"
   first=${array[0]}
   last=${array[1]}
   tmp=temp.txt
   file="$first"".txt"
   echo "first = $first last = $last filename = $i"
  # action based on file extension type : doc; docx; pdf; txt; others
   if [ "$last" == "doc" ] || [ "$last" == "docx" ]
   then
      doc2pdf "$i"
      echo "doc2tmp works"
      pdftotext -layout "$first.pdf" 
      iconv -c -f utf8 -t ascii < "$first.txt" > "$tmp"
      tr -d '\000-\011\013\014\016-\037' < "$tmp" > "../$2/$file" 
      rm -f "$first.pdf" "$first.txt" "$tmp"
#  else
#  if [ "$last" == "docx" ]
#  then
#      doc2pdf "$i"
#      pdftotext -layout "$i" 
#      iconv -c -f utf8 -t ascii < "$first.txt" > "$tmp"
#      tr -d '\000-\011\013\014\016-\037' < "$tmp" > "$2/$file" 
  else
  if [ "$last" == "pdf" ]
  then
      pdftotext -layout "$i" 
      iconv -c -f utf8 -t ascii < "$first.txt" > "$tmp"
      ls -l $tmp; echo $PWD; 
      tr -d '\000-\011\013\014\016-\037' < "$tmp" > "../$2/$file" 
      rm -f "$first.txt" "$tmp"
  else
  if [ "$last" == "txt" ]
  then
      iconv -c -f utf8 -t ascii < "$i" > "$tmp"
      tr -d '\000-\011\013\014\016-\037' < "$tmp" > "../$2/$file" 
      rm "$tmp"
  else
     echo unknown type "$last" not converted
  fi
  fi
  fi
#  fi
done
exit;
