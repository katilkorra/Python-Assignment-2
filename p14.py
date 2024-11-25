#  Find all the mobile numbers out of a long text.

import re

mobile_data="Mobile phone numbers can be formatted in various ways depending on the country or region, reflecting local conventions and international 1234567890 dialing standards. For example, in the United States, a mobile number 123 is typically written as (123) 456-7890, where the area code is enclosed in parentheses. In Canada, it uses a similar format: with the same North American numbering system. In the United Kingdom, mobile numbers are often presented as 07123 456789 or +44 7123 456789, where the country code (+44) replaces the leading zero. In Australia, a mobile number might appear as 0412 345 678 or +61 412 345 678, with the country code +61. In India, mobile numbers are usually written as +91 98765 43210 or 09876543210, where the country code (+91) is sometimes included, while the local format omits it. Each of these formats reflects how different regions organize their numbering systems, helping to standardize how we dial and connect internationally."

# Expression
m1=r'\d{10}'
m2=r'\(\d{3}\)\s\d{3}-\d{4}'
m3=r'\d{5}\s\d{6}'
m4=r'\+\d{2}\s\d{4}\s\d{6}'
m5=r'\(\+\d{2}\)'
m6=r'\d{4}\s\d{3}\s\d{3}'
m7=r'\+\d{2}\s\d{3}\s\d{3}\s\d{3}'
m8=r'\+\d{2}'
m9=r'\+\d{2}\s\d{5}\s\d{5}'
expMobile = m1 + "|" + m2 + "|" + m3 + "|" + m4 + "|" + m5 + "|" + m6 + "|" + m7 + "|" + m8 + "|" + m9

# Find mobile
allNumber=re.findall(expMobile,mobile_data)

# Print Mobile
print(allNumber)