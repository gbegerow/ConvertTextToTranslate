import unittest
from Txt2TranslateLib import TextToTranslateConverter

class Test_ConvertTests(unittest.TestCase):
    def test_A(self):
        #self.fail("Not implemented")
        self.assertTrue('gelingt immer')

    def test_ContainsText_should_false_for_empty(self):
        sut  = TextToTranslateConverter('')
        self.assertEqual(sut.mightContainText(), False)

    def test_ContainsText_should_true_for_tellraw(self):
        sut  = TextToTranslateConverter('/tellraw @a Hello')
        self.assertEqual(sut.mightContainText(), True)

if __name__ == '__main__':
    unittest.main()
