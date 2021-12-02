from operator import add, mul
exps = [l.strip().split(" ") for l in open("input")]



def evalc(exp):
    res = 0
    evaluator = None
    while len(exp)>0:
        
        print(res, evaluator," ".join(exp))
        op = exp[0]

        if op == ")":
            return [str(res)]+exp[1:]
        elif op == "(":
            temp_exp = evalc(exp[1:])
            if isinstance(temp_exp, list):
                exp = temp_exp
            else:
                exp = [temp_exp]
        elif op == "+":
            evaluator = add
            exp = exp[1:]
        
        elif op == "*":
            evaluator = mul

            temp_exp = evalp(exp[1:])
            if isinstance(temp_exp, list):
                exp = temp_exp
            else:
                exp = [temp_exp]
        else:
            if bool(evaluator):
                res = evaluator(res, int(op))
                exp = exp[1:]
            else:
                res = int(op)
                exp = exp[1:]
   
    return str(res)



def evalp(exp):
    res = 0
    evaluator = None
    while len(exp)>0:
        
        print(res, evaluator," ".join(exp))
        op = exp[0]

        if op == ")":
            return [str(res)]+exp
        elif op == "(":
            temp_exp = evalc(exp[1:])
            if isinstance(temp_exp, list):
                exp = temp_exp
            else:
                exp = [temp_exp]
        elif op == "+":
            evaluator = add
            
            exp = exp[1:]
        elif op == "*":
            evaluator = mul
            temp_exp = evalp(exp[1:])
            if isinstance(temp_exp, list):
                exp = temp_exp
            else:
                exp = [temp_exp]
        else:
            if bool(evaluator):
                res = evaluator(res, int(op))
                exp = exp[1:]
            else:
                res = int(op)
                exp = exp[1:]
   
    return str(res)


def split_closures(exp):
    exp2 = []
    for x in exp:
        if "(" in x:
            c = x.count("(")
            exp2+= (["("]*c)
            exp2.append(x[c:])

        elif ")" in x:
            c = x.count(")")
            exp2 += [x[:-c]]
            exp2 += ([")"]*c)

        else:
            exp2.append(x)

    return exp2

exps = list(map(split_closures, exps))
print(sum(int(evalc(exp)) for exp in exps))
