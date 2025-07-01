def negate_literal(literal):
    """ Negate a literal by adding or removing the negation symbol '~' """
    if literal.startswith('~'):
        return literal[1:]  # Remove negation
    else:
        return '~' + literal  # Add negation

def resolve(clause1, clause2):
    """ Resolve two clauses to derive a new clause """
    new_clause = []
    resolved = False

    # Copy literals from both clauses
    for literal in clause1:
        if negate_literal(literal) in clause2:
            resolved = True
        else:
            new_clause.append(literal)

    for literal in clause2:
        if negate_literal(literal) not in clause1:
            new_clause.append(literal)

    # Remove duplicates and sort the new clause for consistency
    new_clause = sorted(list(set(new_clause)))

    if resolved:
        # Return the new clause as a tuple so it can be added to a set
        return tuple(new_clause)
    else:
        return None  # No resolution possible

def resolution(propositional_kb, query):
    """ Use resolution to prove or disprove a query using propositional logic """
    # Convert the initial clauses to tuples for consistency
    kb = [tuple(clause) for clause in propositional_kb]
    # Add negated query as a tuple
    kb.append(tuple([negate_literal(query)]))

    while True:
        new_clauses = []
        n = len(kb)
        resolved_pairs = set()  # Track resolved pairs to avoid redundant resolutions

        for i in range(n):
            for j in range(i + 1, n):
                clause1 = kb[i]
                clause2 = kb[j]

                # Ensure consistent order for checking resolved pairs
                pair = tuple(sorted((clause1, clause2)))
                if pair not in resolved_pairs:
                    resolved_pairs.add(pair)
                    resolvent = resolve(clause1, clause2)

                    if resolvent is None:
                        continue  # No resolution possible for these clauses

                    if len(resolvent) == 0:
                        return True  # Empty clause (contradiction), query is proved

                    if resolvent not in new_clauses and resolvent not in kb:
                        new_clauses.append(resolvent)

        if not new_clauses:
            return False  # No new clauses added, query cannot be proven

        kb.extend(new_clauses)  # Add new clauses to the knowledge base

# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    # Example propositional knowledge base (clauses)
    propositional_kb = [
        ['~P', 'Q'],
        ['P', 'Q', 'R'],
        ['~R', 'S']
    ]

    # Query to test
    query = 'S'

    # Run resolution
    result = resolution(propositional_kb, query)

    # Output result
    if result:
        print(f"The query '{query}' is PROVED using resolution.")
    else:
        print(f"The query '{query}' is DISPROVED using resolution.")
