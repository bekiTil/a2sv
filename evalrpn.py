  def evalRPN(self, tokens: List[str]) -> int:
    
        operation=["+","-","/","*"]
        operand=[]
        for i in tokens:
            if not i in operation:
                operand.append(i)
            else:
                ope1=operand.pop()
                ope2=operand.pop()
                operand.append(str(eval(ope2+i+ope1)))
                if float(operand[-1])<0:
                    operand[-1]=str(ceil(float(operand[-1])))
                else:
                    operand[-1]=str(floor(float(operand[-1])))
        return operand[0]
