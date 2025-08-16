def arithmetic_arranger(problems, display_answers=False):
    # Error checks
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    operators = []
    second_operands = []
    results = []
    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must contain two operands and one operator."

        op1, operator, op2 = parts

        # Check operator validity
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check operands are digits
        if not (op1.isdigit() and op2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check length of operands
        if len(op1) > 4 or len(op2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate width for formatting
        width = max(len(op1), len(op2)) + 2

        # Calculate result
        if operator == '+':
            result = str(int(op1) + int(op2))
        else:
            result = str(int(op1) - int(op2))

        # Format lines
        line1.append(op1.rjust(width))
        line2.append(operator + ' ' + op2.rjust(width - 2))
        line3.append('-' * width)
        line4.append(result.rjust(width))

    # Join lines with 4 spaces in between
    arranged_problems = '    '.join(line1) + '\n' + '    '.join(line2) + '\n' + '    '.join(line3)
    if display_answers:
        arranged_problems += '\n' + '    '.join(line4)

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
