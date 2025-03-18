#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os

cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")


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
  body{
        background-image: url(./media/aco.jpg);
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
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
                    </ul>
      
          
                    <div class="dropdown profile-dropdown ">
                        <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown">
                                <img src="./media/{r[7]}" id="userProfilePic" class="rounded-circle" width="40" height="40">
                            <span id="userName">{r[1]}</span>
                        </button>
                        <ul class="dropdown-menu left">
                            <li><a class="dropdown-item" href="sam.py?id={uid}">My Orders</a></li>
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
    fieldset{
        background-color: rgb(115, 194, 194);
        border: 2px black;
        border-radius:10px;
        padding: 15px; 
        width:500px;
    }
</style>

    <header></header>
    """)
select_query = "SELECT * FROM signup WHERE id=%s"
cur.execute(select_query, (uid))
r = cur.fetchall()

for i in r:
    print("""
<div class="container mt-4">
    <div class="row justify-content-center">
        <!-- Form Section -->
        <div class="col-lg-6 col-md-8"><br><br>
            <fieldset class="border p-4">
                <legend class="text-center">Edit Account</legend>
                <form class="form-group" enctype="multipart/form-data" method="post">
                    <label for="name">Username:</label>
                    <input type="text" name="Username" id="name" class="form-control" required placeholder="Please Enter Your Username"><br>

                    <label for="mobile_number">Mobile Number:</label>
                    <input type="number" name="Mobile_number" id="mobile_number" class="form-control" required placeholder="Please Enter your mobile number"><br>

                    <label for="mail">Email:</label>
                    <input type="email" name="mail" id="mail" class="form-control" required placeholder="Please Enter Your Email-id"><br>

                    <label for="Address">Address:</label>
                    <textarea class="form-control" name="Address" rows="4" placeholder="Enter your address"></textarea><br>

                    <label for="photo">Profile:</label>
                    <input type="file" name="photo" class="form-control"><br>

                    <input type="submit" name="submite" class="btn btn-primary form-control">
                </form>
            </fieldset>
        </div>

        <!-- Image Section -->
        <div class="col-lg-4 col-md-4 text-center">
            <br><br><br><br><br>
            <img src="./media/Electrician_png_images-removebg-preview.png" alt="Electrician Image" class="img-fluid float-start rounded">
        </div>
    </div>
</div>
""")
if len(form) != None:
    submit = form.getvalue("submite")
    if submit:
        name = form.getvalue("Username")
        mobile = form.getvalue("Mobile_number")
        mid = form.getvalue("id")  # Ensure the form has this field
        Email = form.getvalue("mail")
        Address = form.getvalue("Address")

        photo = form['photo']
        photo_filename = None  # Default to None if no file is uploaded

        if photo.filename:
            photo_filename = os.path.basename(photo.filename)
            with open("media/" + photo_filename, "wb") as f:
                f.write(photo.file.read())

        # Secure Parameterized Query
        query = """UPDATE signup 
                   SET name=%s, mobile=%s, mail=%s, Address=%s, photo=%s 
                   WHERE id=%s"""
        values = (name, mobile, Email, Address, photo_filename, mid)

        try:
            cur.execute(query, values)
            con.commit()
            print("""
                <script>
                alert('Updated successfully');
                </script>
            """)
        except Exception as e:
            print(f"""
                <script>
                alert('Update failed: {str(e)}');
                </script>
            """)
print("""
 <br><br><br><footer>
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

