#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os

cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
total_amount = form.getvalue("total")
product_id = form.getvalue("product_id")

v = """SELECT * FROM signup WHERE id=%s""" % uid
cur.execute(v)
r = cur.fetchone()
if r:
    print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-voltify</title>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"></script>

    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">


    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

    <link rel="stylesheet" href="sty.css">
</head>
<style>
 #tea:hover{
    transform: scale(1.02);
    transition:0.3s ease-in-out ;
    box-shadow: 2px 2px 5px black;
        }
a{
 color: black;
  background-color: transparent;
  text-decoration: none;
}
</style>


<body>
    <header>

        <h1 class="  p-2" align="center ">SRI PALANI MURUGAN AGENCIES</h1>
    </header>""")

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
                        <a class="nav-link active" aria-current="page" href="./homelog.py?id={uid}"><i
                                class="bi bi-house-door-fill"></i> HOME</a>
                    <li class="nav-item">
                        <a class="nav-link" href="./contactlog.py?id={uid}"><i class="bi bi-person-rolodex"></i> CONTACT</a>
                    </li>
                </ul>         


                <ul class="navbar-nav">

                  
                   <div class="dropdown profile-dropdown ">
                        <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown">
                                <img src="./media/{r[7]}" id="userProfilePic" class="rounded-circle" width="40" height="40">
                            <span id="userName">{r[1]}</span>
                        </button>
                        <ul class="dropdown-menu left">     
                            <li><a class="dropdown-item" href="./sam.py?id={uid}">My Orders</a></li>
                            <li><a class="dropdown-item" href="./Account.py?id={uid}">Account Settings</a></li>
                            <li><a class="dropdown-item text-danger" href="./home.py" id="logoutBtn">Logout</a></li>
                        </ul>
                    </div>
                </div>
            </div>

              </ul>
            </div>
        </div>
    </nav>""")

print("""

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        .container1 {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        label {
            margin-bottom: 5px;
            font-weight: bold;
            color: #555;
        }

        input[type="number"],
        input[type="text"],
        input[type="email"],
        input[type="password"],
        input[type="submit"] {
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }

        input[type="submit"] {
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        input[type="submit"]:hover {
            background-color: #218838;
        }

        .error {
            color: red;
            font-size: 14px;
            margin-bottom: 10px;
        }

        .success {
            color: green;
            font-size: 14px;
            margin-bottom: 10px;
        }

        .payment-options {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .payment-options label {
            display: flex;
            align-items: center;
        }

        .payment-options input[type="radio"] {
            margin-right: 10px;
        }

        .payment-options .upi-details {
            display: none;
        }

        .payment-options input[type="radio"]:checked + .upi-details {
            display: block;
        }
    </style>
</head>
<body>""")
print("""
    <div class="container1">
        <h1>UPI Payment</h1>
        <form id="paymentForm"  method="POST">
            <label for="amount">Amount:</label>
            <input type="number" id="amount" name="amount" required>
            
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="vpa">VPA (UPI ID):</label>
            <input type="text" id="vpa" name="vpa" required>

            

            <input type="submit" name="submit" value="Pay">
        </form>
    </div>
""")
if form.getvalue("submit"):
    user_id = form.getvalue("user_id")  # Get user ID from form
    name = form.getvalue("name")
    amount = form.getvalue("amount")
    vpa = form.getvalue("vpa")

    if user_id and name and amount and vpa:
        try:
            query = """INSERT INTO payments (user_id, name, amount, vpa) 
                       VALUES (%s, %s, %s, %s)"""
            cur.execute(query, (user_id, name, amount, vpa))
            con.commit()

            print(f"""
                <script>
                    alert("Payment Submitted Successfully!");
                    window.location.href = "homelog.py?id={user_id}"; // Redirect to home page with user ID
                </script>
            """)

        except pymysql.MySQLError as e:
            print(f"""
                <script>
                    alert("Error processing payment: {str(e)}");
                    window.location.href = "payment.py"; // Redirect back to payment page
                </script>
            """)

    else:
        print("""
            <script>
                alert("All fields are required!");
                window.location.href = "payment.py";
            </script>
        """)

print("""<article>
            <div class="container">
                <br>
                <h2 align="center">About Us</h2><br><br>
                <p> Established with the vision of delivering top-notch electrical solutions,
                    Sri Palani Murugan Agencies has earned a reputation for excellence.
                    Guided by a commitment to quality and service, we take pride in being a
                    trusted name in the electrical industry. Our shop is built on the principles
                    of integrity, innovation, and a customer-first approach.
                </p>
            </div><br><br>
            <div class="container">
                <div class="row">
                    <h3>Our Products</h3><br><br><br><br>
                    <div class="col-md-5">
                        <b>We stock a comprehensive range of electrical products to cater to diverse needs,
                            including:</b><br><br>

                        <p><b>Wires and Cables:</b> Top brands like Havells, Polycab, and Anchor for safe and reliable
                            wiring.</p>
                        <p><b>Switches and Sockets:</b> Stylish and durable options from brands like Legrand, Anchor,
                            and Goldmedal.</p>
                        <p><b>Lighting Solutions:</b> LED lights, tube lights, and decorative lighting for homes and
                            offices.</p>
                        <p><b>Fans and Appliances:</b> Ceiling fans, exhaust fans, and other energy-efficient
                            appliances.</p>
                        <p><b>Industrial Electrical Equipment:</b> Control panels, circuit breakers, and tools for
                            industrial projects.</p>
                    </div>
                    <div class="col-md-6">
                        <img src="./media/all things 2.jpg" alt="" width="100%" height="400px" class="rounded">
                    </div>
                </div>
            </div><br><br>
            <div class="container">
                <div class="row">
                    <div class="col-md-7">
                        <img src="./media/pho1.jpg" alt="" width="100%" height="400px" class="rounded">
                    </div>
                    <div class="col-md-5">
                        <h3>Our Mission</h3>
                        <p>At Sri Palani Murugan Agencies, our mission is to empower homes and businesses with
                            cutting-edge electrical solutions while upholding the values of trust, quality, and
                            affordability.</p>

                        <h5><b>Visit Us</b></h5>
                        <p>Experience the difference at Sri Palani Murugan Agencies. Whether you're undertaking a small
                            home renovation or managing a large-scale industrial project, we’ve got you covered. Visit
                            our store today at Malumichampatti.</p>

                        <h5>Let’s Stay Connected</h5>
                        <p>Follow us on Instagram,Facebook for the latest updates on products, offers, and promotions.
                        </p>
                    </div>
                </div>
            </div>

        </article><br><br><br>
    </main>

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

</html>""")