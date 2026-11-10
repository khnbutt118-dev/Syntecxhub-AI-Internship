"""A* maze solver with Manhattan heuristic; 0=open, 1=wall."""
import heapq
from pathlib import Path
import matplotlib.pyplot as plt
GRID=[[0,0,0,1,0,0],[1,1,0,1,0,1],[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,0,0,0,0]]
START=(0,0);GOAL=(4,5)
def h(a,b):return abs(a[0]-b[0])+abs(a[1]-b[1])
def astar(grid,start,goal):
 rows,cols=len(grid),len(grid[0])
 if grid[start[0]][start[1]] or grid[goal[0]][goal[1]]:return None
 q=[(h(start,goal),0,start)];came={};g={start:0};seen=set()
 while q:
  _,cost,node=heapq.heappop(q)
  if node in seen:continue
  seen.add(node)
  if node==goal:
   path=[node]
   while node in came:node=came[node];path.append(node)
   return path[::-1],seen
  for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
   nxt=(node[0]+dr,node[1]+dc)
   if not(0<=nxt[0]<rows and 0<=nxt[1]<cols) or grid[nxt[0]][nxt[1]]:continue
   ng=cost+1
   if ng<g.get(nxt,float("inf")):
    came[nxt]=node;g[nxt]=ng;heapq.heappush(q,(ng+h(nxt,goal),ng,nxt))
 return None,seen
if __name__=="__main__":
 result,visited=astar(GRID,START,GOAL);print("Visited:",len(visited))
 if result:
  print("Shortest path length:",len(result)-1,"Path:",result)
  plt.imshow(GRID,cmap="Greys");ys=[p[0] for p in result];xs=[p[1] for p in result];plt.plot(xs,ys,"r-o");plt.scatter([START[1],GOAL[1]],[START[0],GOAL[0]],c=["green","blue"]);plt.gca().invert_yaxis();plt.title("A* Maze demo");plt.savefig(Path(__file__).parent/"maze_path.png")
 else:print("No path exists.")
 # unreachable case test
 print("Unreachable test:",astar([[0,1],[1,0]],(0,0),(1,1))[0])
