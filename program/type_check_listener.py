from SimpleLangListener import SimpleLangListener
from SimpleLangParser import SimpleLangParser
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckListener(SimpleLangListener):

  def __init__(self):
    self.errors = []
    self.types = {}

  def enterMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    pass

  def exitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not self.is_valid_arithmetic_operation(left_type, right_type):
      self.errors.append(f"Unsupported operand types for * or /: {left_type} and {right_type}")
    self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  def enterAddSub(self, ctx: SimpleLangParser.AddSubContext):
    pass

  def exitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not self.is_valid_arithmetic_operation(left_type, right_type):
      self.errors.append(f"Unsupported operand types for + or -: {left_type} and {right_type}")
    self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  def enterInt(self, ctx: SimpleLangParser.IntContext):
    self.types[ctx] = IntType()

  def enterFloat(self, ctx: SimpleLangParser.FloatContext):
    self.types[ctx] = FloatType()

  def enterString(self, ctx: SimpleLangParser.StringContext):
    self.types[ctx] = StringType()

  def enterBool(self, ctx: SimpleLangParser.BoolContext):
    self.types[ctx] = BoolType()

  def enterParens(self, ctx: SimpleLangParser.ParensContext):
    pass

  def exitParens(self, ctx: SimpleLangParser.ParensContext):
    self.types[ctx] = self.types[ctx.expr()]

  def is_valid_arithmetic_operation(self, left_type, right_type):
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
      return True
    return False

  def can_compare(self, left_type, right_type):
    """Determina si dos tipos pueden compararse con =="""
    # Números pueden compararse entre sí
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return True
    # Tipos del mismo tipo pueden compararse
    if type(left_type) == type(right_type):
        return True
    # Otras combinaciones no son válidas
    return False
  
  def enterEqual(self, ctx: SimpleLangParser.EqualContext):
    pass

  def exitEqual(self, ctx: SimpleLangParser.EqualContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not self.can_compare(left_type, right_type):
      self.errors.append(f"Cannot compare {left_type} and {right_type}")
    self.types[ctx] = BoolType()  # Comparaciones siempre retornan bool

  def enterAnd(self, ctx: SimpleLangParser.AndContext):
    pass

  def exitAnd(self, ctx: SimpleLangParser.AndContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not (isinstance(left_type, BoolType) and isinstance(right_type, BoolType)):
      self.errors.append(f"Logical operator && requires boolean operands, got {left_type} and {right_type}")
    self.types[ctx] = BoolType()
