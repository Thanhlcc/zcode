Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite

## Exceptions
1. Redeclared(<kind>, <identifier>)
    <kind>: Variable/Parameter/Function
2. Undeclared(Identifier(), <identifier-name>)
3. Undeclared(Function(), <function-name>)
4. TypeMismatchInExpression(<expression>)
    - Indexing E1\[E2\]
    - Binary and Unary
    - Function Call Expr return type != VoidType
5. TypeCannotBeInferred(<statement>)
    - VoidType <- VoidType (assignment or declaration with initialization block)
    - Type of symbols at usage point must be known or resolvable at the **first usage**
      - Including usages in both statement and expression and declaration
      - The exception thrown is the **innermost one containing the symbol**.
6. TypeMistmatchStatement
   - Function Call Statement must have **VoidType** as return type
   - **If** condition / **For** condition expression must return **BoolType**
   - type(expression in Return) == type(Function return)
   - type(declaration) == type(initialization)
7. NoDefinition(<name>)
   - Declaration with no Definition (body=None)