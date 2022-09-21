Assignment 4


When to Submit
Due: 11:59pm, 11/5/2020

What to Submit
	 Please prepare a PDF file to include your answers to each question. Please also prepare ONE .py file to include all your codes (if applicable) – clearly comment the corresponding questions. 

How to Submit
	Submit your PDF file and .py file using the Canvas. 

The goal of this collection of assignment is to help you review (i) Trees! 

 
1, In the Lecture 7 for Tree, page 26, we describe a set of ADT operations for a class BinaryTree, which are in addition to the operations of its superclass Tree (page 9). Please design a Pseudo algorithm that uses these operations (and only these operations) to count the number of leaves in a binary tree that are the left children of their respective parent nodes. Your algorithm should have an argument of class BinaryTree. No Python Codes are needed. Please include your answer in the .pdf file. 

2, A binary tree can be used to represent arithmic expressions. In your writeup, please manually draw the binary tree representation of the following expression:   9+(10*20-48/3)-29/(19+4). Note that you have to determine the calculation orders of the operators first. You might use PowerPoint or any other drawing tools to prepare your answers. You might also draw on a piece of paper and include a photograph of your drawings. 

3, Once a binary tree constructed, we might visit every tree node once in certain orders. We taught three traverse algorithms: pre-order traverse, post-order traverse, and in-order traverse. Please Draw a Binary Tree T to satisfy the following requirements. 

a.	Each internal tree node of T stores a single Character
b.	A pre-order traverse will generate the string “EXAMFUN”
c.	A in-order traverse will generate the string “MAFXUEN”

You might use PowerPoint or any other drawing tools to prepare your answers. You might also draw on a piece of paper and include a photograph of your drawings.

4, Please design and implement the BinaryTree class taught in our lecture using Python Arrays, instead of LinkedLink. Note that:  
•	This Array-Based Representation of Binary Trees was introduced in our lecture 7, page 40.
•	The attached folder: sampleCodes includes four .py files which implement the classes: Tree, BinaryTree, LinkedBinaryTree and ExpressionTree, respectively. You need to create a new class ArrayBinaryTree as an alternative to LinkedBinaryTree. 
Like LinkedBinaryTree, the class ArrayBinaryTree should have the following ADT: 

from .binary_tree import BinaryTree

class LinkedBinaryTree(BinaryTree):
  """Linked representation of a binary tree structure."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
  
    def __init__(self, element, parent=None, left=None, right=None):

  #-------------------------- nested Position class --------------------------
  class Position(BinaryTree.Position):
    """An abstraction representing the location of a single element."""

    def __init__(self, container, node):
    def element(self):
    def __eq__(self, other):

  #------------------------------- utility methods -------------------------------
  def _validate(self, p):
    """Return associated node, if position is valid."""

  def _make_position(self, node):
    """Return Position instance for given node (or None if no node)."""

  #-------------------------- binary tree constructor --------------------------
  def __init__(self):
    """Create an initially empty binary tree."""

  #-------------------------- public accessors --------------------------
  def __len__(self):
    """Return the total number of elements in the tree."""
  
  def root(self):
    """Return the root Position of the tree (or None if tree is empty)."""

  def parent(self, p):
    """Return the Position of p's parent (or None if p is root)."""

  def left(self, p):
    """Return the Position of p's left child (or None if no left child)."""

  def right(self, p):
    """Return the Position of p's right child (or None if no right child)."""

  def num_children(self, p):
    """Return the number of children of Position p."""

  #-------------------------- nonpublic mutators --------------------------
  def _add_root(self, e):
    """Place element e at the root of an empty tree and return new Position.

  def _add_left(self, p, e):
"""Create a new left child for Position p, storing element e.

  def _add_right(self, p, e):
    """Create a new right child for Position p, storing element e. Return the Position of new node. Raise ValueError if Position p is invalid or p already has a right child.
    """

  def _replace(self, p, e):
    """Replace the element at position p with e, and return old element."""

  def _delete(self, p):
    """Delete the node at Position p, and replace it with its child, if any.  Return the element that had been stored at Position p.Raise ValueError if Position p is invalid or p has two children.
    """
 
  def _attach(self, p, t1, t2):
    """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p. As a side effect, set t1 and t2 to empty.
    Raise TypeError if trees t1 and t2 do not match type of this tree. Raise ValueError if Position p is invalid or not external.
    """
 You should be able to find similar implementations of the above methods in the file: linked_binary_tree.py. What you need to do is to modify each of these methods  in order to use the Python Array (instead of Linked List) to store the binary tree. 
 
 

5. With the new class ArrayBinaryTree from the previous question,  please design and implement a new version of ExpressionTree, called  ExpressionTreeV2. This new implementation should have the identical ADT as the class ExpressionTree except that its base class is ArrayBinaryTree. Also, please develop codes that use this ExpressionTreeV2 to create a binary tree representing the expression:  5+3*5-(10*4)/2. Different from Question 2 that requires you to manually draw the binary tree, you need to provide Python codes for this question. 

