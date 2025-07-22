class Type:
  pass

class IntType(Type):
  def __str__(self):
    return "int"

class FloatType(Type):
  def __str__(self):
    return "float"

class StringType(Type):
  def __str__(self):
    return "string"

class BoolType(Type):
  def __str__(self):
    return "bool"

class ArrayType(Type):
  def __str__(self):
    return "array"

class VoidType(Type):
  def __str__(self):
    return "void"

class ErrorType(Type):
  def __str__(self):
    return "error"