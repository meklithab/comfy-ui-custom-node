class Calculator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "num1": ("FLOAT", {"default": 0.0}),
                "num2": ("FLOAT", {"default": 0.0}),
                "operand": (["+", "-", "*", "/"],)
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Result",)
    FUNCTION = "calculate"

    def calculate(self, num1, num2, operand):
        try:
            if operand == "+":
                return (f"Sum: {num1 + num2}",)
            elif operand == "-":
                return (f"Differences: {num1 - num2}",)
            elif operand == "*":
                return (f"Product: {num1 * num2}",)
            elif operand == "/":
                return (f"Quotient: {num1 / num2}",)
            else:
                return ("Unknown Operand",)
        except Exception as e:
            return (f"Error: {str(e)}",)


NODE_CLASS_MAPPINGS = {
    "Calculator": Calculator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Calculator": "Custom Calculator"
}
