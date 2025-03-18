#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
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
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./productlog.py?id={uid}"><i class="bi bi-basket2"></i> PRODUCTS</a>
                    </li>

                    
                    <li class="nav-item">
                        <a class="nav-link" href="./contactlog.py?id={uid}"><i class="bi bi-person-rolodex"></i> CONTACT</a>
                    </li>
                </ul>


                <form class="d-flex  mt-3" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    </form>


                <ul class="navbar-nav">

                    <li class="nav-item">
                        <a href="cart.py?id={uid}" class="nav-link">
                            <i class="bi bi-cart2"></i> Cart
                        </a>
                    </li>

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


    <main>
        <section> <br><br><br>


            <div class="container text-center">
                <div class="row">
                    <div class="col-md-4 m-3"><br><br>
                        <img src="./media/eletrical first.webp" alt="Electrical Product Display" class="img-fluid">
                    </div>

                    <div class="col-md-7">
                        <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel"
                            data-bs-pause="hover">
                            <div class="carousel-indicators">
                                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0"
                                    class="active" aria-current="true" aria-label="Slide 1"></button>
                                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1"
                                    aria-label="Slide 2"></button>
                                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2"
                                    aria-label="Slide 3"></button>
                            </div>

                            <div class="carousel-inner">
                                <div class="carousel-item active" data-bs-interval="5000">
                                    <img src="./media/all things 1.jpg" class="d-block w-100"
                                        alt="Slide 1 - Product Showcase">
                                </div>
                                <div class="carousel-item" data-bs-interval="5000">
                                    <img src="./media/all things 2.jpg" class="d-block w-100"
                                        alt="Slide 2 - Product Showcase">
                                </div>
                                <div class="carousel-item">
                                    <img src="./media/all things 3.avif" class="d-block w-100"
                                        alt="Slide 3 - Product Showcase">
                                </div>
                            </div>

                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark"
                                data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark"
                                data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            
            
              <style>
        .parent {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-template-rows: repeat(4, 1fr);
            gap: 8px;
            margin: 5px;
        }
            
        
        .div2 {
            grid-column-start: 3;
            grid-row-start: 1;
        }
        
        .div3 {
            grid-column-start: 2;
            grid-row-start: 1;
        }
        #r{
            margin: 15px;
            text-align:center;
            text-size-adjust: 18px ;
            color: rgb(38, 45, 43);
            
        }
        #te:hover{
    transform: scale(1.02);
    transition:0.3s ease-in-out ;
    box-shadow: 2px 2px 5px black;
}
#te{
    border-radius: 20px;
}
.co{
    margin-bottom:-650px;
    }
    </style>""")
print(f"""

<div class="container co">
        <br><h1 ID="r" >POPULAR BRANDS</h1>
    <div class="parent">
        <div id="te" class="div1">
           <a href="havellslog.py?id={uid}"> <img src="./media/Havells Logo 3.jpg"  alt="" height="200px" width="100%"></a>
        </div>
        <div id="te" class="div2">
            <a href="polycablog.py?id={uid}"><img src="./media/polycab logo3.jpg" alt="" height="200px" width="300px"></a>
        </div>
        <div id="te" class="div3">
            <a href="goldmedallog.py?id={uid}"><img src="./media/goldmedal logo 1.jpg" alt="" height="200px" width="300px"></a>
        </div>
        <div id="te" class="div4">
            <a href="anchorlog.py?id={uid}"><img src="./media/Anchor logo1.jpg" alt="" height="200px" width="300px"></a>
        </div>
    </div>
