import string

f = open("sample.txt", "r")
a = f.read()
a = a.translate(str.maketrans('', '', string.punctuation))
#print (a)
a = " ".join(a)
#print(a)
new_a = [ord(count) for count in a]
#print (new_a)

for count in range(len(new_a)) :
   if new_a[count] != 32 :
       new_a[count] = 128 - new_a[count]
#print(new_a)

new_a.reverse()
#print (new_a)
for count in range(len(new_a)) :
        if new_a[count] != 32 :
            conv = [chr(count) for count in new_a]
#print (conv)
conv1 = ''.join([str(i) for i in conv])
print (conv1)
f.close()
