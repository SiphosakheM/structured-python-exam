import unittest
from exam import *

class TestSection1DataStructures(unittest.TestCase):
    """Testing Data Structures Scenarios (20%)"""
    def test_q1_sync(self):
        self.assertEqual(sync_user_preferences({'a': 1, 'b': 2}, {'b': 2, 'c': 3}), {'a': 1, 'c': 3})

    def test_q2_flatten(self):
        self.assertEqual(flatten_api_response({'u': {'id': 1}}), {'u_id': 1})

    def test_q3_investors(self):
        self.assertEqual(find_common_investors([['A', 'B'], ['B', 'C'], ['B']]), {'B'})

    def test_q4_trending(self):
        self.assertEqual(filter_trending_hashtags(['a', 'a', 'a', 'a', 'b'], 3), {'a': 4})

    def test_q5_linter(self):
        self.assertTrue(validate_code_blocks("{[()]}"))
        self.assertFalse(validate_code_blocks("{[(])}"))

class TestSection2DataManipulation(unittest.TestCase):
    """Testing Data Manipulation Scenarios (20%)"""
    def test_q1_portfolio(self):
        self.assertAlmostEqual(calculate_portfolio_return([(10, 0.5), (20, 0.5)]), 15.0)

    def test_q2_logs(self):
        data = [("2023-01-01", "srv1", "OK")]
        self.assertEqual(group_logs_by_timestamp(data)["2023-01-01"]["srv1"], "OK")

    def test_q3_candidates(self):
        apps = [{'name': 'A', 'score': 80}, {'name': 'B', 'score': 90}]
        self.assertEqual(shortlist_candidates(apps, 85), ['B'])

    def test_q4_normalize(self):
        self.assertEqual(normalize_sensor_reading([10, 20, 30]), [0.0, 0.5, 1.0])

    def test_q5_batch(self):
        self.assertEqual(len(batch_process_orders([1, 2, 3, 4], 2)), 2)

class TestSection3Recursion(unittest.TestCase):
    """Testing Recursion Scenarios (20%)"""
    def test_q1_interest(self):
        self.assertAlmostEqual(compute_compound_interest_recursive(100, 0.1, 1), 110.0)

    def test_q2_audit(self):
        self.assertEqual(sum_nested_integers([1, [2, [3]]]), 6)

    def test_q3_file_tree(self):
        tree = {'src': {'main.py': 'file'}}
        self.assertTrue(find_file_in_tree(tree, 'main.py'))

    def test_q4_routes(self):
        self.assertEqual(len(generate_route_combinations(['A', 'B', 'C'])), 6)

    def test_q5_depth(self):
        self.assertEqual(recursive_depth_check([1, [2, [3]]]), 3)

class TestSection4StringFormatting(unittest.TestCase):
    """Testing String Formatting Scenarios (20%)"""
    def test_q1_invoice(self):
        res = format_invoice_line("Milk", 2.50, 1)
        self.assertTrue(res.endswith("2.50") and len(res) == 40)

    def test_q2_pnl(self):
        self.assertEqual(display_pnl_change(110, 100), "+10.00%")

    def test_q3_sql(self):
        res = generate_db_insert("users", {"id": 1})
        self.assertIn("INSERT INTO users", res)

    def test_q4_mac(self):
        self.assertEqual(format_mac_address([255, 170, 0]), "FF:AA:00")

    def test_q5_log(self):
        res = create_log_entry("INFO", "Test")
        self.assertIn("[   INFO   ]", res)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(importlib.import_module(__name__))
    result = unittest.TextTestRunner(verbosity=0).run(suite)
    
    total = result.testsRun
    failed = len(result.failures) + len(result.errors)
    passed = total - failed
    score = (passed / total) * 100
    
    print(f"\n--- FINAL REPORT ---")
    print(f"SECTION A SCORE: {score:.2f}%")