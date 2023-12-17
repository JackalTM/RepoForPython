import unittest
import code_to_test

class TestCap(unittest.TestCase):

    def TestOneWord(self):
        text = "python"
        resoule = code_to_test.CapitalizeText(text)
        self.assertAlmostEqual(resoule, "Python")

    def TestMultipleWorld(self):
        text = "monty python"
        resoule = code_to_test.CapitalizeText(text)
        self.assertAlmostEqual(resoule, "Monty Python")

if __name__ == "__main__":
    unittest.main()
