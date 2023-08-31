import unittest
from emotion_detection.analyzer import emotion_predictor


class TestEmotionPredictor(unittest.TestCase):

    def test_positive_emotion(self):
        text = "I am really happy today!"
        result = emotion_predictor(text)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_negative_emotion(self):
        text = "I'm feeling sad and disappointed."
        result = emotion_predictor(text)
        self.assertEqual(result['dominant_emotion'], 'sadness')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEmotionPredictor)

    # Run the tests
    unittest.TextTestRunner(verbosity=2).run(suite)
