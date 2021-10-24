import fileinput as fi

import re
import collections

import lark

def generate_grammar(lines: str) -> str:
    """generate a grammar from the input"""
    rules = collections.defaultdict(set)
    for line in lines.splitlines():
        rule_name, rest = line.split(" => ")
        atoms = re.findall(r"[A-Z][a-z]*", rest)

        # Add the rule literal
        rules[rule_name].add('"{}"'.format(rule_name))
        # Add all the atoms
        rules[rule_name].add(" ".join(map(str.lower, atoms)))

        # We also want to make sure we append literals for all atoms
        for atom in atoms:
            rules[atom].add('"{}"'.format(atom))

    sg = ""
    for name, rule in rules.items():
        rs = " | ".join(list(rule))
        sg += "{}: {}\n".format(name.lower(), rs)

    return sg

def count_nodes(tree: lark.Tree) -> int:
    """Used to get the number of parent nodes in the tree"""
    return sum(len(x.children) > 0 for x in tree.iter_subtrees())

# Parse the input
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")

grammar = generate_grammar(groups[0])
try:
    parser = lark.Lark(grammar, start="e", parser="lalr")
    tree = parser.parse(groups[1])
except:
    # Some grammars cannot be parsed with the lalr, so it's worth
    # falling back to the slower, but more robust earley
    parser = lark.Lark(grammar, start="e", paresr="earley")
    tree = parser.parse(groups[1])


print(count_nodes(tree))
