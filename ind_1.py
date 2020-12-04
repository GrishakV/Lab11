#!/usr/bin/env 2.
# -*- config: utf-8 -*-

# В строке могут присутствовать скобки как круглые, так и квадратные скобки. Каждой
# открывающей скобке соответствует закрывающая того же типа (круглой – круглая,
# квадратной- квадратная). Напишите рекурсивную функцию, проверяющую правильность
# расстановки скобок в этом случае.


def parChecker(symbolString):
    s = []
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([":
            s.append(symbol)
        else:
            if len(s) == 0:
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and len(s) == 0:
        return True
    else:
        return False


def matches(open, close):
    opens = "(["
    closers = ")]"
    return opens.index(open) == closers.index(close)


if __name__ == '__main__':

    print(parChecker('((([][]))())'))
    print(parChecker('[(])'))
