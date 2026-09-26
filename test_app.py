import unittest

from app import app, evaluate_expression


class CalculatorTests(unittest.TestCase):
    def test_arithmetic_and_parentheses(self):
        self.assertEqual(evaluate_expression("(2 + 3) * 4", "deg"), 20)

    def test_trigonometry_uses_selected_angle_unit(self):
        self.assertAlmostEqual(evaluate_expression("sin(30)", "deg"), 0.5)
        self.assertAlmostEqual(evaluate_expression("sin(pi / 2)", "rad"), 1)

    def test_constants_logs_and_roots(self):
        self.assertAlmostEqual(evaluate_expression("log(100) + ln(e) + sqrt(9) + cbrt(8)", "deg"), 8)

    def test_rejects_python_expressions(self):
        with self.assertRaises(ValueError):
            evaluate_expression("__import__('os').system('true')", "deg")

    def test_button_submission_and_equals(self):
        app.config["TESTING"] = True
        with app.test_client() as client:
            client.post("/", data={"action": "key|digit|2"})
            client.post("/", data={"action": "key|operator|+"})
            client.post("/", data={"action": "key|digit|3"})
            response = client.post("/", data={"action": "equals"})
            self.assertIn(b">5</p>", response.data)


if __name__ == "__main__":
    unittest.main()