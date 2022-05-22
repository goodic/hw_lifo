class LiFo:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if self.size() > 0:
            return False
        return True

    def push(self, element):
        self.stack.append(element)

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def pop(self):
        if not self.isEmpty():
            self.stack.pop(-1)
        return self.peek()


def balance_checker(check_string):
    good_pairs = [['(', ')'], ['[', ']'], ['{', '}']]
    check_stack = LiFo()
    for symbol in check_string:
        if symbol in ('(', '[', '{'):
            check_stack.push(symbol)
        else:
            if [check_stack.peek(), symbol] in good_pairs:
                check_stack.pop()
            else:
                return 'Несбалансированно'
    return 'Сбалансированно'


if __name__ == '__main__':
    print(balance_checker(input('введите строку из скобок: ')))
