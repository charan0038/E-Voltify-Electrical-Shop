#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
import http.cookies

cgitb.enable()

conn = pymysql.connect(host="localhost", user="root", password="", database="spma")
cursor = conn.cursor()

# ✅ Retrieve cookie safely
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

form = cgi.FieldStorage()
user_id = form.getvalue("user_id")  # Directly passed from previous page
product_id = form.getvalue("product_id")  # Get product ID
step = form.getvalue("step", "2")  # Default to step 2

if step == "2":
    # Fetch full address from the `signup` table
    cursor.execute("SELECT address FROM signup WHERE id = %s", (user_id,))
    address = cursor.fetchone()

    print("<h2>Step 2: Confirm Your Address</h2>")

    if not address or not address[0]:  # If no address found
        print("<p>No address found. Please add an address.</p>")
        print('<a href="add_address.py">Add New Address</a>')
    else:
        full_address = address[0]  # Address stored in a single column

        print(f"""
            <form action="checkout.py" method="post">
                <input type="hidden" name="step" value="3">
                <input type="hidden" name="user_id" value="{user_id}">
                <input type="hidden" name="product_id" value="{product_id}">
                <input type="hidden" name="address" value="{full_address}">

                <p><strong>Address:</strong> {full_address}</p>
                <button type="submit">Confirm and Continue</button>
            </form>
        """)
elif step == "3":
    address_id = form.getvalue("address_id")

    # ✅ Set address_id in cookie (Ensure path is set)
    cookie["address_id"] = address_id
    cookie["address_id"]["path"] = "/"
    print(cookie.output())

    cursor.execute("SELECT * FROM cart WHERE user_id = %s", (user_id,))
    cart_items = cursor.fetchall()

    total_price = sum(item[3] for item in cart_items)  # Assuming price is column 4

    print("<h2>Step 3: Review Your Products</h2>")
    for item in cart_items:
        print(f"<p>{item[2]} - ₹{item[3]}</p>")

    print(f"<p>Total Price: ₹{total_price}</p>")
    print(f"""
        <form action="checkout.py" method="post">
            <input type="hidden" name="step" value="4">
            <input type="hidden" name="total_price" value="{total_price}">
            <input type="hidden" name="user_id" value="{user_id}">
            <button type="submit">Proceed to Payment</button>
        </form>
    """)

elif step == "4":
    total_price = form.getvalue("total_price")
    address_id = cookie.get("address_id").value  # ✅ Retrieve address from cookie

    # ✅ Insert order into database
    cursor.execute(
        "INSERT INTO orders (user_id, address_id, total_price, payment_status) VALUES (%s, %s, %s, 'pending')",
        (user_id, address_id, total_price))
    conn.commit()
    order_id = cursor.lastrowid

    # ✅ Move cart items to `order_items`
    cursor.execute("SELECT * FROM cart WHERE user_id = %s", (user_id,))
    cart_items = cursor.fetchall()

    for item in cart_items:
        cursor.execute("INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
                       (order_id, item[1], 1, item[3]))  # Assuming price is column 4
        conn.commit()

    # ✅ Clear user's cart
    cursor.execute("DELETE FROM cart WHERE user_id = %s", (user_id,))
    conn.commit()

    print("<h2>Step 4: Order Placed Successfully</h2>")
    print(f"<p>Your Order ID is {order_id}. Proceed to Payment.</p>")
    print(f'<a href="pay_now.py?order_id={order_id}&user_id={user_id}">Pay Now</a>')
