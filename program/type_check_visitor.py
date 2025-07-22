from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckVisitor(SimpleLangVisitor):

  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for * or /: {} and {}".format(left_type, right_type))

  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for + or -: {} and {}".format(left_type, right_type))
  
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())



  def visitEqual(self, ctx: SimpleLangParser.EqualContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    # Solo permitir comparaciones entre tipos compatibles
    if self.can_compare(left_type, right_type):
        return BoolType()  # Comparaciones siempre retornan bool
    else:
        raise TypeError("Cannot compare {} and {}".format(left_type, right_type))

  def visitAnd(self, ctx: SimpleLangParser.AndContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    # && solo funciona con booleanos
    if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
        return BoolType()
    else:
        raise TypeError("Logical operator && requires boolean operands, got {} and {}".format(left_type, right_type))

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