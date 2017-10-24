# File to handle testing of shopping list items
import unittest
from app.shoppingitems import ShoppingItemsClass


class TestCasesItems(unittest.TestCase):
    
    # Test for existence of activity in activity creation
    # Test for special character activitynames
    # Test for correct owner
    # Test for correct output(activity creation)
    # Test for deletion of existing activity
    # Test for editing activity names
    # Test for editing activity names with existing activity names
    # Test for deletion of bucket with its activities
    

    def setUp(self):
        # Setting up ShoppingItems class
    
        self.item_class_obj = ShoppingItemsClass()

    def tearDown(self):
        # Removing ShoppingItems class
        
        del self.item_class_obj

    def test_existing_item(self):
        # Check to see item name exists or not
         
        self.item_class_obj.item_list = \
            [{'owner': 'mike@gmail.com', 'list': 'Easter', 'name': 'Bread'}, {
                'owner': 'mike@gmail.com', 'list': 'Easter', 'name': 'Blueband'}]
        msg = self.item_class_obj.add_item(
            "Easter", "Bread", "mike@gmail.com")
        self.assertIn(" name already exists", msg)

    def test_special_characters_name(self):
        # Check for special characters in item name
        
        msg = self.item_class_obj.add_item(
            "Easter", "Bread!", "mike@gmail.com")
        self.assertIn("No special characters ", msg)

    def test_owner(self):
        # Check for shopping items belonging to owner
        
        self.item_class_obj.item_list = \
            [{'owner': 'boriss@gmail.com',
              'list': 'Easter', 'name': 'Blueband'}]
        user = "boriss@gmail.com"
        shoppinglist = "Easter"
        msg = self.item_class_obj.owner_items(user, shoppinglist)
        self.assertEqual(
            msg, [{'owner': 'boriss@gmail.com', 'list': 'Easter', 'name': 'Blueband'}])

    def test_correct_output_item(self):
        # Check for correct item creation
        
        msg = self.item_class_obj.add_item(
            "Easter", "Bread", "mike@gmail.com")
        self.assertEqual(
            msg, [{'owner': 'mike@gmail.com', 'list': 'Easter', 'name': 'Bread'}])

    def test_editing_item(self):
        # Check for edits to item name
        
        self.item_class_obj.item_list = \
        [{'owner': 'mike@gmail.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'owner': 'mike@gmail.com', 'list': 'Adventure', 'name': 'Booze'}]
        msg = self.item_class_obj.edit_item(
            'Soda', 'Booze', 'Adventure', "mike@gmail.com")
        self.assertEqual(msg, \
        [{'owner': 'mike@gmail.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'owner': 'mike@gmail.com', 'list': 'Adventure', 'name': 'Soda'}])

    def test_edit_existing_itemname(self):
        # Check if edit name provided is similar to an existing item
        
        self.item_class_obj.item_list = \
        [{'owner': 'mike@gmail.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'owner': 'mike@gmail.com', 'list': 'Adventure', 'name': 'Booze'}]
        msg = self.item_class_obj.edit_item(
            'Snacks', 'Booze', 'Adventure', "mike@gmail.com")
        self.assertIn("name already exists", msg)

    def test_delete_item(self):
        # Check to see if item is deleted
        
        self.item_class_obj.item_list = \
        [{'owner': 'mike@gmail.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'owner': 'mike@gmail.com', 'list': 'Adventure', 'name': 'Booze'}]
        msg = self.item_class_obj.delete_item(
            'Booze', "mike@gmail.com", 'Adventure')
        self.assertEqual(msg, ['Snacks'])

    def test_deleted_list(self):
        #Check if bucket deleted will have its activities deleted to
        
        self.item_class_obj.item_list = \
        [{'owner': 'mike@gmail.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'owner': 'mike@gmail.com', 'list': 'Adventure', 'name': 'Booze'}]
        deleting = self.item_class_obj.deleted_list_items('Adventure')
        self.assertEqual(deleting, None)


if __name__ == '__main__':
    unittest.main()
