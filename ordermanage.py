#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
import sys
import smtplib
from email.mime.text import MIMEText

sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()

# Database connection
con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
# Handle form submission for order status update
if form.getvalue('order_id') and form.getvalue('status'):
    order_id = form.getvalue('order_id')
    new_status = form.getvalue('status')

    # Ensure order_id and new_status are single values
    if isinstance(order_id, list):
        order_id = order_id[0]
    if isinstance(new_status, list):
        new_status = new_status[0]

    update_query = "UPDATE orders SET order_status = %s WHERE order_id = %s"
    try:
        cur.execute(update_query, (new_status, order_id))
        con.commit()

        if new_status == 'Cancelled':
            # Fetch user email from the database
            fetch_email_query = "SELECT mail FROM signup WHERE id = %s"
            cur.execute(fetch_email_query, (uid,))
            user_email = cur.fetchone()

            if user_email:
                user_email = user_email[0]
                sender_email = "spma483@gmail.com"
                sender_password = "ggik alzy dqvj nyve"
                recipient_email = user_email
                subject = "Order Cancelled"
                body = f"Your order with ID {order_id} has been cancelled."

                msg = MIMEText(body)
                msg['Subject'] = subject
                msg['From'] = sender_email
                msg['To'] = recipient_email

                try:
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                        server.login(sender_email, sender_password)
                        server.sendmail(sender_email, recipient_email, msg.as_string())
                    print(f"""
                    <script>
                        alert('Order status updated successfully and email sent to the customer!');
                        window.location.href = 'Ordermanage.py'; // Redirect to the same page to refresh the orders list
                    </script>
                    """)
                except smtplib.SMTPException as e:
                    print(f"""
                    <script>
                        alert('Failed to send email: {e}');
                        window.location.href = 'Ordermanage.py'; // Redirect to the same page
                    </script>
                    """)
            else:
                print(f"""
                <script>
                    alert('Failed to fetch user email for order ID {order_id}');
                    window.location.href = 'Ordermanage.py'; // Redirect to the same page
                </script>
                """)
        else:
            print(f"""
            <script>
                alert('Order status updated successfully!');
                window.location.href = 'Ordermanage.py'; // Redirect to the same page to refresh the orders list
            </script>
            """)
    except pymysql.MySQLError as e:
        print(f"""
        <script>
            alert('Failed to update order status: {e}');
            window.location.href = 'Ordermanage.py'; // Redirect to the same page
        </script>
        """)

print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Boxicons CSS -->
    <link href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css" rel="stylesheet">
    <!-- Bootstrap 5 JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link href="https://cdn.lineicons.com/5.0/lineicons.css" rel="stylesheet">
    <link rel="stylesheet" href="./style.css">
</head>

<style>
a {
    text-decoration: none;
}
</style>

<body>

<header>
    <a class="navbar-brand float-start" href="#">
        <img src="./media/shop_1-removebg-preview.png" alt="Logo" width="90px" height="50px">
    </a>
    <h1 class="p-2 text-center">SRI PALANI MURUGAN AGENCIES</h1>
</header>

<div class="wrapper">
    <aside id="sidebar">
        <div class="d-flex">
            <button class="toggle-btn" type="button">
                <i class="lni lni-dashboard-square-1"></i>
            </button>
            <div class="sidebar-logo">
                <a href="#">Admin Panel</a>
            </div>
        </div>
        <ul class="sidebar-nav">
            <li class="sidebar-item">
                <a href="./Admine.py" class="sidebar-link">
                    <i class="lni lni-user-4"></i>
                    <span>Dashboard</span>
                </a>
            </li>
            <li class="sidebar-item">
                <a href="./manageproduct.py" class="sidebar-link">
                    <i class="lni lni-basket-shopping-3"></i>
                    <span>Manage Products</span>
                </a>
            </li>
            <li class="sidebar-item">
                <a href="./Ordermanage.py" class="sidebar-link">
                    <i class="lni lni-notebook-1"></i>
                    <span> Order Details </span>
                </a>
            </li>
            <li class="sidebar-item">
                <a href="./usermanage.py" class="sidebar-link">
                    <i class="lni lni-user-multiple-4"></i>
                    <span> Manage Users </span>
                </a>
            </li>
        </ul>
        <div class="sidebar-footer">
            <a href="./home.py" class="sidebar-link">
                <i class="lni lni-power-button"></i>
                <span>Logout</span>
            </a>
        </div>
    </aside>

    <div class="main">
        <nav class="navbar navbar-expand px-4 py-3">
            <div class="navbar-collapse collapse">
                <h3 class="fw-bold">Admin Dashboard</h3>
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item dropdown">
                        <a href="#" data-bs-toggle="dropdown" class="nav-icon pe-md-0">
                            <img src="./media/account.png" class="avatar img-fluid" alt="">
                        </a>
                    </li>
                </ul>
            </div>
        </nav>

        <div class="container mt-5">
            <h2>Orders List</h2>
            <table class="table table-bordered table-hover">
                <tr>
                    <th>Order ID</th>
                    <th>User ID</th>
                    <th>Address</th>
                    <th>Product</th>
                    <th>Total Price</th>
                    <th>Payment Method</th>
                    <th>Order Status</th>
                    <th>Order Date</th>
                    <th>Quantity</th>
                    <th>Action</th>
                </tr>
""")

# Fetch and display orders
try:
    query = "SELECT * FROM orders"
    cur.execute(query)
    rows = cur.fetchall()

    for order in rows:
        print(f"""
                <tr>
                    <td>{order[0]}</td>
                    <td>{order[1]}</td>
                    <td>{order[2]}</td>
                    <td>{order[3]}</td>
                    <td>{order[4]}</td>
                    <td>{order[5]}</td>
                    <td>
                        <form method="POST" action="Ordermanage.py">
                            <input type="hidden" name="order_id" value="{order[0]}">
                            <select name="status" class="form-select">
                                <option value="Pending" {'selected' if order[6] == 'Pending' else ''}>Pending</option>
                                <option value="Processing" {'selected' if order[6] == 'Processing' else ''}>Processing</option>
                                <option value="Shipped" {'selected' if order[6] == 'Shipped' else ''}>Shipped</option>
                                <option value="Delivered" {'selected' if order[6] == 'Delivered' else ''}>Delivered</option>
                                <option value="Cancelled" {'selected' if order[6] == 'Cancelled' else ''}>Cancelled</option>
                            </select>
                            
                    </td>
                    <td>{order[7]}</td>
                    <td>{order[8]}</td>
                    <td><button type="submit" class="btn btn-primary">Update</button>
                        </form>
                    </td>
                </tr>
        """)

except pymysql.MySQLError as e:
    print(f"<tr><td colspan='10'>Error fetching data: {e}</td></tr>")

print("""
            </table>
        </div>
    </div>
</div>

<script>
    const hamBurger = document.querySelector(".toggle-btn");
    hamBurger.addEventListener("click", function () {
        document.querySelector("#sidebar").classList.toggle("expand");
    });
</script>

</body>
</html>
""")