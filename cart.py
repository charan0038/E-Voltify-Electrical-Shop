#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()
user_id = form.getvalue("id")
action = form.getvalue("action")
product_id = form.getvalue("product_id")
quantity = form.getvalue("quantity")

con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()

# Handle form submissions
if action == "remove":
    # Ensure product_id is a single value
    if isinstance(product_id, list):
        product_id = product_id[0]
    cur.execute("DELETE FROM cart WHERE product_id = %s AND user_id = %s", (product_id, user_id))
    con.commit()
elif action == "clear":
    cur.execute("DELETE FROM cart WHERE user_id = %s", (user_id,))
    con.commit()
elif action == "update":
    cur.execute("UPDATE cart SET quantity = %s WHERE product_id = %s AND user_id = %s", (quantity, product_id, user_id))
    con.commit()

cur.close()
con.close()

con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()
cur.execute("SELECT * FROM cart WHERE user_id = %s", (user_id,))
cat = cur.fetchall()
total_amount = sum(item[5] * item[4] for item in cat)
v = "SELECT * FROM signup WHERE id=%s"
cur.execute(v, (user_id,))
r = cur.fetchone()
if r:
    print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Voltify</title>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="sty.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
</head>
<body>
    <header>
        <h1 class="p-2" align="center">SRI PALANI MURUGAN AGENCIES</h1>
    </header>
    <nav class="navbar navbar-expand-lg sticky-top">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <img src="./media/shop_1-removebg-preview.png" alt="Logo" width="90px" height="50px">
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbar">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="./homelog.py?id={user_id}"><i class="bi bi-house-door-fill"></i> HOME</a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a href="cart.py?id={user_id}" class="nav-link">
                            <i class="bi bi-cart2"></i> Cart
                        </a>
                    </li>
                </ul>
                <div class="dropdown profile-dropdown">
                    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown">
                        <img src="./media/{r[7]}" id="userProfilePic" class="rounded-circle" width="40" height="40">
                        <span id="userName">{r[1]}</span>
                    </button>
                    <ul class="dropdown-menu left">
                        <li><a class="dropdown-item" href="#">My Orders</a></li>
                        <li><a class="dropdown-item" href="Account.py?id={user_id}">Account Settings</a></li>
                        <li><a class="dropdown-item text-danger" href="./home.py" id="logoutBtn">Logout</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>
""")

print(f"""
    <div class="container mt-5">
        <h1 class="text-center">Cart</h1>
        <form action="cart.py?id={user_id}" method="post" id="cartForm">
            <table class="table mt-4">
                <thead>
                    <tr>
                        <th>Image</th>
                        <th>Product</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
""")
for y in cat:
    print(f"""
                    <tr>
                      <td><img src="media/{y[6]}" height="50px" width="50px"></td>
                      <td>{y[8]}</td>
                      <td>{y[5]}</td>
                      <td>
                          <input type="number" name="quantity_{y[2]}" value="{y[4]}" min="1" class="form-control" onchange="updateQuantity('{y[2]}', this.value)">
                      </td>
                      <td>
                          <button type="submit" name="action" value="remove" class="btn btn-danger">Remove</button>
                          <input type="hidden" name="product_id" value="{y[2]}">
                      </td>
                    </tr>
""")
print(f"""
                </tbody>
            </table>
            <h4 class="text-center">Total Amount: <span class="fa fa-inr"></span>{total_amount}</h4>
            <button type="submit" name="action" value="clear" class="btn btn-danger">Clear Cart</button>
        </form>
        <a href="homelog.py?id={user_id}" class="btn btn-primary mt-4">Back to Products</a>
        <a href="cartbuy.py?id={user_id}&total={total_amount}"  id="buy-now" class="btn btn-success mt-4 button float-end">
            <i class="bi bi-bag button"></i> Buy Now</a>
    </div><br><br><br>
<script>
    function updateQuantity(productId, quantity) {{
        // Create a new form data object
        var formData = new FormData();
        formData.append('action', 'update');
        formData.append('product_id', productId);
        formData.append('quantity', quantity);

        // Send the form data using fetch
        fetch('cart.py?id={user_id}', {{
            method: 'POST',
            body: formData
        }}).then(response => response.text()).then(data => {{
            // Optionally, you can reload the page or update the cart dynamically
            location.reload();
        }}).catch(error => {{
            console.error('Error:', error);
        }});
    }}
</script>
""")
print("""
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