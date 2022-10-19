
import numexpr # Для работы этого калькулятора необходима библиотека numexpt


expr = input('Введите математическое выражение: ') #вводим все то что нужно сделать. Например 7+5 и жмем Enter
res = numexpr.evaluate(expr)

print(f'Result = {res}')