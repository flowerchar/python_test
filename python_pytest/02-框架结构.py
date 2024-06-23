
def setup_module():
    print("\nsetup_module：整个.py模块只执行一次，开始")

def teardown_module():
    print("\nteardown_module：整个.py模块只执行一次，结束")

def setup_function():
    print("\nsetup_function：不在类中的函数前面，每个函数执行一次")

def teardown_function():
    print("\nteardown_function：不在类中的函数后面，每个函数执行一次")

def test_one():
    print("正在执行测试模块----test_one")
    x = "this"
    assert "h" in x

def test_two():
    print("正在执行测试模块----test_two")
    assert 1 == 1

class TestClass:
    def setup_class(self):
        print("\nsetup_class：类里面所有用例执行之前执行")

    def teardown_class(self):
        print("\nteardown_class：类里面所有用例执行之后执行")

    def setup_method(self):
        print("\nsetup_method：每个用例开始前执行")

    def teardown_method(self):
        print("\nteardown_method：每个用例结束后执行")

    def test_three(self):
        print("正在执行测试模块----test_three")
        x = "hello"
        assert "h" in x

    def test_four(self):
        print("正在执行测试模块----test_four")
        x = "this"
        assert "h" in x

