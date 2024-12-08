class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_expression_tree(expression):
    def helper(tokens):
        if not tokens:
            return None

        # Стек для хранения узлов и операций
        stack = []

        # Перебираем все токены в выражении
        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.isalnum():
                # Если токен - операнд, создаем узел и помещаем в стек
                stack.append(Node(token))

            elif token in '+*':
                # Если токен - оператор, создаем узел операции
                new_node = Node(token)

                # Поп из стека операндов
                if len(stack) >= 2:
                    new_node.right = stack.pop()
                    new_node.left = stack.pop()

                stack.append(new_node)

            i += 1

        return stack[0] if stack else None

    tokens = []
    operand = ""
    for char in expression:
        if char.isalnum():
            operand += char
        else:
            if operand:
                tokens.append(operand)
                operand = ""
            if char in '+*':
                tokens.append(char)

    if operand:
        tokens.append(operand)

    root = helper(tokens)
    return root


def inorder_traversal(node):
    if node is None:
        return ""

    left_expr = inorder_traversal(node.left)
    right_expr = inorder_traversal(node.right)

    if node.left and node.right:
        return f"({left_expr}{node.value}{right_expr})"

    return f"{node.value}"


expression = "(a+b)*(c*(d+e+f))+g*(i+j^2)"
parsed_expression = expression.replace(" ", "").replace("(", " ( ").replace(")", " ) ")
print("Parsed expression:", parsed_expression)

root = build_expression_tree(parsed_expression)
reconstructed_expression = inorder_traversal(root)
print("Reconstructed expression:", reconstructed_expression)

# Проверяем, совпадает ли исходное и воссозданное выражения
if reconstructed_expression == expression:
    print("The expression tree is correct!")
else:
    print("There is an error in the expression tree.")
