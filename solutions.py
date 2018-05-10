
Technical Interview Practice Solutions
Dr. Ahmet Faruk Cakmak

'''
Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False.

Answer Q_1:
'''    

input_s_1 = "udacity"
input_t_1 = "cityuda"

input_s_2 = "footbal"
input_t_2 = "soccer"

def question1(s_1, t_1):
    
    s_1 = s_1.replace(" ", "")
    t_1 = t_1.replace(" ", "")

    if len(s_1) != len(t_1):
        return False

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s_1 = s_1.lower()
    t_1 = t_1.lower()

    dict_1 = dict.fromkeys(list(alphabet), 0)
    dict_2 = dict.fromkeys(list(alphabet), 0)

    for i in range(len(s_1)):
        dict_1[s_1[i]] += 1
        dict_2[t_1[i]] += 1
    return dict_1 == dict_2


print(question1(input_s_1, input_t_1))

print(question1(input_s_2, input_t_2))



'''
Question 2
Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.

Answer Q_2:
'''


def is_Palindrome(s):
    s = s.lower()
    return s[::-1] == s


def question2(s):
    L_P_S = ""
    
    if type(s) != str:
        return None
    else:
        length_s = len(s)
        sub_string = []
        for i in range(0, length_s):
            for j in range(i, length_s):
                if is_Palindrome(s[i:j + 1]) and len(s[i:j + 1]) > len(L_P_S):
                    L_P_S = s[i:j + 1]
        print("The longest palindromic substring of '{}' is '{}'".format(s,L_P_S))
        return L_P_S
                
    

print(question2("Hannah"))
print(question2("banana"))
print(question2("udacityyticadu"))
print(question2("A"))






'''
Question 3
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices 
in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list
structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be question3(G)

Answer Q_3:
'''    


from heapq import heappop, heappush

def question3(G):
    V, Sp_T = [], {} 
    s = 'A'
    Queue = [(0, None, s)]
    if G:
        while Queue:
            x, weight, y = heappop(Queue)
            if y in V: continue 
            V.append(y)

            if weight is None :
                pass
            elif weight in Sp_T:
                Sp_T[weight].append((y, x))
            else:
                Sp_T[weight]=[(y, x)]

            for z, x in G[y]:
                heappush(Queue, (x, y, z))
        return Sp_T
    else:
        return None


G = {'A':[('B',2)],'B':[('A',2),('C',5)],'C':[('B',5)]}
print ("The minimum spanning tree of {} is: {}.".format(G, question3(G)))

G1 = {'A': [('B', 1), ('C', 5), ('D', 4)],
     'B': [('A', 1), ('C', 2), ('D', 6)],
     'C': [('A', 5), ('B', 2), ('D', 3)],
     'D': [('A', 4), ('B', 6), ('C', 3)]}
print ("The minimum spanning tree for the G1 is: {}.".format( question3(G1)))


G2 = {'A':[('B',4)],
      'B':[('C',8),('A',4)],
      'C':[('B',8),('D',7),('F',4)],
      'D':[('C',7),('F',14),('E',9)],
      'E':[('D',9),('F',10)],
      'F':[('E',10),('D',14),('C',4)],}
      

print ("The minimum spanning tree for the G2 is: {}.".format( question3(G2)))




'''
Question 4

Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest 
node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the 
tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common 
ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The 
function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the 
index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative 
integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular 
order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.

Answer Q_4:
'''



def parent_node(T, n):
 #return parent of n if it exists else return -1
    height_T = len(T)
    for i in range(height_T):
        if T[i][n] == 1:
            return i
    return -1

def question4(T, r, n1, n2):
    n1_ancestor_list= []
    while n1 != r:        
        n1 = parent_node(T, n1)
        n1_ancestor_list.append(n1)
    if len(n1_ancestor_list) == 0:
        return -1
    while n2 != r:
        n2 = parent_node(T, n2)
        if n2 in n1_ancestor_list:
            return n2
    return -1



print (question4([[0,1,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [1,0,0,0,1],
                  [0,0,0,0,0]],
                 3,
                 1,
                 4))


print (question4([[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]],
                  2,
                  3,
                  4))



print (question4([[0, 0, 1, 0],
                 [0, 0, 0, 0],
                 [0, 1, 0, 1],
                 [0, 0, 0, 0]],
                0,
                1,
                3))
            

    
    
'''
Question 5

Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements,
the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll 
is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below 
to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

Answer Q_5:
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None 

class S_Linked_List(object):
    def __init__(self,head=None):
      self.head = head
  
    def append(self, data):
      cur_node = self.head
      if self.head:
        while cur_node.next:
          cur_node = cur_node.next
        cur_node.next = data
      else:
        self.head = data
    
def question5(ll, m):
    if (ll and m == None):
      return None

    cur_position = ll
    cur_value = ll
    index = 0
    
    if True:
      for i in range(0, m):
        if index == None:
          return None
        cur_position = cur_position.next
          
      while cur_position != None:
        cur_position = cur_position.next
        cur_value = cur_value.next
      return cur_value.data

       
A = Node(1)
B = Node(2)
C = Node(4)
D = Node(16)
E = Node(32)
F = Node(64)
G = Node(128)
H = Node(264)

list = S_Linked_List(A)
list.append(B)
list.append(C)
list.append(D)
list.append(E)
list.append(F)
list.append(G)

print (question5(A, 1))
print (question5(A, 2))
print (question5(A, 3))
print (question5(A, 4))
print (question5(A, 5))
print (question5(A, 6))

