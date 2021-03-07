# Dijkstra算法
# (和最小生成树中的Prim算法比较接近)
# 1.把图中的顶点分为两个集合, 已选集合, 未选集合
# (已选集合初始状态是start顶点)
# 2.每次从已选集合到未选集合之间选取距离最短的边, 并将该边连接的处于未选集合的顶点划入已选集合
# 3.直到终点顶点都处于已选集合则完成
# -------------------实现思路--------------------------
# 维护4个array: node, visited, minDist, parent:
# node   =   [0, 1, 2, 3, 4, 5, 6, 7, 8]    顶点
# visited  = [F, F, F, F, F, F, F, F, F]    顶点是否被访问过
# distance = [inf,inf,inf,inf,inf,inf,inf,inf,inf]    该节点到起点的最短距离
# parent   = [-1,-1,-1,-1,-1,-1,-1,-1,-1]     最小路径中上一个顶点
#       1. Updata:  
#           if distance[a->b] + distance[b->c] < distance[a->c]: 
#               distance[a->c] = distance[a->b] + distance[b->c]
#               parent[c] = node[b]
#       2. Scan:
#           a.遍历distance, 找到最小值, 对应到node
#       3. Add:
#           a.将该node添加到已选集合, visited = T
#           b.然后作为新顶点重复第一步update操作

# Floyd算法
# 基于动态规划思想
# size = len(node)
# for k in range(size):
#     for i in range(size):
#         for j in range(size):
#             if distance[i][k] + distance[k][j] < distance[i][j]:
#                 distance[i][j] = distance[i][k] + distance[k][j]
#                 s[i][j] = s[i][k]
# table D (size x size): -----> distance table;      table S (size x size): -----> sequence table;
