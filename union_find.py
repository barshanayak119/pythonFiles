# Program implementing Union Find (disjoint sets)
# Per Union Time Complexity : O(n), overall O(n^2)
def union(arr,a,b):
	a1=arr[a]
	b1=arr[b]
	for i in range(len(arr)):
		if arr[i]==a1:
			arr[i]=b1

def find(arr,a,b):
	if arr[a]==arr[b]:
		return True
	else:
		return False

vertex=[0,1,2,3,4,5,6]
edges=[(1,0),(1,3),(4,6),(2,6)]
for edge in edges:
	union(vertex,edge[0],edge[1])
print(vertex)
print(find(vertex,1,5))

