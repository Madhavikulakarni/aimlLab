def cnf(formula):
    if "and" in formula:
        parts = formula.split("and")
        return " ∧ ".join(p.strip() for p in parts)
    elif "or" in formula:
        parts = formula.split("or")
        return " ∨ ".join(p.strip() for p in parts)
    return formula

def dnf(formula):
    if "or" in formula:
        parts = formula.split("or")
        return " ∨ ".join(p.strip() for p in parts)
    elif "and" in formula:
        parts = formula.split("and")
        return " ∧ ".join(p.strip() for p in parts)
    return formula


# main program
formula = "(A and B) or C or D"

cnf_formula = cnf(formula)
dnf_formula = dnf(formula)

print("CNF:", cnf_formula)
print("Hello")
print("DNF:", dnf_formula)
