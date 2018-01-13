#Solution One:
#head -n 10 file.txt | tail -n +10

#Solution Two:
#awk 'NR==10' file.txt

#Solution Three:
sed -n 10p file.txt