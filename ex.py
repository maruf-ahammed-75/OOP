def remove_immediate_left_recursion(head, rules):
    alpha = []
    beta = []

    # Separate left-recursive rules (alpha) and non-recursive rules (beta)
    for rule in rules:
        if rule.startswith(head):
            alpha.append(rule[len(head):].strip())  # α part
        else:
            beta.append(rule.strip())  # β part

    new_productions = []

    if alpha:
        head_prime = head + "'"  # new non-terminal A'

        # Step 1: A → βA'
        for b in beta:
            production = head + " → " + b + head_prime
            new_productions.append(production)

        # Step 2: A' → αA' | E
        rhs_rules = []
        for a in alpha:
            rhs_rules.append(a + head_prime)
        rhs_rules.append("E")  # epsilon

        # Build RHS string step-by-step
        rhs = ""
        for i in range(len(rhs_rules)):
            rhs += rhs_rules[i]
            if i != len(rhs_rules) - 1:
                rhs += " | "

        new_productions.append(f"{head_prime} → {rhs}")

    else:
        # No left recursion
        rhs = ""
        for i in range(len(rules)):
            rhs += rules[i]
            if i != len(rules) - 1:
                rhs += " | "
        new_productions.append(f"{head} → {rhs}")

    return new_productions


def eliminate_left_recursion_all(productions_dict):
    nonterminals = list(productions_dict.keys())  # ["A", "B"]

    for i in range(len(nonterminals)):
        Ai = nonterminals[i]
        rules_ai = productions_dict[Ai]


        for j in range(i):
            Aj = nonterminals[j] # kon nonTerminal diea start hossse
            rules_new = []
            for rule in rules_ai:
                if rule.startswith(Aj):
                    # Replace Ai → Aj α with Aj's rules
                    for r in productions_dict[Aj]:
                        rules_new.append(r + rule[len(Aj):].strip()) # akhan a len(Aj)=1 dile kaj korbe
                else:
                    rules_new.append(rule)
            rules_ai = rules_new

        # Remove immediate left recursion , separates α and β
        new_rules = remove_immediate_left_recursion(Ai, rules_ai)

        # Update dictionary with new rules
        productions_dict.pop(Ai)
        for prod in new_rules:
            h, body = prod.split("→")
            h = h.strip()
            # Step-by-step: split body by '|', remove spaces
            parts = body.split("|")
            rlist = []
            for p in parts:
                rlist.append(p.strip())
            productions_dict[h] = rlist

    # Final printing: step-by-step
    print("Transformed Productions:")
    for head in productions_dict:
        output = head + " → "
        for i in range(len(productions_dict[head])):
            output += productions_dict[head][i]
            if i != len(productions_dict[head]) - 1:
                output += " | "
        print(output)


# -----------------------------
if __name__ == "__main__":
    productions_dict = {}

    while True:
        line = input().strip()
        if line.lower() == "end":
            break
        
        head, body = line.split("->")
        head = head.strip()

        parts = body.split("|")
        rules = []
        for p in parts:
            rules.append(p.strip())

        productions_dict[head] = rules

    eliminate_left_recursion_all(productions_dict)