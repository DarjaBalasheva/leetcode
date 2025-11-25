from back.model.calc_model import Calculator

# val = [0,0,2,1,2,2,3,0]
# def my_function(a: list):
#     result = {}
#     for i in a:
#         if result.get(i):
#             result.get(i) += 1
#         else:
#             result[i] = 1
#


# Запуск калькулятора
if __name__ == "__main__":
    # x = lambda a: a + 10
    # print(x(1))
    calc = Calculator()
    calc.window.mainloop()
