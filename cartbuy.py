#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("Content-type: text/html\n\n")

import pymysql
import cgi
import cgitb
import  smtplib
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()

# Get user ID and product ID from URL
form = cgi.FieldStorage()
product_id = form.getvalue("product_id")
uid = form.getvalue("id")
address_id = form.getvalue("address_id")
quantity = form.getvalue("quantity")
total_amount = form.getvalue("total")
payment_method = form.getvalue("payment_method")

# Fetch user details
c = "SELECT * FROM signup WHERE id=%s"
cur.execute(c, (uid,))
user = cur.fetchone()

print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>E-voltify</title>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        <link rel="stylesheet" href="sty.css">
    </head>
    <style>
        #tea:hover {
            transform: scale(1.02);
            transition: 0.3s ease-in-out;
            box-shadow: 2px 2px 5px black;
        }
        a {
            color: black;
            background-color: transparent;
            text-decoration: none;
        }
    </style>
    <body>
        <header>
            <h1 class="p-2" align="center">SRI PALANI MURUGAN AGENCIES</h1>
        </header>
    """)

print(f"""
        <nav class="navbar navbar-expand-lg sticky-top">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">
                    <img src="media/shop_1-removebg-preview.png" alt="Logo" width="90px" height="50px">
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbar">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="./homelog.py?id={uid}"><i class="bi bi-house-door-fill"></i> HOME</a>
                        </li>
                    </ul>
                    <ul class="navbar-nav">
                        <div class="dropdown profile-dropdown">
                            <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown">
                                <img src="media/{user[7]}" id="userProfilePic" class="rounded-circle" width="40" height="40">
                                <span id="userName">{user[1]}</span>
                            </button>
                            <ul class="dropdown-menu left">
                                <li><a class="dropdown-item" href="#">My Orders</a></li>
                                <li><a class="dropdown-item" href="Account.py?id={uid}">Account Settings</a></li>
                                <li><a class="dropdown-item text-danger" href="./home.py" id="logoutBtn">Logout</a></li>
                            </ul>
                        </div>
                    </ul>
                </div>
            </div>
        </nav>
    """)

p = f"SELECT * FROM address WHERE user_id=%s"
cur.execute(p, (uid,))
h = cur.fetchall()

if h:
    for b in h:
        print(f"""
            <div class="container mt-5" id="addressSection">
                <div class="card p-3">
                    <h4>Delivery Address</h4>
                    <p><strong>Name:</strong> {b[2]}</p>
                    <p><strong>Address:</strong> {b[3]}</p>
                    <p><strong>Pincode:</strong> {b[4]}</p>
                    <p><strong>Phone:</strong> {b[5]}</p>
                    <form action="#" method="POST">
                        <input type="hidden" name="user_id" value="{uid}">
                        <button type="button" data-bs-toggle="modal" data-bs-target="#log" class="btn btn-primary">Change Address</button>
                    </form>
                    <form method="POST">
                        <input type="hidden" name="address_id" value="{b[0]}">
                        <button type="submit" name="action" value="delete" class="btn btn-danger">Clear</button>
                    </form>
                </div>
            </div>
            """)
else:
    print(f"""
        <br><br>
        <div class="container" id="addAddressSection">
            <div class="card p-3">
                <p>Please Add the Address ...!</p>
                <button type="button" data-bs-toggle="modal" data-bs-target="#lo" class="btn btn-primary">Add Address</button>
            </div>
        </div>
        """)

# Address Modal (common for both Add and Change)
print("""
    <div class="modal fade" id="log" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Add / Change Address</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form method="POST" action="/cgi-bin/submit_address.py" class="form-group">
                        <input type="hidden" name="user_id" value="{uid}">
                        <label>Name:</label>
                        <input type="text" class="form-control" required placeholder="Enter Your Name" name="name"><br>
                        <label>Address:</label>
                        <textarea class="form-control" name="Address" rows="3" placeholder="Enter your address" required></textarea><br>
                        <label>Pincode:</label>
                        <input type="number" class="form-control" required placeholder="Enter Pincode" name="pinc"><br>
                        <label>Phone Number:</label>
                        <input type="number" class="form-control" required placeholder="Enter Phone Number" name="num"><br>
                        <button type="submit" name="action" value="update" class="btn btn-success">Save</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    """)

# Handling form submission
name = form.getvalue("name")
address = form.getvalue("Address")
pincode = form.getvalue("pinc")
phone = form.getvalue("num")
action = form.getvalue("action")

if action == "update" and name and address and pincode and phone:
    update_query = "UPDATE address SET name=%s, address=%s, pincode=%s, phone=%s WHERE user_id=%s"
    cur.execute(update_query, (name, address, pincode, phone, uid))
    con.commit()
    # Redirect to refresh

if action == "delete" and address_id:
    # Check if address entry exists
    cur.execute("SELECT * FROM address WHERE id=%s", (address_id,))
    address_exists = cur.fetchone()

    if address_exists:
        # Execute delete query
        delete_query = "DELETE FROM address WHERE id=%s"
        cur.execute(delete_query, (address_id,))
        con.commit()  # Commit changes
    else:
        print("<script>alert('Address not found!');</script>")

print("""
        <div class="modal fade" id="lo" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Add Address</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form method="POST" class="form-group">
                            <label>Name:</label>
                            <input type="text" class="form-control" required placeholder="Enter Your Name" name="name"><br>
                            <label>Address:</label>
                            <textarea class="form-control" name="Address" rows="3" placeholder="Enter your address" required></textarea><br>
                            <label>Pincode:</label>
                            <input type="number" class="form-control" required placeholder="Enter Pincode" name="pinc"><br>
                            <label>Phone Number:</label>
                            <input type="number" class="form-control" required placeholder="Enter Phone Number" name="num"><br>
                            <input type="submit" name="Update" class="btn btn-success" data-bs-dismiss="modal">
                        </form>
                    </div>
                </div>
            </div>
        </div>
    """)

name = form.getvalue("name")
address = form.getvalue("Address")
pincode = form.getvalue("pinc")
phone = form.getvalue("num")
submit = form.getvalue("Update")
if submit:
    query = "INSERT INTO address (User_id, name, address, pincode, phone) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(query, (uid, name, address, pincode, phone))
    con.commit()
    print("""
            <script>
                alert("Submit Successfully..!");
            </script>
        """)
print("""
    <div class="container">
    """)
# Assuming user_id is the logged-in user's ID
user_id = 1  # Example user ID

# Step 1: Get all product IDs and their quantities from the cart for the given user_id
cur.execute("SELECT product_id, quantity FROM cart WHERE user_id = %s", (user_id,))
cart_items = cur.fetchall()  # Fetch all rows

# Create a dictionary to store product_id as key and quantity as value
cart_dict = {row[0]: row[1] for row in cart_items}

# Extract product IDs
product_ids = list(cart_dict.keys())

# Check if there are products in the cart
if product_ids:
    # Step 2: Retrieve product details for the fetched product_ids
    placeholders = ', '.join(['%s'] * len(product_ids))
    query = f"SELECT * FROM products WHERE product_id IN ({placeholders})"
    cur.execute(query, tuple(product_ids))
    products = cur.fetchall()

    # Step 3: Display each product with its quantity from the cart
    for i in products:
        product_id = i[0]  # Assuming product_id is in the first column
        quantity = cart_dict.get(product_id, 1)  # Get quantity, default to 1 if not found

        print(f"""
                <!-- Product Details -->
                <div class="card mt-4 p-3">
                    <h4>Product Details</h4>
                    <div class="row">
                        <div class="col-md-3">
                            <img src="./media/{i[7]}" class="img-fluid">
                        </div>
                        <div class="col-md-9">
                            <h5>{i[1]}</h5>
                            <p><strong>Brand:</strong> {i[2]}</p>
                            <p><strong>Quantity:</strong> {quantity}</p> 
                            <p><strong>Price:</strong> &#8377; {i[4]}</p>
                            <p><strong>About:</strong> {i[10]}</p>
                            <p><strong>Description:</strong> {i[6]}</p>
                        </div>
                    </div>
                </div>""")
else:
    print("<p>No products in your cart.</p>")

cur.execute("SELECT * FROM address WHERE user_id = %s", (uid,))
addresses = cur.fetchall()
print(f"""
    <div class="container">
        <div class="card mt-4 p-3">
            <h4>Payment</h4>
            <form method="POST">
                <input type="hidden" name="user_id" value="{uid}">
                <input type="hidden" name="phone" value="{phone}">
                <input type="hidden" name="quantity" value="{quantity}">
                <input type="hidden" name="product_details" value="{i[1]} - &#8377;{i[2]}">
                <input type="hidden" name="total" value="{i[4]}">

                <h5>Select Address</h5>
    """)

    # Dynamically display addresses as radio buttons
for address in addresses:
        address_id = address[0]  # Assuming first column is address ID
        full_address = f"{address[2]}, {address[3]}, {address[4]}, {address[5]}"  # Adjust based on your table fields

        print(f"""
        <label>
            <input type="radio" name="address_id" value="{address_id}" required> {full_address}
        </label><br>
        """)

print("""
            <h5>Payment Method</h5>
            <label><input type="radio" name="payment_method" value="Cash On Delivery" checked> Cash on Delivery</label><br>
            <label><input type="radio" name="payment_method" value="Online Payment"> Online Payment</label><br>
            <input type="submit" name="up" class="btn btn-success mt-3" value="Place Order">
        </form>
    </div>
    </div>
    """)
if form.getvalue("up"):
    # Fetch user email from the signup table
    cur.execute("SELECT mail FROM signup WHERE id=%s", (uid,))
    user_email = cur.fetchone()

    if user_email:
        user_email = user_email[0]
        fromadd = "spma483@gmail.com"
        password = "ggik alzy dqvj nyve"
        toadd = user_email
        subject = "Order Confirmation - Your Order Has Been Placed Successfully!"
        body =  f"""
        Dear Customer,

        Your order has been placed successfully!

        Order Details:
        - Address ID: {address_id}
        - Payment Method: {payment_method}

        Thank you for shopping with us!

        Regards,
        SRI PALANI MURUGAN AGENCIES
        """
        msg = f"Subject: {subject}\n\n{body}"

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(fromadd, password)
            server.sendmail(fromadd, toadd, msg)
            server.quit()
            print(f"""
               <script>
               alert("Order confirmation email sent successfully!");
               </script>
               """)
        except smtplib.SMTPException as e:
            print(f"""
               <script>
               alert("Failed to send email: {str(e)}");
               </script>
               """)

try:
        # Fetch form data
        submit = form.getvalue("up")

        if submit:
            user_id = form.getvalue("user_id")
            address_id = form.getvalue("address_id")  # Get selected address ID
            phone = form.getvalue("phone")
            product_details = form.getvalue("product_details")
            total = form.getvalue("total")
            quantity = form.getvalue("quantity")  # New: Get quantity from the form
            payment_method = form.getvalue("payment_method")

            # Ensure quantity is a valid integer
            # Ensure quantity is a valid integer
            if quantity is None or quantity.strip() == "":
                quantity = 1  # Default value if empty
            else:
                try:
                    quantity = int(quantity)  # Convert to integer
                except ValueError:
                    quantity = 1  # Set default valid value

            cur.execute("SELECT name, address, pincode, phone FROM address WHERE id = %s", (address_id,))
            selected_address = cur.fetchone()

            if selected_address:
                address = f"{selected_address[0]}, {selected_address[1]}, Pincode: {selected_address[2]}, Phone: {selected_address[3]}"

                # Ensure all values are filled
                if not all([user_id, address, product_details, total, quantity, payment_method]):
                    print("<script>alert('Some required fields are missing.');</script>")
                else:
                    # Insert the order into the database with quantity
                    order_query = """
                        INSERT INTO orders (user_id, address, product, total_amount, quantity, payment_method) 
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    cur.execute(order_query, (user_id, address, product_details, total, quantity, payment_method))
                    con.commit()

                    print(f"<script>alert('Order placed successfully!'); location.href='sam.py?id={user_id}';</script>")
            else:
                print("<script>alert('Invalid address selection.');</script>")
