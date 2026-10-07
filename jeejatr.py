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
