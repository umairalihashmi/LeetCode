class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk  = []
        def operator(var, st):
            match var:
                case "!":
                    if "f" in st:
                        return "t"
                    return "f"
                case "|":
                    if "t" in st:
                        return "t"
                    return "f"
                case "&":
                    if "f" in st:
                        return "f"
                    return "t"
                case default:
                    return "nothing"
        for x in expression:
            if x == ")":
                st = set()
                while stk[-1] != "(":
                    st.add(stk.pop())
                stk.pop()
                new = operator(stk.pop(),st)
                stk.append(new)

            elif x == ",":
                continue
            else:
                stk.append(x)
        if stk[0] == "f":
            return False
        return True
        