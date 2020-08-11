import ast
import sys
import pickle
from astor import to_source

# To modify the nodes(change identifier names) as we traverse the AST
class MyNodeTransformer(ast.NodeTransformer):
    def visit_Name(self, node):
        if(isinstance(node, ast.Name)):
            result = ast.Name(id='x')
            return ast.copy_location(result, node)
        return node

# To perform the above defined modification on the source code of our choice
def mutate(filename):
    file = open(filename)
    contents = file.read()
    # Generate the AST
    parsed = ast.parse(contents)
    nodeVisitor = MyNodeTransformer()
    transformed = nodeVisitor.visit(parsed)
    return ast.parse(to_source(transformed))

level0 = []
level1 = []
level2 = []

# Extraction of nodes from every level
def ast_print(node, level=0):
    if level==0:
        level0.append(ast.dump(node))
    elif level==1:
        level1.append(ast.dump(node))
    elif level==2:
        level2.append(ast.dump(node))

    for _, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    ast_print(item, level=level+1)
        elif isinstance(value, ast.AST):
            ast_print(value, level=level+1)

filename = sys.argv[2]
input_tree = mutate(filename)
ast_print(input_tree)

level0 = sorted(level0)
level1 = sorted(level1)
level2 = sorted(level2)

program_number1 = sys.argv[1]

filename_prognum = "program"+program_number1


# output_file_lev0 = open((filename_prognum+"_lev0.txt"), "w")
# for i in range(len(level0)):
#     output_file_lev0.write(level0[i])
#     output_file_lev0.write('\n')

# output_file_lev1 = open((filename_prognum+"_lev1.txt"), "w")
# for i in range(len(level1)):
#     output_file_lev1.write(level1[i])
#     output_file_lev1.write('\n')

# output_file_lev2 = open((filename_prognum+"_lev2.txt"), "w")
# for i in range(len(level2)):
#     output_file_lev2.write(level2[i])
#     output_file_lev2.write('\n')

# print("LEVEL0 = ", level0)
# print("LEVEL1 = ", level1)
# print("LEVEL2 = ", level2)

def get_children(node):
    parent = ast.dump(node)
    children = []
    for child_node in ast.iter_child_nodes(node):
        children.append(ast.dump(child_node))
    return parent, children

parents1 = []
parents2 = []
children1 = []
children2 = []

def get_parent_children_relation(root, level=0):
    for _, value in ast.iter_fields(root):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    p, c = get_children(item)
                    if level == 0:
                        parents1.append(p)
                        children1.append(c)
                    elif level == 1:
                        parents2.append(p)
                        children2.append(c)       
                    get_parent_children_relation(item, level=level+1)
        elif isinstance(value, ast.AST):
            p, c = get_children(value)
            if level == 0:
                parents1.append(p)
                children1.append(c)
            elif level == 1:
                parents2.append(p)
                children2.append(c)
            get_parent_children_relation(value, level=level+1)

get_parent_children_relation(input_tree)

pc_1 = list(zip(parents1, children1))
pc_2 = list(zip(parents2, children2))
pc_1.sort
pc_2.sort

output_file_lev0 = open((filename_prognum+"_lev0.txt"), "w")
for ele in level0:
    output_file_lev0.write(ele)
    output_file_lev0.write('\n')

output_file_lev1 = open((filename_prognum+"_lev1.txt"), "w")
output_file_lev2 = open((filename_prognum+"_lev2.txt"), "w")
for ele in pc_1:
    output_file_lev1.write(ele[0])
    output_file_lev1.write('\n')
    for item in ele[1]:
        output_file_lev2.write(item)
        output_file_lev2.write('\n')

# output_file_lev1_pc = open((filename_prognum+"_lev1_pc.pickle"), "wb")
# pickle.dump(pc_1, output_file_lev1_pc)

# output_file_lev2_pc = open((filename_prognum+"_lev2_pc.pickle"), "wb")

# pickle.dump(pc_2, output_file_lev2_pc)

# print("-----------------------------LEVEL1 -> LEVEL2-----------------------------------------------------")
# for i in range(len(parents1)):
#     print("Parent = ", parents1[i], "\nChildren = ", children1[i])
#     print("\n")
# print("------------------------------LEVEL2 -> LEVEL3----------------------------------------------------")
# for i in range(len(parents2)):
#     print("Parent = ", parents2[i], "\nChildren = ", children2[i])
#     print("\n")
# print("-------------------------------------------------------------------------------------------")
