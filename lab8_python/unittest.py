import unittest
import lab8


def broken_function():
    raise Exception('Это ошибка')

class MyTestCase(unittest.TestCase):




    def test(self):
        try:
            lab8.product_insert_window()

        except Exception:
            self.fail('unexpected exception raised')
        else:
            self.fail('ExpectedException not raised')




if __name__ == '__main__':
    unittest.main()