# Ayoub Rammo
 

from array_binary_tree import ArrayBinaryTree

class ExpressionTree(ArrayBinaryTree):
  """An arithmetic expression tree."""

  def __init__(self, token, left=None, right=None):
    
    super().__init__()                        
    if not isinstance(token, str):
      raise TypeError('Token must be a string')
    self._add_root(token)                    
    if left is not None:                     
      if token not in '+-*x/':
        raise ValueError('token must be valid operator')
      self._attach(self.root(), left, right)  

  def __str__(self):
    """Return string representation of the expression."""
    pieces = []                
    self._parenthesize_recur(self.root(), pieces)
    return ''.join(pieces)

  def _parenthesize_recur(self, p, result):
    """Append piecewise representation of p's subtree to resulting list."""
    if self.is_leaf(p):
      result.append(str(p.element()))                   
    else:
      result.append('(')                                 
      self._parenthesize_recur(self.left(p), result)     
      result.append(p.element())                        
      self._parenthesize_recur(self.right(p), result)   
      result.append(')')                                

  def evaluate(self):
    """Return the numeric result of the expression."""
    return self._evaluate_recur(self.root())

  def _evaluate_recur(self, p):
    """Return the numeric result of subtree rooted at p."""
    if self.is_leaf(p):
      return float(p.element())      # we assume element is numeric
    else:
      op = p.element()
      left_val = self._evaluate_recur(self.left(p))
      right_val = self._evaluate_recur(self.right(p))
      if op == '+':
        return left_val + right_val
      elif op == '-':
        return left_val - right_val
      elif op == '/':
        return left_val / right_val
      else:                          # treat 'x' or '*' as multiplication
        return left_val * right_val   


def tokenize(raw):
  
  oparators = set('+-x*/() ')    

  mark = 0
  tokens = []
  n = len(raw)
  for j in range(n):
    if raw[j] in oparators:
      if mark != j:                 
        tokens.append(raw[mark:j])  
      if raw[j] != ' ':
        tokens.append(raw[j])       
      mark = j+1                    
  if mark != n:                 
    tokens.append(raw[mark:n])      
  return tokens

def buildExpressionTree(tokens):
  """
      5+3*5-(10*4)/2
  """
  exArray = []                                        
  for t in tokens:
    if t in '+-x*/':                           
      exArray.append(t)                               
    elif t not in '()':                         
      exArray.append(ExpressionTree(t))               
    elif t == ')':       
      right = exArray.pop()                          
      op = exArray.pop()                             
      left = exArray.pop()                           
      exArray.append(ExpressionTree(op, left, right)) 
    
  return exArray.pop()

if __name__ == '__main__':
  big = buildExpressionTree(tokenize('5+3*5-(10*4)/2'))
  print(big, '=', big.evaluate())
