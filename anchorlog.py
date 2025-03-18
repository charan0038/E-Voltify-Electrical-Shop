#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")

# Secure query execution
cur.execute("SELECT * FROM signup WHERE id=%s", (uid,))
r = cur.fetchone()

if r:  # Check if user exists
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
                <img src="./media/shop_1-removebg-preview.png" alt="Logo" width="90px" height="50px">
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbar">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="./homelog.py?id={uid}">
                            <i class="bi bi-house-door-fill"></i> HOME
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./productlog.py?id={uid}">
                            <i class="bi bi-basket2"></i> PRODUCTS
                        </a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                            <i class="bi bi-book-fill"></i> POPULAR BRANDS
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="./havellslog.py?id={uid}">Havells</a></li>
                            <li><a class="dropdown-item" href="./polycablog.py?id={uid}">Polycab India Ltd</a></li>
                            
                            <li><a class="dropdown-item" href="./Goldmedallog.py?id={uid}">Goldmedal</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./contactlog.py?id={uid}">
                            <i class="bi bi-person-rolodex"></i> CONTACT
                        </a>
                    </li>
                </ul>

                <form class="d-flex mt-3" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                </form>

                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a href="cart.py?id={uid}" class="nav-link">
                            <i class="bi bi-cart2"></i> Cart
                        </a>
                    </li>
                    <div class="dropdown profile-dropdown">
                        <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown">
                            <img src="./media/{r[7]}" id="userProfilePic" class="rounded-circle" width="40" height="40">
                            <span id="userName">{r[1]}</span>
                        </button>
                        <ul class="dropdown-menu left">
                            <li><a class="dropdown-item" href="#">My Orders</a></li>
                            <li><a class="dropdown-item" href="#">Account Settings</a></li>
                            <li><a class="dropdown-item text-danger" href="./anchor.py" id="logoutBtn">Logout</a></li>
                        </ul>
                    </div>
                </ul>
            </div>
        </div>
    </nav>
    """)



print("""
<div class="container">
        <br><br><img src="./media/Anchor length.png" alt="" class="roun"  width="100%" >
        </div>


        <div class="container " align="center">
            <div class="row" id="productContainer">
            <h2>ANCHOR</h2><br><br><br>""")
brand = "Anchor"
query = "SELECT * FROM products WHERE brand = %s LIMIT 12"
cur.execute(query, (brand,))
r = cur.fetchall()

for e in r:

    print(f"""
    <div class="col-md-3 product-item"><br><br>
        <a href="./productview.py?id={uid}&product_id={e[0]}&brand_id={e[2]}&category_id={e[3]}">
            <div class="card" style="width: 18rem;" id="tea">
                <img src="media/{e[7]}" class="card-img-top" alt="" >

                <div class="card-body">
                    <h5 class="card-title">{e[1]}</h5>
                    <p>{e[2]}</p>
                    <p class="card-text"><b><span class="fa fa-inr"></span>{e[4]}</b></p>

        </a><br>
        <form action="navvv.py" method="POST">
            <input type="hidden" name="product_id" value="{e[0]}">
            <input type="hidden" name="user_id" value="{uid}">
            <input type="hidden" name="brand_name" value="{e[2]}">
            <input type="hidden" name="product_price" value="{e[4]}">
            <input type="hidden" name="product_image" value="{e[7]}">
            <input type="hidden" name="product_name" value="%s">
            <button type="submit" class="btn btn-warning">Add to Cart</button>
        </form>
        <a href="./productview.py?product_id={e[0]}&uid={uid}&brand_id={e[3]}&category_id={e[3]}" class="btn btn-success button"><i class="bi bi-bag"></i> View Details</a><br><br>
    </div>
       </div>
            </div>
    """%(e[1]))

print("</div></div>")
print("""
                    
                    <article>
                        <div class="container">
                            <br><br><br>
                            <h2>About Us</h2><br><br>
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
                <script>
                        $(document).ready(function(){
                          $("#myInput").on("keyup", function() {
                            var value = $(this).val().toLowerCase();
                            $(".product-item").filter(function() {
                              $(this).toggle($(this).text().toLowerCase().includes(value));
                            });              

                        if (value.trim() !== "") {
                            $("h2").hide();
                          } else {
                            $("h2").show();
                          }
                        });
                      });
                        </script>
            
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