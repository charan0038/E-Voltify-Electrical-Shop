#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os, smtplib, random, string

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()
form = cgi.FieldStorage()
action = form.getvalue("action")

otp = None
email = form.getvalue("email")

if action == "send_otp" and email:

    otp = generate_otp()
    v = """select id from userreg where email='%s'""" % (email)
    cur.execute(v)
    r = cur.fetchone()
    if r != None:


      fromadd = 'arabkgm@gmail.com'
      password = 'gpfj scmy kuwi rbir'
      toadd = email
      subject = 'Your OTP'
      body = f'The OTP is {otp}'

      msg = f"Subject:{subject}\n\n{body}"
      server = smtplib.SMTP("smtp.gmail.com:587")
      server.starttls()
      server.login(fromadd, password)
      server.sendmail(fromadd, toadd, msg)
      server.quit()
      print(f" <script>alert('OTP sent to {email}.')</script>")
    else:
        print("""
            <script>
            alert("email not found");
            location.href="home.py";
            </script>
            """)


print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"></script>

    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

  

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="stylesheet" href="sty.css">
</head>

<body>
    <header>

        <h1 class="  p-2" align="center ">SRI PALANI MURUGAN AGENCIES</h1>
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
                        <a class="nav-link active" aria-current="page" href="./home.py"><i
                                class="bi bi-house-door-fill"></i> HOME</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./product.py"><i class="bi bi-basket2"></i> PRODUCTS</a>
                    </li>

               
                    <li class="nav-item">
                        <a class="nav-link" href="./contact.py"><i class="bi bi-person-rolodex"></i> CONTACT</a>
                    </li>
                </ul>


                <ul class="navbar-nav">

                   

                    <li class="nav-item dropdown">
                        <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">
                            <i class="bi bi-door-open-fill"></i> Sign in
                        </a>
                        <ul class="dropdown-menu">
                            <li><a href="#" class="dropdown-item" data-bs-toggle="modal" data-bs-target="#log">User
                                    Sign-in</a></li>
                            <li><a href="#adm" class="dropdown-item" data-bs-toggle="modal">Admin Log-in</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a href="#inlog" class="nav-link" data-bs-toggle="modal" data-bs-target="#sing">
                            <i class="bi bi-door-open"></i> Sign up
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="modal fade" id="adm" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">ADMIN LOG-IN</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <script>
                        function valid() {
                            const un = document.forms["val"]["Name"];
                            const pa = document.forms["val"]["Password"];
                            const user = "Admin";
                            const pass = "AD123";

                            if (un.value === "") {
                                alert("Username is required!");
                                un.focus();
                                return false;
                            } else if (pa.value === "") {
                                alert("Password is required!");
                                pa.focus();
                                return false;
                            } else if (un.value === user && pa.value === pass) {
                                return true;
                            } else {
                                alert("Please enter a valid username or password!");
                                return false;
                            }
                        }
                    </script>
                    <form action="./Admine.py" name="val" class="form-group" onsubmit="return valid()">
                        <label for="Name" class="form-label">Username</label>
                        <input type="text" id="user" name="Name" class="form-control" placeholder="Enter Your Username">
                        <label for="Password" class="form-label">Password</label>
                        <input type="password" name="Password" class="form-control" placeholder="Enter Your Password"
                            id="pass">
                </div>
                <div class="modal-footer">
                    <input type="submit" name="Log-in" value="Log-in" class="btn btn-success">
                    <input type="reset" name="cancel" value="Cancel" class="btn btn-danger">
                    </form>
                </div>
            </div>
        </div>
    </div>

    <div class="modal fade" id="log" id="#singup" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">USER SIGN-IN</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form action="" class="form-group" name="login-form">
                        <label for="">Username:</label>
                        <input type="text" id="username" class="form-control" required placeholder="Enter Your Username"
                            name="username"><br>
                        <label for="">Password:</label>
                        <input type="password" id="password" name="word" required class="form-control"
                            placeholder="Enter Your Password"><br>
                        <button type="submit" class="btn btn-success form-control" name="Sign-in" value="Sign-in">Sign-in</button><br><br>
                        <a href=""  data-bs-target="#got" name="Forgot password" data-bs-toggle="modal" style="text-decoration: none;">Forgot password</a>
                        <a href="" data-bs-target="#sing" data-bs-toggle="modal"  name="Forgot password" style="text-decoration: none;" class="float-end">Sing-up</a> 

                </div>
                <div class="modal-footer">
                    <input type="reset" name="cancel" id="cancel" class="btn btn-danger">
                    </form>
                </div> 
            </div>
        </div>
    </div>""")

username = form.getvalue("username")
passw = form.getvalue("word")
submit = form.getvalue("Sign-in")
if submit:
    v = """SELECT id FROM signup WHERE name='%s' AND pass='%s'""" % (username, passw)
    cur.execute(v)
    r = cur.fetchone()
    if r is not None:
        print("""
                <script>
                alert("Login Successfully");
                location.href='homelog.py?id=%s';
                </script>
            """ % (r[0]))
    else:
        print("""
            <script>
            alert('username and password does not exist');
            </script>
            """)
print("""
    <div class="modal fade" id="got" id="#singup" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Forgot Password</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form action="" class="form-group" name="login-form">
                        <label for="">Enter Your Mail-id :</label>
                        <input type="Email" id="Email" class="form-control" required placeholder="Enter Your Email_id"
                            name="Email"><br>
                            <a href="" data-bs-target="#for" data-bs-toggle="modal" name="Submit" 
                        class="btn btn-success float-start" style="text-decoration: none;">Submit</a>

                    <input type="reset" name="cancel" id="cancel" class="btn btn-danger float-end">
                </form>
                </div>
                    <div class="modal-footer">  
                </div> 
            </div>
        </div>
    </div>""")

print("""
    <div class="modal fade" id="for" id="#singup" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Forgot Password</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form action="" class="form-group" name="login-form">
                        <label for="">Enter Your OTP :</label>
                        <input type="text" id="OTP" class="form-control" required placeholder="Enter Your OTP"
                            name="OTP"><br>
                            <a href="" data-bs-target="#pas" data-bs-toggle="modal" name="Submit" 
                        class="btn btn-success float-start" style="text-decoration: none;">Submit</a>

                    <input type="reset" name="cancel" id="cancel" class="btn btn-danger float-end">
                </form>
                </div>
                    <div class="modal-footer">  
                </div> 
            </div>
        </div>
    </div>""")
print("""

    

    <div class="modal fade" id="pas" id="#singup" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Enter Your New  Password</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form action="" class="form-group" name="login-form">
                        <label for="">New Password:</label>
                        <input type="password" id="password" class="form-control" required placeholder="Enter Your New Password..!"
                            name="Password"><br>
                            <label for="">Confrim Password:</label>
                            <input type="password" id="password" class="form-control" required placeholder="Enter Your New Password..!"
                                name="Password"><br>
                            <a href="" data-bs-target="#log" data-bs-toggle="modal" name="Submit" 
                        class="btn btn-success float-start" style="text-decoration: none;">Submit</a>

                    <input type="reset" name="cancel" id="cancel" class="btn btn-danger float-end">
                </form>
                </div>
                    <div class="modal-footer">  
                </div> 
            </div>
        </div>
    </div> """)

print("""

        
                <div class="modal fade" id="sing" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Sign up</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form  class="form-group" enctype="multipart/form-data" method="post">
                                <label for=" ">Username:</label>
                                    <input type="text" name="Username" id="name" class="form-control" required
                                        placeholder="Please Enter Your Username"><br>
                                    <label for="mobile_number">Mobile Number:</label>
                                    <input type="number" name="Mobile_number" id="Mobile number" class="form-control" required
                                        placeholder="Please Enter your mobile number"><br>
                                        
                        <label for="gender" >Gender: </label><br>
                        <label for="male">
                        <input type="radio" name="gender" id="male" value="male" >Male
                        </label>
                        <label for="female"> 
                            <input type="radio" name="gender" id="female" value="Female">
                            Female</label><br><br>
            
                                    <label for="mail">Email:</label>
                                    <input type="email" name="mail" id="mail" class="form-control" required
                                        placeholder="Please Enter Your Email-id"><br>
                                    <label for="Address "> Address:</label>
                                    <textarea type="text-area" class="form-control width" name="Address" rows="4" cols="10"></textarea><br><br>
                                    <label for="">password:</label>
                                    <input type="password"  required
                                        placeholder="Please Enter Your Password" name="passwords" class="form-control"><br>
                                    <label for="">Profile:</label>
                                    <input type="file" name="photo" class="form-control"><b><br></b>
                                    <input type="submit" name="submite" data-bs-target="#log" data-bs-toggle="modal" class="btn btn-primary form-control">
            
                            </div>
                            <div class="modal-footer">
                                <input type="reset" name="cancel" value="cancel" class="btn btn-danger">
                                </form>
                            </div>
                        </div>
                    </div>
                </div>""")
if len(form) != None:
    submit = form.getvalue("submite")
    if submit != None:
        name = form.getvalue("Username")
        mobile = form.getvalue("Mobile_number")
        Gender = form.getvalue("gender")
        Email = form.getvalue("mail")
        Address = form.getvalue("Address")
        password = form.getvalue("passwords")
        photo = form['photo']
        if photo.filename:
            fn = os.path.basename(photo.filename)
            open("media/" + fn, "wb").write(photo.file.read())
            v = """insert into signup (name,mobile,gender, mail,Address,Pass,photo) values('%s','%s','%s','%s','%s','%s','%s')""" % \
                (name, mobile, Gender, Email, Address, password, fn)
            cur.execute(v)
            con.commit()
            print("""
            <script>
            alert("Submit Successfully..!");
            </script>""")
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
            border-radius: 1000px;
            
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
    </style>

<div class="container co">
    <br><h1 ID="r" >POPULAR BRANDS</h1>
    <div class="parent">
        <div id="te" class="div1 ">
           <a href="havells.py"> <img src="./media/Havells Logo 3.jpg"  alt="" height="200px" width="100%"></a>
        </div>
        <div id="te" class="div2">
            <a href="polycab.py"><img src="./media/polycab logo3.jpg" alt="" height="200px" width="300px"></a>
        </div>
        <div id="te" class="div3">
            <a href="goldmedal.py"><img src="./media/goldmedal logo 1.jpg" alt="" height="200px" width="300px"></a>
        </div>
        <div id="te" class="div4">
            <a href="anchor.py"><img src="./media/Anchor logo1.jpg" alt="" height="200px" width="300px"></a>
        </div>
    </div>
</div>


            <div class="container" align="center">
                <br><br><br>
                <h2> Top Selling Products</h2><br><br><br>

            </div>
            
           <style>
    .product-card {
        
        height: 380px;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        padding: 10px;
    }
    .product-card img {
        width: 100%;
        height: 150px;
        object-fit: cover;
        border-radius: 5px;
    }
    .product-card .card-body {
        padding: 8px;
    }
    .product-card h5 {
        font-size: 16px;
        font-weight: bold;
        margin: 5px 0;
    }
    .product-card p {
        font-size: 13px;
        color: #555;
        margin: 2px 0;
    }
    #tea:hover{
    transform: scale(1.02);
    transition:0.3s ease-in-out ;
    box-shadow: 2px 2px 5px black;
}
    .product-card .btn {
        font-size: 12px;
        padding: 6px;
    }
   
</style>


            <div class="container " align="center">
                <img src="media/all led blubs.png" alt="" class="rounded" height="auto" width="100%">

                <div class="row" id="product-list">""")
