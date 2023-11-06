# custom_test_framework.py

class TestCase:
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        methods = [func for func in dir(self) if callable(getattr(self, func)) and func.startswith("test_")]
        for method in methods:
            self.setUp()
            try:
                getattr(self, method)()
                print(f"{method} - Test passed")
            except AssertionError as e:
                print(f"{method} - Test failed: {e}")
            finally:
                self.tearDown()

    def test(self):
        # This method should be overridden by subclasses
        # If this raises, it means a subclass has not implemented its own test methods
        raise NotImplementedError("Test method not implemented")
