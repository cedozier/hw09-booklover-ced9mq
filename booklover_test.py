"""
booklover_test.py
"""

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        my_object = BookLover("Claire D", "ced123@gmail.com", "romance")
        book_name = "Pride and Prejudice"
        my_object.add_book(book_name, 5)
        is_book_in_book_list = my_object.book_list['book_name'].isin([book_name]).any() # test if book is in list
        self.assertTrue(is_book_in_book_list) # check 

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        my_object = BookLover("Claire D", "ced123@gmail.com", "romance")
        book_name = "Pride and Prejudice"
        my_object.add_book(book_name, 5)
        my_object.add_book(book_name, 5) # try to add book a second time
        num_times_book_in_list = my_object.book_list['book_name'].value_counts()[book_name] # get number of times book is in list
        expected = 1
        self.assertEqual(num_times_book_in_list, expected) # check
    
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        my_object = BookLover("Claire D", "ced123@gmail.com", "romance")
        book_name = "Pride and Prejudice"
        my_object.add_book(book_name, 5)
        is_book_in_list = my_object.has_read(book_name) # test has_read
        self.assertTrue(is_book_in_list) # check 
    
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        my_object = BookLover("Claire D", "ced123@gmail.com", "romance")
        book_name = "Pride and Prejudice"
        my_object.add_book(book_name, 5)
        is_book_in_list = my_object.has_read("Persuasion") # test book not in list
        self.assertFalse(is_book_in_list) # check 
    
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        my_object = BookLover("Claire D", "ced123@gmail.com", "romance")
        my_object.add_book("Pride and Prejudice", 5)
        my_object.add_book("Emma", 5)
        my_object.add_book("Persuasion", 5)
        my_object.add_book("Sense and Sensibility", 4.5)
        my_object.add_book("Northanger Abbey", 4)
        my_object.add_book("Mansfield Park", 3)
        number_of_books_in_list = my_object.num_books_read() # get number of books in list
        expected = 6 
        self.assertEqual(number_of_books_in_list, expected) # check
    
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        my_object = BookLover("Claire D", "ced123@gmail.com", "romance")
        my_object.add_book("Pride and Prejudice", 5)
        my_object.add_book("Emma", 5)
        my_object.add_book("Persuasion", 5)
        my_object.add_book("Sense and Sensibility", 4.5)
        my_object.add_book("Northanger Abbey", 4)
        my_object.add_book("Mansfield Park", 3)
        my_object.add_book("Lady Susan", 2.5)
        fav_books_list = my_object.fav_books()
        all_greater_than_3 = (fav_books_list['book_rating'] > 3).all() # test that all returned books have rating > 3
        self.assertTrue(all_greater_than_3) # check
                
if __name__ == '__main__':
    unittest.main(verbosity=3)