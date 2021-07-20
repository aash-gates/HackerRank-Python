K = int(input())

#Step 1
roomList = list(map(int,input().split()))

#Step 2
roomSet = set(roomList) 

#Step 3
sumRoomSet = sum(roomSet) 
sumRoomList = sum(roomList) 

# Step 4
temp = sumRoomSet * K - sumRoomList 

# Step 5
answer = temp / (K - 1) 

# Step 6
print(answer)