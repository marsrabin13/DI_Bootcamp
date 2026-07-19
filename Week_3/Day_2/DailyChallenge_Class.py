
# Goal:

# Create a Pagination class that simulates a basic pagination system.

# Step 1: Create the Pagination Class

# Define a class called Pagination to represent paginated content.
# It should optionally accept a list of items and a page size when initialized.


# Step 2: Implement the __init__ Method

# Accept two optional parameters:
# items (default None): a list of items
# page_size (default 10): number of items per page
import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        if page_size <= 0:
            raise ValueError("Page size must be greater than 0.")
        self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages_count = (len(items) + page_size - 1) // page_size  # math.ceil equivalent

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages_count:
            raise ValueError("Page number out of range.")
        self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages_count - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages_count - 1:
            self.current_idx += 1
        else:
            print("Already on last page.")
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        else:
            print("Already on first page.")
        return self

    def total_pages(self):
        return self.total_pages_count

    def __str__(self):
        return f"Page {self.current_idx + 1} of {self.total_pages_count} | Items: {self.get_visible_items()}"

# Behavior:

# If items is None, initialize it as an empty list.
# Save page_size and set current_idx (current page index) to 0.
# Calculate total number of pages using math.ceil.


# Step 3: Implement the get_visible_items() Method

# This method returns the list of items visible on the current page.
# Use slicing based on the current_idx and page_size.


# Step 4: Implement Navigation Methods

# These methods should help navigate through pages:

# go_to_page(page_num)
# → Goes to the specified page number (1-based indexing).
# → If page_num is out of range, raise a ValueError.

# first_page()
# → Navigates to the first page.

# last_page()
# → Navigates to the last page.

# next_page()
# → Moves one page forward (if not already on the last page).

# previous_page()
# → Moves one page backward (if not already on the first page).

# 📝 Note:

# Pages are indexed internally from 0, but user input is expected to start at 1.
# All navigation methods (except go_to_page) should return self to allow method chaining.


