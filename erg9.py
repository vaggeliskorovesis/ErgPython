import string
import math

f = open("sample.txt", "r")
a = f.read()
a = a.translate(str.maketrans('', '', string.punctuation))
#print (a)
a = " ".join(a)
#print(a)
new_a = [ord(count) for count in a]
#print (new_a)

sum = 0
A , a = 0 , 0
C , c = 0 , 0
E , e = 0 , 0
G , g = 0 , 0
I , i = 0 , 0
K , k = 0 , 0
M , m = 0 , 0
O , o = 0 , 0
Q , q = 0 , 0
S , s = 0 , 0
U , u = 0 , 0
W , w = 0 , 0
Y , y = 0 , 0
for count in new_a :
    if count != 32 and count % 2 :
        sum += 1
        if count == 65 :
            A += 1
        elif count == 97 :
            a += 1
        elif count == 67 :
            C += 1
        elif count == 99 :
            c += 1
        elif count == 69 :
            E += 1
        elif count == 101 :
            e += 1
        elif count == 71 :
            G += 1
        elif count == 103 :
            g += 1
        elif count == 73 :
            I += 1
        elif count == 105 :
            i += 1
        elif count == 75 :
            K += 1
        elif count == 107 :
            k += 1
        elif count == 77 :
            M += 1
        elif count == 109 :
            m += 1
        elif count == 79 :
            O += 1
        elif count == 111 :
            o += 1
        elif count == 81 :
            Q += 1
        elif count == 113 :
            q += 1
        elif count == 83 :
            S += 1
        elif count == 115 :
            s +=1
        elif count == 85 :
            U += 1
        elif count == 117 :
            u += 1
        elif count == 87 :
            W += 1
        elif count == 119 :
            w += 1
        elif count == 89 :
            Y += 1
        elif count == 121 :
            y += 1

print("A: ", math.ceil((A/sum)*100)*"*")
print("a: ", math.ceil((a/sum)*100)*"*")
print("C: ", math.ceil((C/sum)*100)*"*")
print("c: ", math.ceil((c/sum)*100)*"*")
print("E: ", math.ceil((E/sum)*100)*"*")
print("e: ", math.ceil((e/sum)*100)*"*")
print("G: ", math.ceil((G/sum)*100)*"*")
print("g: ", math.ceil((g/sum)*100)*"*")
print("I: ", math.ceil((I/sum)*100)*"*")
print("i: ", math.ceil((i/sum)*100)*"*")
print("K: ", math.ceil((K/sum)*100)*"*")
print("k: ", math.ceil((k/sum)*100)*"*")
print("M: ", math.ceil((M/sum)*100)*"*")
print("m: ", math.ceil((m/sum)*100)*"*")
print("O: ", math.ceil((O/sum)*100)*"*")
print("o: ", math.ceil((o/sum)*100)*"*")
print("Q: ", math.ceil((Q/sum)*100)*"*")
print("q: ", math.ceil((q/sum)*100)*"*")
print("S: ", math.ceil((S/sum)*100)*"*")
print("s: ", math.ceil((s/sum)*100)*"*")
print("U: ", math.ceil((U/sum)*100)*"*")
print("u: ", math.ceil((u/sum)*100)*"*")
print("W: ", math.ceil((W/sum)*100)*"*")
print("W: ", math.ceil((w/sum)*100)*"*")
print("Y: ", math.ceil((Y/sum)*100)*"*")
print("y: ", math.ceil((y/sum)*100)*"*")


f.close()
