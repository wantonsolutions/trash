#-----------------------------------------------------------------
# pycparser: rewrite_ast.py
#
# Tiny example of rewriting a AST node
#
# Eli Bendersky [https://eli.thegreenplace.net/]
# License: BSD
#-----------------------------------------------------------------
from __future__ import print_function
from re import A
import sys

sys.path.extend(['.', '..'])
from pycparser import c_parser, parse_file, c_generator, c_ast



class PointerWrapper(c_ast.NodeVisitor):
    def visit_FuncDecl(self, node):
        # print(node.coord)
        # print(node)
        ty = c_ast.TypeDecl(declname='_hidden',
                            quals=[],
                            type=c_ast.IdentifierType(['int']))
        newdecl = c_ast.Decl(
                    name='_hidden',
                    quals=[],
                    storage=[],
                    funcspec=[],
                    type=ty,
                    init=None,
                    bitsize=None,
                    coord=node.coord)
        if node.args:
            node.args.params.append(newdecl)
        else:
            node.args = c_ast.ParamList(params=[newdecl])

def print_node(node):
    generator = c_generator.CGenerator()
    print(generator.visit(node))

def wrap_node_with_func(node, func_name):

    #make sure that the node is wrapable
    print(type(node))
    if node == None:
        print("node is none")
    if isinstance(node,c_ast.ID):
        #check the node type
        print("actually wrapping " + node.name)
        fc = c_ast.FuncCall(
            c_ast.ID(func_name), 
            c_ast.ExprList([node],
            coord=node.coord))
        return fc
    return node

def capture_line(ast, line_number):
    for child_name, child in ast.children():
        coord = child.coord
        if coord == None:
            print("printing none child")
            print_node(child)
            continue
        s = str(coord).split(":")
        print(s)
        lnumber = s[1]

        if lnumber == line_number:
            print("FOUND Correct Line Number")
            print_node(child)
            node = wrap_node_with_func(child,"trace_pointers")
            if node == child:
                print("not quite a match continuing")
                capture_line(child,line_number)
            else:
                print("a match made in heaven")
                child = node
                print_node(child)
                return
        capture_line(child,line_number)

def get_line(ast, line):
    print("TODO: validate line here")
    s = line.split(":")
    filename=s[0]
    lnumber=s[1]
    offset=s[2]

    print(filename + ":" +  lnumber + ":" + offset)
    #ast = parse_file(filename,use_cpp=True)
    c = capture_line(ast,lnumber)
    return c



# FuncCall:  (at helloworld.c:8:5)
#           ID: anil_func (at helloworld.c:8:5)
#           ExprList:  (at helloworld.c:8:16)
#             UnaryOp: & (at helloworld.c:8:16)
#               ID: a (at helloworld.c:8:16)

    

if __name__ == '__main__':

    #inject_func(None)

    line = "helloworld.c:8:2"
    anil_func = "trace_pointers"

    s = line.split(":")
    filename=s[0]
    lnumber=s[1]
    offset=s[2]

    print(filename + ":" +  lnumber + ":" + offset)
    ast = parse_file(filename,use_cpp=True)
    ast.show(showcoord=True, nodenames=True, attrnames=True)


    # v = PointerWrapper()
    # v.visit(ast)
    # generator = c_generator.CGenerator()
    # print(generator.visit(ast))

    node = get_line(ast, line)
    generator = c_generator.CGenerator()
    print(generator.visit(ast))

    # node = wrap_node_with_func(node,anil_func)
    # node.show()
    # print(generator.visit(node))
    # print(generator.visit(ast))





#     parser = c_parser.CParser()
#     ast = parse_file("helloworld.c", use_cpp=True)

#     #traverse(ast)

# #    ast = parser.parse(text)
#     print("Before:")
#     ast.show(offset=2, showcoord=True)

#     assign = ast.ext[0].body.block_items[0]
#     assign.lvalue.name = "y"
#     assign.rvalue.value = 2

#     print("After:")

#     ast.show(offset=2)
#     generator = c_generator.CGenerator()
#     print(generator.visit(ast))

