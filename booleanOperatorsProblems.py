"""
and, or, and not:
1.create a variable and set it equal to True using a statement containing an "and" Boolean operator
2.create a variable and set it equal to False using a statement containing an "and" Boolean operator
3.create a variable and set it equal to True using a statement containing an "or" Boolean operator
4.create a variable and set it equal to False using a statement containing an "or" Boolean operator
5.create a variable and set it equal to True using a statement containing an "not" Boolean operator
6.create a variable and set it equal to False using a statement containing an "not" Boolean operator
"""
# type your code for "and, or, and not" below this comment and above the one below it.
var1=True and 5!=4
var2=1==2 and 3>=5
var3=False or 5<=9
var4=4<=1 or 5==2
var5=not 5>=7
var6= not 5//2>=1
print(var1,var2,var3,var4,var5,var6)
# ----------------------------------------------------------------------------------------------------------------------
"""
order of operations for Boolean operators:
1.make var1 evaluate to False by changing or removing a single Boolean operator
2.make var2 evaluate to True by changing or removing a single Boolean operator
"""
# type your code for "order of operations for Boolean operators" below this comment and above the one below it. --------
var11 = not 3 > 1 and 5 != 2 or 6 == 6
var21 = 4 * 2 != 6 and not 7 % 6 == 1
print(var11,var21)
var12 = not 3 > 1 and 5 != 2 and 6 == 6
var22 = 4 * 2 != 6 or not 7 % 6 == 1
print(var12,var22)
var23 = 4 * 2 != 6 and 7 % 6 == 1
print(var23)
# ----------------------------------------------------------------------------------------------------------------------