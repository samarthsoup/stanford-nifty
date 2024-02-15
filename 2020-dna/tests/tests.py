import unittest
from src.profile import analyze_dna

class TestDNAAnalysis(unittest.TestCase):
    def test_analyze_dna_1(self):
        data_path = r"C:\Users\thesa\codes\stanford-nifty\2020-dna\test-data\data.csv" 
        sequence_path = r"C:\Users\thesa\codes\stanford-nifty\2020-dna\test-data\sequence1.txt" 
        expected = "Alice"
        result = analyze_dna(data_path, sequence_path)
        self.assertEqual(result, expected)

    def test_analyze_dna_2(self):
        data_path = r"C:\Users\thesa\codes\stanford-nifty\2020-dna\test-data\data.csv" 
        sequence_path = r"C:\Users\thesa\codes\stanford-nifty\2020-dna\test-data\sequence2.txt" 
        expected = "Bob"
        result = analyze_dna(data_path, sequence_path)
        self.assertEqual(result, expected)

    def test_analyze_dna_3(self):
        data_path = r"C:\Users\thesa\codes\stanford-nifty\2020-dna\test-data\data.csv" 
        sequence_path = r"C:\Users\thesa\codes\stanford-nifty\2020-dna\test-data\sequence3.txt" 
        expected = "Charlie"
        result = analyze_dna(data_path, sequence_path)
        self.assertEqual(result, expected)

    def test_analyze_dna_4(self):
        data_path = r"C:\Users\thesa\codes\stanford-nifty\2020-dna\test-data\data.csv" 
        sequence_path = r"C:\Users\thesa\codes\stanford-nifty\2020-dna\test-data\sequence4.txt" 
        expected = "no match"
        result = analyze_dna(data_path, sequence_path)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

# to run tests, be in the 2020-dna directory and run 'python -m unittest tests/tests.py'