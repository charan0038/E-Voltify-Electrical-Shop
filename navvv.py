#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("Content-type: text/html\n\n")
import pymysql
import cgi
import cgitb

cgitb.enable()

# Get data from the form submission
form = cgi.FieldStorage()
product_id = form.getvalue("product_id")
user_id = form.getvalue("user_id")
brand_name = form.getvalue("brand_name")
product_price = form.getvalue('product_price')
product_image = form.getvalue('product_image')
product_name = form.getvalue('product_name')
color1 = form.getvalue('color1')


# Database connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',  # Empty password for XAMPP
    database='spma',  # Your database name
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

# Check if the product is already in the cart
cursor.execute("SELECT * FROM cart WHERE product_id = %s AND user_id = %s", (product_id, user_id))
existing_cart = cursor.fetchone()

if existing_cart:
    # If product exists, increase quantity
    new_quantity = existing_cart['quantity'] + 1
    cursor.execute("UPDATE cart SET quantity = %s WHERE product_id = %s AND user_id = %s", (new_quantity, product_id, user_id))
    connection.commit()
    message = "Product quantity updated in cart!"
else:
    # Add new product to cart
    cursor.execute("INSERT INTO cart (user_id,product_id, quantity,price, image, brand, product_name,Color) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
                   , (user_id,product_id, 1,product_price, product_image, brand_name, product_name,color1))
    connection.commit()
    message = "Product added to cart!"

# Close DB connection
cursor.close()
connection.close()

# Redirect back with JavaScript alert
print(f"""
<script>
    alert("{message}");
    window.history.back();
</script>
""")
