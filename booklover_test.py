import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        test_1 = BookLover("Noah Thro", "xjb6yb@virginia.edu", "Fantasy")
        test_1.add_book("Knowing God", 5)
        self.assertTrue(test_1.has_read("Knowing God"))
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_2 = BookLover("Noah Thro", "xjb6yb@virginia.edu", "Fantasy")
        test_2.add_book("Knowing God", 5)
        test_2.add_book("Knowing God", 5)
        expected = 1
        self.assertEqual(test_2.book_list.book_name.isin(["Knowing God"]).sum(), expected)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_3 = BookLover("Noah Thro", "xjb6yb@virginia.edu", "Fantasy")
        test_3.add_book("Knowing God", 5)
        self.assertTrue(test_3.has_read("Knowing God"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_4 = BookLover("Noah Thro", "xjb6yb@virginia.edu", "Fantasy")
        test_4.add_book("Knowing God", 5)
        self.assertFalse(test_4.has_read("Gentle and Lowly"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_5 = BookLover("Noah Thro", "xjb6yb@virginia.edu", "Fantasy")
        test_5.add_book("Knowing God", 5)
        test_5.add_book("Gentle and Lowly", 4)
        test_5.add_book("Every Good Endeavor", 3)
        test_5.add_book("Everybody Always", 2)
        expected = 4
        self.assertEqual(test_5.num_books, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating greater than 3. 
        # Your test should check that the returned books have rating greater than 3
        test_6 = BookLover("Noah Thro", "xjb6yb@virginia.edu", "Fantasy")
        test_6.add_book("Knowing God", 5)
        test_6.add_book("Gentle and Lowly", 4)
        test_6.add_book("Every Good Endeavor", 3)
        test_6.add_book("Everybody Always", 2)
        expected = 2
        self.assertEqual(test_6.fav_books().shape[0], expected)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)