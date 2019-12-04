import os
import json
import unittest

from mnist_app.constants import conf_constants, TESTS_DIR
from mnist_app.api import _predict, model_loader


TEST_DATA_DIR = os.path.join(TESTS_DIR, "test_data", "mnist_app")


class TestAPI(unittest.TestCase):

    model_loader.from_conf_constants(conf_constants)
    test_img_path = os.path.join(TEST_DATA_DIR, "mnist_img_0.jpg")

    def test__predict(self, expected_l=10):
        print("Testing mnist_app.api._predict")
        result_json = _predict(self.test_img_path, debug=True)
        result_list = json.loads(result_json)
        result_l = len(result_list)
        self.assertEqual(expected_l, result_l)
        print("Output length is 10 - test passed")
        self.assertEqual(expected_l, len(list(filter(lambda x: type(x) is float, result_list))))
        print("All values in output list are floats - test passed")
        self.assertEqual(expected_l, len(list(filter(lambda x: x <= 0.0, result_list))))
        print("All values in output list <= 0.0 - test passed")


def main():
    TestAPI().test__predict()


if __name__ == "__main__":
    main()