except Exception as e:
        print(f"<script>alert('Error placing order: {str(e)}');</script>")

print("""
<br><br>
<footer>
    <div class="container"><br>
        <div class="row"><br>
            <div class="col-md-4" align="center">
                <h4>Address</h4>
                <p align="center"> <a href="" id="k" style="text-decoration: none;"><i class="bi bi-geo-alt-fill"></i>
                        1/189-1,Vadakku Thottam Salai,<br>Malumichampatti,<br>Coimbatore-641050</a><br><br>
                    <a href=""  style="text-decoration: none;" id="k"><i class="bi bi-envelope-fill"></i>
                        spmagencies1819@gmail.com</a><br><br>
                    <a href="" id="k"  style="text-decoration: none;"><i class="bi bi-telephone-fill"></i> +91 7708166635</a>
                </p>
            </div>

            <div class="col-md-4" align="center">
                <h4>Working Hours</h4><br>
                <p><i class="bi bi-alarm-fill"></i> Monday to Saturday: 9:00 AM – 8:00 PM</p>
                <p><i class="bi bi-alarm-fill"></i> Sunday: 9:00 AM – 2:00 PM </p><br><br>
                <p style="font-size: larger; ">
                    <div class="link">
                    <a href=""><span class="fa fa-whatsapp "></span>
                    </a><a href=""><span class="fa fa-instagram"></span>
                    </a><a href=""><span class="fa fa-facebook"></span>
                    </a><a href=""><span class="fa fa-twitter"></span></a></div>
                </p>
            </div>
            <div class="col-md-4" align="center">
                <h4>Why Choose Us?</h4>

                <p> High-Quality Products</p>
                <p>Competitive Pricing</p>
                <p>Expert Assistance</p>
                <p>Reliable After-Sales Support</p><br><br><br>
            </div>
            <div class="container">
                <div class="rows">
                <p align="center"> Copyrights <i class="bi bi-c-circle"></i> 2025 & SRI
                    PALANI MURUGAN
                    AGENCIES.All Rights Reserved</p>
            </div></div>
        </div>
    </div>
</footer>
</body>
</html>
""")