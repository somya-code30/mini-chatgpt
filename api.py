from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.semantic_match import get_best_match

app = Flask(__name__)
CORS(app)

QA_PAIRS = {
    # ------------------- DSA: Arrays & Strings -------------------
    "What is an array?": "An array is a data structure that stores elements in contiguous memory locations.",
    "Difference between array and linked list?": "Arrays have fixed size and allow random access; linked lists are dynamic and allow efficient insertions/deletions.",
    "What is a string in DSA?": "A string is a sequence of characters stored as an array of characters.",
    "Reverse an array": "Use two pointers or a loop swapping elements from start and end.",
    "Check if a string is a palindrome": "Compare characters from start and end, or use stack/recursion.",

    # ------------------- DSA: Searching & Sorting -------------------
    "What is binary search?": "Binary search divides the sorted array in half to find the element. Time complexity: O(log n).",
    "Difference between linear and binary search": "Linear search scans all elements, O(n); binary search divides sorted data, O(log n).",
    "Explain bubble sort": "Repeatedly swaps adjacent elements if they are in the wrong order. O(n^2) time complexity.",
    "Explain quick sort": "Divide-and-conquer algorithm. Average: O(n log n), Worst: O(n^2).",
    "Explain merge sort": "Divide the array, sort subarrays, then merge. Time complexity: O(n log n).",

    # ------------------- DSA: Recursion & Backtracking -------------------
    "What is recursion?": "Function calling itself to solve subproblems.",
    "Base case in recursion?": "Condition to stop further recursive calls and return a result.",
    "N-Queens problem": "Place queens such that no two attack each other using backtracking.",
    "Generate subsets of array": "Use recursion or bit masking to generate all subsets.",

    # ------------------- DSA: Linked Lists -------------------
    "What is a linked list?": "A linear data structure where each element points to the next.",
    "Types of linked lists": "Singly, Doubly, and Circular linked lists.",
    "Detect loop in linked list": "Use Floyd's cycle detection algorithm (slow and fast pointers).",
    "Reverse a linked list": "Iteratively change pointers or use recursion.",

    # ------------------- DSA: Stacks & Queues -------------------
    "What is a stack?": "LIFO structure. Supports push, pop, top. Used in expression parsing, undo features.",
    "What is a queue?": "FIFO structure. Supports enqueue and dequeue. Used in scheduling and BFS.",
    "What is a deque?": "Double-ended queue allows insertion/deletion from both ends.",
    "Implement stack using queue": "Use one or two queues with clever reordering.",

    # ------------------- DSA: Trees -------------------
    "What is a binary tree?": "Each node has at most two children.",
    "What is a BST?": "Binary Search Tree — left child < root < right child.",
    "Inorder traversal": "Left → Root → Right",
    "Preorder traversal": "Root → Left → Right",
    "Postorder traversal": "Left → Right → Root",
    "Level order traversal": "Breadth-first traversal using a queue.",
    "Check if a tree is balanced": "Ensure the height difference between subtrees is ≤ 1.",

    # ------------------- DSA: Graphs -------------------
    "What is a graph?": "A collection of nodes connected by edges.",
    "Difference between BFS and DFS": "BFS uses queue and explores level by level; DFS uses stack/recursion to go deep first.",
    "Detect cycle in graph": "Use DFS or Union-Find for directed/undirected graphs.",
    "What is topological sort?": "Linear ordering of vertices in a DAG such that for every directed edge u→v, u comes before v.",
    "What is Dijkstra's algorithm?": "Finds shortest paths from a source node to all other nodes using a priority queue.",

    # ------------------- DSA: Heaps & Tries -------------------
    "What is a heap?": "A binary tree where each node follows the heap property (min or max).",
    "Applications of heap": "Priority queues, scheduling, heap sort.",
    "What is a trie?": "Prefix tree used for storing strings and fast prefix-based search.",

    # ------------------- DSA: Dynamic Programming -------------------
    "What is dynamic programming?": "Breaking problems into overlapping subproblems and storing solutions.",
    "0/1 knapsack problem": "Select items to maximize value without exceeding weight. Uses DP.",
    "Longest common subsequence": "DP to find the longest sequence present in both strings.",
    "Longest increasing subsequence": "Find length of the increasing subsequence using DP or binary search.",

    # ------------------- DSA: Misc -------------------
    "What is time complexity?": "Estimates the growth of runtime as input size increases.",
    "Big O notation?": "Describes worst-case performance of an algorithm.",
    "What is memoization?": "Caching results of expensive function calls.",

    # ------------------- DBMS: Basics -------------------
    "What is DBMS?": "Database Management System — software for storing, retrieving, and managing data.",
    "What is RDBMS?": "Relational DBMS stores data in tables with rows and columns.",
    "Difference between DBMS and RDBMS": "RDBMS supports relationships and constraints; DBMS may not.",
    "What is a primary key?": "Uniquely identifies each row in a table.",
    "What is a foreign key?": "References a primary key in another table to enforce relationships.",
    "What are constraints in SQL?": "Rules applied to table data like NOT NULL, UNIQUE, CHECK, PRIMARY KEY.",

    # ------------------- DBMS: SQL -------------------
    "What is SQL?": "Structured Query Language used to manage relational databases.",
    "What is normalization?": "Process of organizing data to reduce redundancy.",
    "Types of normalization": "1NF, 2NF, 3NF, BCNF, etc.",
    "What is a JOIN in SQL?": "Combines rows from two or more tables based on related columns.",
    "Types of joins": "INNER, LEFT, RIGHT, FULL OUTER.",
    "What is an index in SQL?": "Improves speed of data retrieval from a table.",
    "Difference between WHERE and HAVING": "WHERE filters rows before grouping; HAVING filters after GROUP BY.",
    "What is a view in SQL?": "A virtual table based on result-set of an SQL statement.",

    # ------------------- DBMS: Transactions -------------------
    "What are ACID properties?": "Atomicity, Consistency, Isolation, Durability — key properties of transactions.",
    "What is a transaction in DBMS?": "A unit of work performed against a database that is treated atomically.",
    "Difference between COMMIT and ROLLBACK": "COMMIT saves changes; ROLLBACK undoes changes.",
    "What is concurrency control?": "Techniques to ensure correct results when multiple users access data simultaneously.",

    # ------------------- DBMS: Indexing & Keys -------------------
    "What is indexing in DBMS?": "Speeds up retrieval using pointers. Similar to a book index.",
    "Clustered vs Non-clustered index": "Clustered index stores rows in sorted order; non-clustered uses a pointer.",
    "Candidate key vs primary key": "Candidate key can uniquely identify a row; one of them is chosen as primary key.",
    "What is a surrogate key?": "Artificial key used when no natural key is available." ,
    #  DSA

    "What is time complexity of binary search?":"Binary search has O(log n) time complexity.",
    "Explain quick sort algorithm.": "QuickSort uses divide-and-conquer. Average case: O(n log n), worst case: O(n²).",
    "What is dynamic programming?": "Dynamic Programming solves problems by storing solutions to subproblems to avoid recomputation.",
    "Difference between stack and queue.": "Stack is LIFO (Last In First Out); Queue is FIFO (First In First Out).",
    "What is a hash table?": "Hash tables store key-value pairs with O(1) average time for insert, delete, and search.",

    #  Operating Systems
    "What is process scheduling in OS?": "It determines which process runs next using algorithms like FCFS, SJF, Round Robin.",
    "What is a deadlock?": "Deadlock is a state where processes wait indefinitely for resources. Avoided via Banker's algorithm, etc.",
    "What is paging in OS?": "Paging divides memory into fixed-size pages to avoid external fragmentation.",
    "What is context switching?": "Switching the CPU from one process to another, saving state and loading new state.",
    
    #  DBMS
    "What are ACID properties in DBMS?": "ACID = Atomicity, Consistency, Isolation, Durability. Guarantees reliable transactions.",
    "Difference between primary key and foreign key.": "Primary key uniquely identifies rows. Foreign key links two tables.",
    "What is normalization?": "Normalization reduces data redundancy and improves data integrity via normal forms.",
    "Types of SQL joins.": "INNER, LEFT, RIGHT, FULL OUTER joins combine data from multiple tables.",
    "What is indexing in SQL?": "Indexing speeds up retrieval of rows using pointers to data in a table.",
    
    #  Computer Networks
    "What is the OSI model?": "OSI model has 7 layers to standardize networking: physical, data link, network, etc.",
    "Difference between TCP and UDP.": "TCP is reliable and connection-oriented. UDP is faster but connectionless.",
    "What is DNS?": "DNS translates domain names to IP addresses.",
    "What is IP addressing?": "IP address identifies devices on a network. IPv4 uses 32 bits, IPv6 uses 128 bits.",

    #  Misc/CS
    "What is recursion?": "Recursion is a function calling itself to solve smaller subproblems.",
    "Difference between compiler and interpreter.": "Compiler translates code all at once; interpreter does it line-by-line.",
    "What is object-oriented programming?": "OOP organizes code using classes and objects. Key concepts: encapsulation, inheritance, polymorphism.",
    "What is Git?": "Git is a version control system to track and manage changes in source code.",
}


@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('query', '')
    best_question = get_best_match(user_input, list(QA_PAIRS.keys()))
    answer = QA_PAIRS.get(best_question, "Sorry, I don't have an answer for that.")
    return jsonify({'response': answer})
