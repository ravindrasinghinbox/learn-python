import camelcase
from word2number import w2n
# import bytesString

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
print (w2n.word_to_num("two million three thousand nine hundred and eighty four"))