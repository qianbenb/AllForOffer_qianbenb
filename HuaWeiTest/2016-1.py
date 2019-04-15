# while True:
#     try:
#         nm = raw_input()
#         id_list_str = raw_input()
#         n,m = int(nm.split()[0]),int(nm.split()[1])
#         id_list = []
#         id_list_str = id_list_str.split()
#         for i in range(n):
#             id_list.append(int(id_list_str[i]))
#         for i in range(m):
#             Minput = raw_input()
#             QU, id1, id2 = Minput.split()[0], Minput.split()[1], Minput.split()[2]
#             id1, id2 = int(id1), int(id2)
#             id12 = [id1, id2]
#             if QU == 'Q':
#                 id1 = min(id12)
#                 id2 = max(id12)
#                 if (id1 == id2):
#                     print id_list[id1 - 1]
#                 else:
#                     print max(id_list[id1 - 1:id2])
#             if QU == 'U':
#                 id_list[id1 - 1] = id2
#     except:
#         break

# ==================================================================

# nm = raw_input()
# id_list_str = raw_input()
# n,m = int(nm.split()[0]),int(nm.split()[1])
# id_list = []
# id_list_str = id_list_str.split()
# for i in range(n):
#     id_list.append(int(id_list_str[i]))
# for i in range(n):
#     Minput = raw_input()
#     QU, id1, id2 = Minput.split()[0],Minput.split()[1],Minput.split()[2]
#     id1,id2 = int(id1),int(id2)
#     id12 = [id1,id2]
#     if QU == 'Q' :
#         id1 = min(id12)
#         id2 = max(id12)
#         if (id1 == id2):
#             print id_list[id1-1]
#         else:
#             print max(id_list[id1-1:id2])
#     if QU == 'U':
#         id_list[id1-1]=id2

# ==================================================================

# x = 'asd dasdw qwrwq E\\C\\D'
# print x[x.rfind('\\')-1]

# ==================================================================

