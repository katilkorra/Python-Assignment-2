# Find all email addresses out of a long text.

import re

email_data="dolor sit amet n123@gamail consectetur adipisicing elit. Est, maiores! a@gmail.com ipsum dolor sit amet, consectetur adipisicing elit. Velit neeljoshi780@gmail.com corporis repellat quo rem eum consequuntur laudantium perferendis aperiam aut sed nobis commodi, repellendus inventore sapiente non dolorem tempore dignissimos! Praesentium ut iusto molestias quae in doloremque ab anshpandit@yahoo voluptates fugit. Ab, placeat ratione itaque voluptatem repellendus ut iste temporibus pariatur quisquam."

allEmail=r'\w+@\w+\.?\w+'

print(re.findall(allEmail,email_data))