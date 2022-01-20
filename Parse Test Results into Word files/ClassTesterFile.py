# тестируем класс MyTestResultParser
from ParserModule import MyTestResultParser

testObj = MyTestResultParser('ksdhfkjsdlfj.txt')

print(testObj.check_format()[0])
print(testObj.check_format()[1])