category = "LEDBlubs"
query = "SELECT * FROM products WHERE category = %s LIMIT 4"
cur.execute(query, (category,))
r = cur.fetchall()
for i in r:
    print(f"""
        <div class="col-md-3"><br><br>
            <a href="javascript:void(0);" onclick="relog()" style="text-decoration: none;">
                <div class="card" style="width: 18rem;" id="tea">
                    <img src="media/{i[7]}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{i[1]}</h5>
                        <p>{i[2]}</p>
                        <p class="card-text"><b><span class="fa fa-inr"></span>{i[4]}</b></p>
                        <button  class="btn btn-warning " 
                        >Add to Cart</button><br><br>
                        <button  class="btn btn-success "><i class="bi bi-bag"></i> View Details</button>
                        
                    </div>
                </div>
            </a>
        </div>
    """)

print("</div></div>")

print(""" 
<script>
                        function relog(){
                            var loginModal = new bootstrap.Modal(document.getElementById('log'));
                            loginModal.show();
                            alert('please login ...!')    
                        }
        
</script>
                    <div class="container" align="center"><br><br>
                        <div class="row">
         
                         <img src="./media/rr-fans.jpg" alt="" width="100%" class="rounded mt-5"><br>
                           """)


category = "fans"
query = "SELECT * FROM products WHERE category = %s LIMIT 4"
cur.execute(query, (category,))
r = cur.fetchall()
for i in r:
    print(f"""
    
        <div class="col-md-3"><br><br>
            <a href="javascript:void(0);" onclick="relog()" style="text-decoration: none;">
                <div class="card" style="width: 18rem;" id="tea">
                    <img src="media/{i[7]}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{i[1]}</h5>
                        <p>{i[2]}</p>
                        <p class="card-text"><b><span class="fa fa-inr"></span>{i[4]}</b></p>
                         <button  class="btn btn-warning " 
                        >Add to Cart</button><br><br>
                        <button  class="btn btn-success "><i class="bi bi-bag"></i> View Details</button>
                    </div>
                </div>
            </a>
        </div>
    """)

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
for i in r:
    print(f"""
        <div class="col-md-3"><br><br>
            <a href="javascript:void(0);" onclick="relog()" style="text-decoration: none;">
                <div class="card" style="width: 18rem;" id="tea">
                    <img src="media/{i[7]}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{i[1]}</h5>
                        <p>{i[2]}</p>
                        <p class="card-text"><b><span class="fa fa-inr"></span>{i[4]}</b></p>
                         <button  class="btn btn-warning " 
                        >Add to Cart</button><br><br>
                        <button  class="btn btn-success "><i class="bi bi-bag"></i> View Details</button>
                    </div>
                </div>
            </a>
        </div>
    """)

print("</div></div>")

print("""
                                            <script>
                                                function addToCart(name, price, image) {
                                                    let cart = JSON.parse(localStorage.getItem('cart')) || {};
                                                    if (cart[name]) {
                                                        cart[name].quantity += 1;
                                                    } else {
                                                        cart[name] = { price: parseFloat(price), quantity: 1, image };
                                                    }
                                                    localStorage.setItem('cart', JSON.stringify(cart));
                                                    alert(`${name} added to cart!`);
                                                }

                                                document.querySelectorAll('.add-to-cart').forEach(button => {
                                                    button.addEventListener('click', () => {
                                                        const name = button.getAttribute('data-name');
                                                        const price = button.getAttribute('data-price');
                                                        const image = button.getAttribute('data-image');
                                                        addToCart(name, price, image);
                                                    });
                                                });
                                            </script>
                                            
       
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
        <div class="container"><br><br><br>
            <div class="row"><br><br><br>
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
                    <p align="center"> Copyrights <i class="bi bi-c-circle"></i> 2025 & SRI
                        PALANI MURUGAN
                        AGENCIES.All Rights Reserved</p>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>""")