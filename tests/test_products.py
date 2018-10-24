import unittest
import json
from app.api.products import create_app

class TestApp(unittest.TestCase):
    def  setUp(self):
        self.app = create_app

    def test_add_product(self):
        with self.app.test_client as client:
            tham = client.post('/api/v1/products', content_type='application/json',
                                data=json.dumps({"product_name":"goat",
                                                "price":"70000",
                                                "stock":3}))
            self.assertEqual(tham.status_code, 201)                                    
            thitue = json.loads(tham.data.decode())
            self.assertIn('added the product', thitue["message"])

    if __name__ == '__main__':
        unittest.main        
