#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
# Python的for循环本质上就是通过不断调用next()函数实现的
from collections.abc import Iterator
from collections.abc import Iterable
print(isinstance(([1,2]),Iterable))
print(isinstance(({1,2}),Iterable))
print(isinstance('112',Iterable))
print(isinstance(11,Iterable))
print(isinstance(iter([]), Iterator))