#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
import sys

sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
order_id = form.getvalue("order_id")

if 'order_id' in form and form.getvalue('cancel_order'):
    order_id = form.getvalue('order_id')

    try:
        cur.execute("UPDATE orders SET order_status='Cancelled' WHERE order_id=%s", (order_id,))
        con.commit()
        print(""" <script>
               alert("Order Cancelled...!");
               </script>""")
    except pymysql.MySQLError as e:
        print(f"<p>Error canceling order: {e}</p>")

print("""<!DOCTYPE html>
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
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .content {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            text-align: center;
            color: #333;
        }
        .table-responsive {
            overflow-x: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
            color: #333;
            font-weight: bold;
        }
        tr:hover {
            background-color: #f5f5f5;
        }
        .btn {
            display: inline-block;
            padding: 6px 12px;
            margin-bottom: 0;
            font-size: 14px;
            font-weight: normal;
            line-height: 1.42857143;
            text-align: center;
            white-space: nowrap;
            vertical-align: middle;
            cursor: pointer;
            background-image: none;
            border: 1px solid transparent;
            border-radius: 4px;
        }
        .btn-primary {
            color: #fff;
            background-color: #337ab7;
            border-color: #2e6da4;
        }
        .btn-primary:hover {
            color: #fff;
            background-color: #286090;
            border-color: #204d74;
        }
        @media (max-width: 768px) {
            th, td {
                padding: 8px;
            }
            .btn {
                padding: 4px 8px;
                font-size: 12px;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1 class="p-2" align="center">SRI PALANI MURUGAN AGENCIES</h1>
    </header>""")
cur.execute("SELECT * FROM signup WHERE id=%s", (uid,))
r = cur.fetchone()
if r:
    print(f"""
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
                        <a class="nav-link active" aria-current="page" href="./homelog.py?id={uid}"><i
                                class="bi bi-house-door-fill"></i> HOME</a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <div class="dropdown profile-dropdown">
                        <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown">
                            <img src="./media/{r[7]}" id="userProfilePic" class="rounded-circle" width="40" height="40">
                            <span id="userName">{r[1]}</span>
                        </button>
                        <ul class="dropdown-menu left">
                            <li><a class="dropdown-item" href="./sam.py?id={uid}">My Orders</a></li>
                            <li><a class="dropdown-item" href="./Account.py?id={uid}">Account Settings</a></li>
                            <li><a class="dropdown-item text-danger" href="./havells.py" id="logoutBtn">Logout</a></li>
                        </ul>
                    </div>
                </ul>
            </div>
        </div>
    </nav><br><br>
    <div class="container">
        <div class="content">
            <h2 align="center">Your Orders</h2>
            <div class="table-responsive">
                <table class="table table-bordered table-hover">
                    <thead>
                        <tr>
                            <th>Address</th>
                            <th>Product</th>
                            <th>Total Price</th>
                            <th>Payment Method</th>
                            <th>Order Status</th>
                            <th>Order Date</th>
                            <th>Quantity</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
""")
try:

        cur.execute("SELECT * FROM orders WHERE user_id=%s", (uid,))
        rows = cur.fetchall()
        for order in rows:
            print(f"""
                <tr>
                    <td>{order[2]}</td>
                    <td>{order[3]}</td>
                    <td>{order[4]}</td>
                    <td>{order[5]}</td>
                    <td>{order[6]}</td>
                    <td>{order[7]}</td>
                    <td>{order[8]}</td>
                    <td>
                        <form action="" method="post">
                            <input type="hidden" name="order_id" value="{order[0]}">
                            <input type="submit" class="btn btn-danger" name="cancel_order" value="Cancel Order">
                        </form>
                    </td>
                </tr>
            """)


except pymysql.MySQLError as e:
    print(f"<tr><td colspan='7'>Error fetching data: {e}</td></tr>")
print("""
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <footer>
        <div class="container"><br><br><br>
            <div class="row"><br><br><br>
                <div class="col-md-4" align="center">
                    <h4>Address</h4>
                    <p align="center"> <a href="" id="k" style="text-decoration: none;"><i
                                class="bi bi-geo-alt-fill"></i>
                            1/189-1,Vadakku Thottam Salai,<br>Malumichampatti,<br>Coimbatore-641050</a><br><br>
                        <a href="" style="text-decoration: none;" id="k"><i class="bi bi-envelope-fill"></i>
                            spmagencies1819@gmail.com</a><br><br>
                        <a href="" id="k" style="text-decoration: none;"><i class="bi bi-telephone-fill"></i> +91
                            7708166635</a>
                    </p>
                </div>
                <div class="col-md-4" align="center">
                    <h4>Working Hours</h4><br>
                    <p><i class="bi bi-alarm-fill"></i> Monday to Saturday: 9:00 AM – 8:00 PM</p>
                    <p><i class="bi bi-alarm-fill"></i> Sunday: 9:00 AM – 2:00 PM </p><br><br>
                    <p style="font-size: larger; ">
                        <div class="link">
                            <a href=""><span class="fa fa-whatsapp"></span></a>
                            <a href=""><span class="fa fa-instagram"></span></a>
                            <a href=""><span class="fa fa-facebook"></span></a>
                            <a href=""><span class="fa fa-twitter"></span></a>
                        </div>
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
                    <p align="center"> Copyrights <i class="bi bi-c-circle"></i> 2025 & SRI
                        PALANI MURUGAN
                        AGENCIES.All Rights Reserved</p>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>
""")