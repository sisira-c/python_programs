str="abcabcdababc"
max_length=0
start=0
char_index={}
for i in range(len(str)):
     char=str[i]
     if char in char_index and char_index[char]>=start:
         start=char_index[char]+1
     char_index[char]=i
     current_length=i-start+1
     if current_length>max_length:
          max_length=current_length
print("length of the longest substring:",max_length)          

              