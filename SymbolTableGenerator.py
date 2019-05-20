import re

class Syminfo:
    sym = ''
    sym_type = ''
    addr = ''
    def __init__(self, sym, sym_type, addr):
        self.sym = sym
        self.sym_type = sym_type
        self.addr = addr
    
class SymbolTable:
    table = list()
    def insert(self, sym):
        sym_tab = [obj.sym for obj in self.table]
        if sym in keywords:
            if sym in sym_tab:
                return True
            self.table.append(Syminfo(sym, 'key', addr[0]))
            addr.remove(addr[0])
            return True
        else:
            if sym in oper:
                if sym in sym_tab:
                    return True
                self.table.append(Syminfo(sym, 'op', addr[0]))
                addr.remove(addr[0])
                return True
            li = split(sym, oper)
            for iden in li:
                if re.match('[a-zA-Z][_a-zA-Z0-9]*', iden):
                    if iden in sym_tab:
                        return True
                    self.table.append(Syminfo(iden, 'id', addr[0]))
                    addr.remove(addr[0])
                    return True
                elif re.match('[0-9]+', iden):
                    if iden in sym_tab:
                        return True
                    self.table.append(Syminfo(iden, 'lit', addr[0]))
                    addr.remove(addr[0])
                    return True
        return False 
    def delete(self, inp1):
        symbols = [i.sym for i in table.table]
        if inp1 in symbols:
            index = symbols.index(inp1)
            ele = table.table.pop(index)
            addr.insert(0, ele.addr)
            print("%s deleted successfully from table" % inp1)
            table.display()
        else:
            print("Symbol %s not found in the table" % inp1)
                
    def update(self, inp1):
        symbols = [i.sym for i in table.table]
        if inp1 in symbols:
            index = symbols.index(inp1)
            table.table[index].sym = input('Enter the new symbol:')
            table.table[index].sym_type = input('Enter symbol type :')
            print('Symbol updated successfully')
            table.display()
        else:
            print('Symbol doesnt exist use insert to add')
                
    def display(self):
        print('symbol \t type \t address')
        for t in self.table:
            print("%s \t %s \t %s" % (t.sym, t.sym_type, t.addr))


def split(line, separators):
    for sep in separators:
        line = line.replace(sep, ' ')
    return [sym.strip() for sym in line.split()]
        
if __name__=='__main__':
    
    oper = ['+','-', '*', '/', '%', '=',
            '==', '!=', '>', '<', '>=', '<=',
            '&&', '||', '!', '&', '|', '^', '~', '<<', '>>']
    keywords = ['int', 'void', 'float', 'double', 'char','return',
                'if', 'else', 'for', 'while', 'do', 'case', 'break', 'struct']    
    identifiers = re.compile('[a-zA-Z][_a-zA-Z0-9]*')
    separators = [' ', '{', '}', '(', ')', ';', ',', '"']
    
    addr = [i for i in range(50)]
    table = SymbolTable()
    fhand = open('input.c')
    for l in fhand:
        line = l.strip()
        line = re.sub('".*"', ' ', line)
        if re.match('^#.*', line) or re.match('//.*', line):
            continue
        symbols = split(line, separators)

        for sym in symbols: 
            for op in oper:
                if op in sym:
                    table.insert(op)
            for id1 in split(sym, oper):
                table.insert(id1)
                        
    table.display()
    
    while True:
        ch = int(input("1.Insert \t 2.Delete \t 3.Update \t 4.Display \t 5.Exit\nEnter choice:"))
        if ch==1:
            inp1 = input("Enter symbol to be inserted :")
            if inp1 in [obj.sym for obj in table.table]:
                print("Symbol already exists")
                continue
            if table.insert(inp1):
                print("Symbol inserted Successfully")
                table.display()
            else:
                print("Invalid Symbol")
                    
        elif ch==2:
            inp1 = input("Enter symbol to be deleted : ")
            table.delete(inp1)
                
        elif ch==3:
            inp1 = input("Enter symbol to be updated: ")
            table.update(inp1)
            
        elif ch==4:
            table.display();
            
        else:
            break
            
            
                
                
