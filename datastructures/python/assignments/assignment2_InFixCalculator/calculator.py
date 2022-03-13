import java.util.Stack;

public class calculator {
    public static void main(String[] args) {
        String expression = "10 * (2 + 15) / 17";
        System.out.println(expression + " = " + calculate(expression));
    } // main

    public static int calculate(String expression) {
        char[] exp = expression.toCharArray();

        // create both stacks for operators and numbers
        Stack<Character> operators = new Stack<Character>();
        Stack<Integer> nums = new Stack<Integer>();

        for (int i = 0; i < exp.length; i++) {
            // if there is a space ignore it and keep moving
            if (exp[i] == ' ')
                continue;

            // add numbers to the number stack
            if (Character.isDigit(exp[i])) {
                StringBuffer temp_str = new StringBuffer();

                // handles multiple digit numbers
                while (i < exp.length && Character.isDigit(exp[i]))
                    temp_str.append(exp[i++]);
                // push the number onto the stack
                nums.push(Integer.parseInt(temp_str.toString()));
                i--;
            }

            // push open parens to operator stack
            else if (exp[i] == '(')
                operators.push(exp[i]);

            // if exp[i] is a close paren, perform operations
            // until the next operator is an open paren
            else if (exp[i] == ')') {
                while (operators.peek() != '(')
                    nums.push(operate(operators.pop(), nums.pop(), nums.pop()));
                // get rid of the open paren
                operators.pop();
            }

            // if exp[i] is an operator check the precedence before pushing
            else if (exp[i] == '+' || exp[i] == '-' || exp[i] == '*' || exp[i] == '/') {
                while (!operators.empty() && precedence(exp[i], operators.peek()))
                    // while exp[i] is has lower precedence than the top of
                    // the stack, perform the highter precedence operations
                    nums.push(operate(operators.pop(), nums.pop(), nums.pop()));
                // push the operator
                operators.push(exp[i]);
            }
        }

        // perform operations until there are no more operators
        while (!operators.empty())
            nums.push(operate(operators.pop(), nums.pop(), nums.pop()));

        // pop the answer off the stack and return it
        return nums.pop();
    } // calculate

    // compares precedence between two operators
    public static boolean precedence(char operator1, char operator2) {
        // if the operator is parens it has the highest precedence
        if (operator2 == '(' || operator2 == ')')
            return false;
        // if the new operator is / or * do nothing
        if ((operator2 == '-' || operator2 == '+') && (operator1 == '/' || operator1 == '*'))
            return false;
        // new operator has lower precedence
        else
            return true;
    } // precedence

    // perform operations on 2 numbers
    public static int operate(char operator, int second, int first) {
        switch (operator) {
            case '+':
                return first + second;
            case '-':
                return first - second;
            case '*':
                return first * second;
            case '/':
                if (second == 0)
                    throw new UnsupportedOperationException("Cannot divide by zero");
                return first / second;
        }
        return 0;
    } // operate

    // Switching from the stack class to the deque interface doesn't actually change
    // too much. For the use case of a stack a deque will offer the same time and
    // space complexity. One thing of note is the fact that the Stack class extends
    // the vector class, meaning you could gather individual indexes of a stack
    // which is contradictory to what a stack should be trying to accomplish. The
    // deque interface does not have this ability.
}
