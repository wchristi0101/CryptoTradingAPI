import unittest
import business_logic.website_api


class TestWebsiteAPI(unittest.TestCase):
    def test_Load_YAML(self):
        test_config = business_logic.website_api.LoadYAML("sample_config.yml")
        test_values = test_config.load_configuration(("website", "bittrex"))
        expected_values = {"username": "my_username", "password": "my_password"}

        self.assertEqual(test_values, expected_values, "Yaml is showing a strange value"
        )

    def test_bittrex_username_password(self):
        test_website = business_logic.website_api.Bittrex()
        username_password_expected = test_website.login()

        test_config = business_logic.website_api.LoadYAML("config.yml")
        test_values = test_config.load_configuration(("website", "bittrex"))
        username_password_actual = (test_values.get("username"), test_values.get("password"))

        self.assertEqual(username_password_actual, username_password_expected, "Bittrex website is initializing the "
                                                                                 "wrong username / password")


if __name__ == '__main__':
    unittest.main()
