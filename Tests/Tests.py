from LoginTests import LoginTests
from AdminTests import AdminTests
from MembersTests import MembersTests
from AddMemberTests import AddMemberTests
from BooksTests import BooksTests
from AddBookTests import AddBookTests
from time import sleep

# Run Tests
LoginTests.login_with_admin()
sleep(1)
LoginTests.login_with_guest()
sleep(1)
AdminTests.admin_members()
sleep(1)
MembersTests.members_insert()
sleep(1)
AddMemberTests.add_member()
sleep(1)
BooksTests.add_book()
sleep(1)
AddBookTests.add_book()
sleep(2)