</div>


            <div class="container" align="center">
                <br><br><br>
                <h2> Top Selling Products</h2><br><br><br>

            </div>


            <div class="container " align="center">
                <img src="./media/all led blubs.png" alt="" class="rounded" height="auto" width="100%">

                <div class="row" id="product-list">""")



category = "LEDBlubs"
query = "SELECT * FROM products WHERE category = %s LIMIT 4"
cur.execute(query, (category,))
r = cur.fetchall()

for p in r:


    print(f"""
    <div class="col-md-3"><br><br>
        <a href="./productview.py?id={uid}&product_id={p[0]}&category_id={p[3]}">
            <div class="card" style="width: 18rem;" id="tea">
                <img src="media/%s" class="card-img-top" alt="" onerror="this.onerror=null;this.src='media/default.jpg';">

                <div class="card-body">
                    <h5 class="card-title">{p[1]}</h5>
                    <p>{p[2]}</p>
                    <p class="card-text"><b><span class="fa fa-inr"></span>{p[4]}</b></p>
             
        </a><br>
        <form action="navvv.py" method="POST">
            <input type="hidden" name="product_id" value="{p[0]}">
            <input type="hidden" name="user_id" value="{uid}">
            <input type="hidden" name="brand_name" value="{p[2]}">
            <input type="hidden" name="product_price" value="{p[4]}">
            <input type="hidden" name="product_image" value="{p[7]}">
            <input type="hidden" name="product_name" value="{p[1]}">
            <input type="hidden" name="color1" value="{p[9]}">
            <button type="submit" class="btn btn-warning">Add to Cart</button>
        </form>
           <a href="./productview.py?id={uid}&product_id={p[0]}&category_id={p[3]}" class="btn btn-success button"><i class="bi bi-bag"></i> View Details</a><br><br>

    </div>
       </div>
            </div>
    """%(p[7]))

print("</div></div>")


print("""                              
                            
                    
                           
                            <div class="container " align="center">
                             <img src="./media/rr-fans.jpg" alt="" width="100%" class="rounded mt-5"><br><br>
                                <div class="row">""")


category = "fans"
query = "SELECT * FROM products WHERE category = %s LIMIT 4"
cur.execute(query, (category,))
r = cur.fetchall()

for e in r:

    print(f"""
    <div class="col-md-3"><br><br>
        <a href="./productview.py?id={uid}&product_id={e[0]}&category_id={e[3]}">
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
        <a href="./productview.py?id={uid}&product_id={e[0]}&category_id={e[3]}" class="btn btn-success button"><i class="bi bi-bag"></i> View Details</a><br><br>
    </div>
       </div>
            </div>
    """%(e[1]))

print("</div></div>")
print("""   
                                    <div class="container"><br><br>
                                        <img src="./media/all wires.png" alt="" width="100% " height="auto" class="rounded">
                                    </div>
                                    <div class="container " align="center">
                                        <div class="row">""")


category = "wiring"
query = "SELECT * FROM products WHERE category = %s LIMIT 4"
cur.execute(query, (category,))
r = cur.fetchall()

for h in r:

    print(f"""
    <div class="col-md-3"><br><br>
        <a href="./productview.py?id={uid}&product_id={h[0]}&category_id={h[3]}">
            <div class="card" style="width: 18rem;" id="tea">
                <img src="media/{h[7]}" class="card-img-top" alt="" >

                <div class="card-body">
                    <h5 class="card-title">{h[1]}</h5>
                    <p>{h[2]}</p>
                    <p class="card-text"><b><span class="fa fa-inr"></span>{h[4]}</b></p>

        </a><br>
        <form action="navvv.py" method="POST">
            <input type="hidden" name="product_id" value="{h[0]}">
            <input type="hidden" name="user_id" value="{uid}">
            <input type="hidden" name="brand_name" value="{h[2]}">
            <input type="hidden" name="product_price" value="{h[4]}">
            <input type="hidden" name="product_image" value="{h[7]}">
            <input type="hidden" name="product_name" value="%s">
            <button type="submit" class="btn btn-warning">Add to Cart</button>
        </form>
        <a href="./productview.py?id={uid}&product_id={h[0]}&category_id={h[3]}" class="btn btn-success button"><i class="bi bi-bag"></i> View Details</a>
    </div>
       </div>
            </div>
    """%(h[1]))


print("</div></div>")


print("""

    </section>
        <aside>
            <h1 style="font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;"
                class="text-center mt-4">
                OUR SHOP VIEW
            </h1>
            <div class="container ">
                <div class="row">
                    <!-- Left Image Section -->
                    <div class="col-md-4 mb-3">
                        <img src="./media/homelast-removebg-preview.png" alt="Electrical Product Display"
                            class="img-fluid rounded"><br><br>
                        <img src="./media/Electrician_png_images-removebg-preview.png" alt="">
                    </div>

                    <!-- Right Carousel Section -->
                    <div class="col-md-8"><br><br>
                        <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel"
                            data-bs-pause="hover">
                            <!-- Carousel Indicators -->
                            <div class="carousel-indicators">
                                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0"
                                    class="active" aria-current="true" aria-label="Slide 1"></button>
                                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1"
                                    aria-label="Slide 2"></button>
                                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2"
                                    aria-label="Slide 3"></button>
                            </div>

                            <!-- Carousel Images -->
                            <div class="carousel-inner">
                                <div class="carousel-item active">
                                    <img src="./media/pho1.jpg" class="d-block w-100" alt="A scenic view of Malumichampatti">
                                    <div class="carousel-caption d-none d-md-block">
                                        <!-- Add captions here if needed -->
                                    </div>
                                </div>
                                <div class="carousel-item">
                                    <img src="./media/pho4.jpg" class="d-block w-100"
                                        alt="A landscape view at Malumichampatti">
                                    <div class="carousel-caption d-none d-md-block">
                                        <!-- Add captions here if needed -->
                                    </div>
                                </div>
                                <div class="carousel-item">
                                    <img src="./media/pho3.jpg" class="d-block w-100"
                                        alt="A picturesque scene from Malumichampatti">
                                    <div class="carousel-caption d-none d-md-block">
                                        <!-- Add captions here if needed -->
                                    </div>
                                </div>
                            </div>

                            <!-- Carousel Controls -->
                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark"
                                data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark"
                                data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>

        </aside>
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