# Symbol-Table-Generator
A Python Script to generate Symbol table which takes C code as input

Language: PYTHON

Tools: re

Description:

  Symbol Table is an important data structure created and maintained by the compiler in order to keep track of semantics of the variable i.e. it stores information about scope and binding information about names, information about instances of various entities such as variable and function names, classes, object, etc. 
  
  Each entry in the symbol table contains the symbol, type, and address of the symbol. In this case study we have used re i.e. regular expression python module to check for identifier, keywords, operators, and literals. The python script accepts c program as input and parses the string to different symbols and regular expression is used to identify the parsed symbol.  
  
The Symbol Table data structure has four methods: 

- Insert() : This is used to insert the parsed symbol into the table if not present. Before    inserting regular expression is used to identify its type. If the symbol is invalid then it is not inserted. 

- Delete()  : The delete method is used to delete the symbols not used in the program. 

- Update() : This method is used to update the symbol table in later time if required.  

- Display() : This method is used to display the symbol table to the user.  

## Output: 

### $gedit Input.c 

    //This is input file 
    #include<stdio.h>
    void main()
    {   
        int a=56;
        printf("Hello world");
        a = a+1;
        if(a>b)
          a=a+1; 
    } 

### $python SymbolTable.py  

    symbol   type   address 
    void     key     0 
    main     id      1 
    int      key     2 
    =        op      3 
    a        id      4 
    56       lit     5 
    printf   id      6 
    +        op      7 
    1        lit     8 
    if       key     9 
    >        op      10 
    b        id      11 

    1.Insert   2.Delete   3.Update   4.Display   5.Exit 
    Enter choice:1 
    Enter symbol to be inserted :/ 
    Symbol inserted Successfully 
    symbol   type    address 
    void     key     0 
    main     id      1 
    int      key     2 
    =        op      3 
    a        id      4 
    56       lit     5 
    printf   id      6 
    +        op      7 
    1        lit     8 
    if       key     9 
    >        op      10 
    b        id      11 
    /        op      12 

    1.Insert   2.Delete   3.Update   4.Display   5.Exit 
    Enter choice:1 
    Enter symbol to be inserted :abc 
    Symbol inserted Successfully 
    symbol   type    address 
    void     key     0 
    main     id      1 
    int      key     2 
    =        op      3 
    a        id      4 
    56       lit     5 
    printf   id      6 
    +        op      7 
    1        lit     8 
    if       key     9 
    >        op      10 
    b        id      11 
    /        op      12 
    abc      id      13 

    1.Insert   2.Delete   3.Update   4.Display   5.Exit 
    Enter choice:1 
    Enter symbol to be inserted :@ 
    Invalid Symbol 

    1.Insert   2.Delete   3.Update   4.Display   5.Exit 
    Enter choice:2 
    Enter symbol to be deleted : abc 
    abc deleted successfully from table 
    symbol   type    address 
    void     key     0 
    main     id      1 
    int      key     2 
    =        op      3 
    a        id      4 
    56       lit     5 
    printf   id      6 
    +        op      7 
    1        lit     8 
    if       key     9 
    >        op      10 
    b        id      11 
    /        op      12 

    1.Insert   2.Delete   3.Update   4.Display   5.Exit 
    Enter choice:2 
    Enter symbol to be deleted : - 
    Symbol - not found in the table 

    1.Insert   2.Delete   3.Update   4.Display   5.Exit 
    Enter choice:3 
    Enter symbol to be updated: / 
    Enter the new symbol:* 
    Enter symbol type :op 
    Symbol updated successfully 
    symbol   type    address 
    void     key     0 
    main     id      1 
    int      key     2 
    =        op      3 
    a        id      4 
    56       lit     5 
    printf   id      6 
    +        op      7 
    1        lit     8 
    if       key     9 
    >        op      10 
    b        id      11 
    *        op      12 

    1.Insert   2.Delete   3.Update   4.Display   5.Exit 
    Enter choice:3 
    Enter symbol to be updated: @ 
    Symbol doesnt exist use insert to add 

    1.Insert   2.Delete   3.Update   4.Display   5.Exit 
    Enter choice:4 
    symbol   type    address 
    void     key     0 
    main     id      1 
    int      key     2 
    =        op      3 
    a        id      4 
    56       lit     5 
    printf   id      6 
    +        op      7 
    1        lit     8 
    if       key     9 
    >        op      10 
    b        id      11 
    *        op      12 

    1.Insert   2.Delete   3.Update   4.Display   5.Exit 
    Enter choice:5 

