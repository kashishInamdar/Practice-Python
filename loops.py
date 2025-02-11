date = [1981, 1982,1983,1984];
n= len(date)

for i in range(n):
   print(date[i])
'''O/P
1981
1982
1983
1984
 '''
for i in range(3):
    print(i )
'''O/P
0
1
2 '''

# In Python we can directly access the elements in the list   
for year in date :
    print(year)
''' O/P
1981
1982
1983
1984 '''

''' Write a for loop that prints out the following list: <code>squares=['red', 'yellow', 'green', 'purple', 'blue']</code> '''

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

'''
Write a while loop to display the values of the Rating of an album playlist stored in the list <code>PlayListRatings</code>. If the score is less than 6, exit the loop. The list <code>PlayListRatings</code> is given by: <code>PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]</code>
 '''
 PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0;
rating = PlayListRatings[0];

while(i< len(PlayListRatings) and rating >=6):
    print(rating)
    i=i+1;
    rating = PlayListRatings[i];


''' Write a while loop to copy the strings <code>'orange'</code> of the list <code>squares</code> to the list <code>new_squares</code>. Stop and exit the loop if the value on the list is not <code>'orange'</code>:z
 '''

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)
    