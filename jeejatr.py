#5 (e) Count the occurences of each word in a line of text.
text = "mango pineapple mango pineapple papaya"
words = text.split()

wcount = {}
for word in words :
    wcount[word] = wcount.get(word, 0) + 1

print(wcount)

#5 (f) Create a list of colors from comma - separated color names entered by user. Display first and last colors.
clist=input("Enter the colors separated by commas: ")
colors=clist.split(",")
if colors:
    print(f"first color: {colors[0].strip()}")
    print(f"last color: {colors[-1].strip()}")

## (g) print out all colors in color_list1 not contained in color_list2
color_list1=["Red", 'Green',"Blue","Purple","White","Black"]
color_list2=["Red", 'Green',"Blue","Purple"]
result=[color for color in color_list1 if color not in color_list2]
print(result)

## (h) create a single string separated with space from two strings by swapping the character at position 1
s1=input("Enter first string: ")
s2=input("Enter second string: ")

new_s1=s2[0] + s1[1] + s1[2:]
new_s2=s1[0] + s2[1] + s2[2:]

result=new_s1 + " " + new_s2
print(result)

## (i) to store and display the contents of the dictionary
a={
    "name":"Akash",
    "age":23,
}
print(a)

## (j) sort dictionary in ascending and descending order

a = {'s':45, 'd':15, 'f':978, 'g':12, 'h':75}
ascending = dict(sorted(a.items()))
descending = dict(sorted(a.items(), reverse=True))
print(f"ascending order:", ascending)
print(f"descending order:", descending)

## (k) merge two dictionaries
dict1={"a":1,"b":2}
dict2={"b":99,"c":3}
merged= dict1|dict2
print(merged)

## (a) program to find the factorial of a number
a=int(input("Enter a number: "))
if a<0:
    print("avoid negative numbers")
else:
    f=1
    for i in range(1,a+1):
        f*=i
    print(f)

## (b) generate a fibanocci series of N terms

N=int(input("Enter the number of terms: "))
a,b=0,1

for i in range(N):
    print(a, end=" ")
    a,b=b,a+b

## (c) Find the sum of all items in a list

a=[10,56,12,478,511]
s=0
for i in a:
    s+=i
print(s)

## (d) generate a list of 4 digit numbers in a given range with all thier digits even and the number is a perfect square
import math

def even_digit_square_numbers(low, high):
    result = []
    start = math.isqrt(low)
    end = math.isqrt(high)

    for n in range(start, end + 1):
        sq = n * n
        if low <= sq <= high:
            if all(int(ch) % 2 == 0 for ch in str(sq)):
                result.append(sq)

    return result

print(even_digit_square_numbers(1000, 9999))
