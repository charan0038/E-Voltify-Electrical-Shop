#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("Content-type: text/html\n\n")

import pymysql
import cgi
import cgitb

cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="spma")
cur=con.cursor()

# Get product_id and user_id from URL
form = cgi.FieldStorage()
product_id = form.getvalue("product_id")
uid = form.getvalue("id")
category_id = form.getvalue('category_id')
b="""select * from signup where id='%s' """%(uid)
cur.execute(b)
s=cur.fetchall()
for i in s:

   print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> - Product Details</title>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="sty.css">
</head>
<body>
    <header>
        <h1 class="p-2" align="center">SRI PALANI MURUGAN AGENCIES</h1>
    </header>

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
                        <a class="nav-link active" href="./homelog.py?id={uid}"><i class="bi bi-house-door-fill"></i> HOME</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./productlog.py?id={uid}"><i class="bi bi-basket2"></i> PRODUCTS</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                            <i class="bi bi-book-fill"></i> POPULAR BRANDS
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="./havells.py?id={uid}">Havells</a></li>
                            <li><a class="dropdown-item" href="./polycab.py?id={uid}">Polycab India Ltd</a></li>
                            <li><a class="dropdown-item" href="./Anchor.py?id={uid}">Anchor By Panasonic</a></li>
                            <li><a class="dropdown-item" href="./Goldmedal.py?id={uid}">Goldmedal</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./contactlog.py?id={uid}"><i class="bi bi-person-rolodex"></i> CONTACT</a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a href="cart.py?id={uid}" class="nav-link">
                            <i class="bi bi-cart2"></i> Cart
                        </a>
                    </li>
                    <div class="dropdown profile-dropdown">
                        <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown">
                            <img src="./media/{i[7]}" class="rounded-circle" width="40" height="40">
                            <span>{i[1]}</span>
                        </button>
                        <ul class="dropdown-menu left">
                            <li><a class="dropdown-item" href="#">My Orders</a></li>
                            <li><a class="dropdown-item" href="#">Account Settings</a></li>
                            <li><a class="dropdown-item text-danger" href="./home.py">Logout</a></li>
                        </ul>
                    </div>
                </ul>
            </div>
        </div>
    </nav>""")
v = """SELECT * FROM products WHERE product_id= %s """%(product_id)
cur.execute(v)
product = cur.fetchall()
for j in product:
    print(f"""
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-6">
                <img src="./media/{j[7]}" class="img-fluid" alt="">
            </div>
            <div class="col-md-6">
                <h4>{j[1]}</h4>
                <p><strong>Brand:</strong> {j[2]}</p>
                <h4 class="text-danger"><i class="bi bi-currency-rupee"></i>{j[4]}</h4>
                <p><strong>Stock:</strong> {j[5]} Available</p>
                <form action="" method="POST">
                    <input type="hidden" name="product_id" value="{j[0]}">
                    <input type="hidden" name="uid" value="{uid}">
                    <p><strong>Warranty:</strong> {j[8]} Year</p>
                    <p><strong>Color:</strong> {j[9]}</p>
                    <p><strong>About:</strong> {j[10]}</p>
                    <label><strong>Quantity:</strong></label>
                    <input type="number" name="quantity" min="1" max="{j[5]}" value="1" class="form-control w-25" required><br>
                    <p>{j[6]}</p>
                    <div class="rating">
                        <span class="star" data-value="1"><i class="bi bi-star"></i></span>
                        <span class="star" data-value="2"><i class="bi bi-star"></i></span>
                        <span class="star" data-value="3"><i class="bi bi-star"></i></span>
                        <span class="star" data-value="4"><i class="bi bi-star"></i></span>
                        <span class="star" data-value="5"><i class="bi bi-star"></i></span>
                    </div>
                    <input type="hidden" name="rating" id="hiddenRating" value="0">
                </form>

                <form action="navvv.py" method="POST">
                    <input type="hidden" name="product_id" value="{j[0]}">
                    <input type="hidden" name="user_id" value="{uid}">
                    <input type="hidden" name="brand_name" value="{j[2]}">
                    <input type="hidden" name="product_price" value="{j[4]}">
                    <input type="hidden" name="product_image" value="{j[7]}">
                    <input type="hidden" name="product_name" value="{j[1]}">
                    <input type="hidden" name="color1" value="{j[9]}">
                    <button type="submit" class="btn btn-warning">Add to Cart</button>
                </form>

                <a href="buy.py?id={uid}&product_id={j[0]}" class="btn btn-success"><i class="bi bi-bag"></i> Buy Now</a>
            </div>
        </div>
    </div><br><br>
    """)


print("""
<div class="container">
<h2 align='center'>Suggest Products</h2>
</div>
<style>
a{
 color: black;
  background-color: transparent;
  text-decoration: none;
}
</style>
<div class="container " align="center">
    <div class="row">""")

c ="""SELECT * from products where category = '%s' limit 4 """ %(category_id)
cur.execute(c)
cat = cur.fetchall()

for y in cat:

    print(f"""
     <div class="col-md-3"><br><br>
        <a href="./productview.py?id={uid}&product_id={y[0]}&category_id={category_id}">
            <div class="card" style="width: 18rem;" id="tea">
                <img src="media/{y[7]}" class="card-img-top" alt="" onerror="this.onerror=null;this.src='media/default.jpg';">

                <div class="card-body">
                    <h5 class="card-title">{y[1]}</h5>
                    <p>{y[2]}</p>
                    <p class="card-text"><b><span class="fa fa-inr"></span>{y[4]}</b></p>

        </a><br>
            <form action="navvv.py" method="POST">
            <input type="hidden" name="product_id" value="{y[0]}">
            <input type="hidden" name="user_id" value="{uid}">
            <input type="hidden" name="brand_name" value="{y[2]}">
            <input type="hidden" name="product_price" value="{y[4]}">
            <input type="hidden" name="product_image" value="{y[7]}">
            <input type="hidden" name="product_name" value="{y[1]}">
            <input type="hidden" name="color1" value="{y[9]}">
            <button type="submit" class="btn btn-warning">Add to Cart</button>
        </form>
        <a href="./productview.py?id={uid}&product_id={y[0]}&category_id={category_id}" class="btn btn-success button"><i class="bi bi-bag"></i> View Details</a><br><br>
    </div>
       </div>
            </div>""")


print("</div></div><br><br>")
print("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.rating .star');
    let selectedRating = 0;

    stars.forEach(star => {
        star.addEventListener('click', function() {
            selectedRating = this.getAttribute('data-value');
            updateRating();
            document.getElementById('hiddenRating').value = selectedRating;
        });
    });

    function updateRating() {
        stars.forEach(star => {
            if (star.getAttribute('data-value') <= selectedRating) {
                star.classList.add('selected');
            } else {
                star.classList.remove('selected');
            }
        });
    }
});
</script>
""")
print("""
<style>
.rating {
    display: inline-block;
}

.rating .star {
    cursor: pointer;
    color: #ccc;
    font-size: 24px;
}

.rating .star:hover,
.rating .star:hover ~ .star {
    color: #ffd700;
}

.rating .star.selected {
    color: #ffd700;
}
</style>

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
""")


