import unittest
import progression as app

class TestMyApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app
    
    def test_progress(self):
        self.assertEqual(app.progress(3), 11)
        self.assertEqual(app.progress(0), 5)
        self.assertEqual(app.progress(2), 9)

if __name__ == '__main__':
    unittest.main()