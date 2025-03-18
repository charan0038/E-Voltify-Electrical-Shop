#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os

cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()
form = cgi.FieldStorage()
action = form.getvalue("action")
product_id = form.getvalue("product_id")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admine </title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Boxicons CSS -->
    <link href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
   
    <link rel="stylesheet" href="./style.css">
    <link href="https://cdn.lineicons.com/5.0/lineicons.css" rel="stylesheet">
    <script src="script.js"></script>

</head>


<body>

    <header>
        <a class="navbar-brand float-start" href="#">
            <img src="./media/shop_1-removebg-preview.png" alt="Logo" width="90px" height="50px">
        </a>
        <h1 class="  p-2" align="center "> SRI PALANI MURUGAN AGENCIES</h1>
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
                <form action="#" class="d-none d-sm-inline-block">

                </form>
                <div class="navbar-collapse collapse">
                    <h3 class="fw-bold " id="style"> Admin Dashboard </h3>

                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item dropdown">
                            <a href="#" data-bs-toggle="dropdown" class="nav-icon pe-md-0">
                                <img src="./media/account.png" class="avatar img-fluid" alt="">
                            </a>
                            <div class="dropdown-menu dropdown-menu-end rounded">

                            </div>
                        </li>
                    </ul>
                </div>
            </nav>
</main>
<footer class="footer">
    <div class="container-fluid">
        <div class="row text-body-secondary">
            <div class="col-6 text-start ">
                <a class="text-body-secondary" href=" #">
                    <!-- <strong>CodzSwod</strong> -->
                </a>
            </div>


            
    <script src="scritp.js"></script>
    
            

 <div id="products" class="my-4 p-3">
                <h2>Manage Products</h2>
                <div class="dropdown">
                    <button class="btn btn-success float-end " type="button" data-bs-toggle="modal"
                     data-bs-target="#try" aria-expanded="false">
                      Add New Products
                    </button>
                  
                  </div><br><br>
                
                    
    <div class="modal fade" id="try" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Wires and Cables</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <form  method="POST" enctype="multipart/form-data">
                    <div class="mb-3">
                        <label for="productName" class="form-label">Product Name</label>
                        <input type="text" class="form-control" name="product" id="productName" required>
                    </div>
                    
                    <div class="mb-3">
                        <label for="brandName" class="form-label">Brand Name</label>
                        <input type="text" class="form-control" name="brand" id="productName" required>
                    </div>
            
                    <!-- Category -->
                    <div class="mb-3">
                        <label for="productCategory" class="form-label">Category</label>
                        <select class="form-select" name="category" id="productCategory" required>
                            <option value="">Select Category</option>
                            <option value="wiring">Wiring</option>
                            <option value="fans">fans</option>
                            <option value="LEDBlubs">LED Blubs</option>
                            <option value="Cables">Cables</option>
                            <option value="Socket">Socket</option>
                            <option value="switches">switches</option>
                            <option value="Tools">Tools</option>
                            <option value="Waterheater">Water Heater</option>
                            <option value="Mcb">Mcb</option>
                        </select>
                    </div>
            
                    
                    <div class="mb-3 col-6">
                        <label for="productPrice" class="form-label">Price </label>
                        <input type="number" name="price" class="form-control"  required>
                    </div>

            
                    <!-- Stock Quantity -->
                    <div class="mb-3 col-6">
                        <label for="productStock"  class="form-label">Stock Quantity</label>
                        <input type="number" name="stock" class="form-control"  required>
                    </div>
                    
                      <div class="mb-3 col-6">
                        <label for="productStock"  class="form-label">Warranty</label>
                        <input type="number" name="Warranty" class="form-control"  required>
                    </div>
                    
                    
                        <div class="mb-3 col-6">
                        <label for="productStock"  class="form-label">Color</label>
                        <input type="text" name="Color" class="form-control"  required>
                    </div>
                    
                    <div class="mb-3 col-6">
                        <label for="productStock"  class="form-label">Type</label>
                        <textarea class="form-control" name="Type"  rows="3" required></textarea>
                    </div>
            
                         
                    <!-- Product Image Upload -->
                    <div class="mb-3 col-6">
                        <label for="productImage" 
                          class="form-label">Product Image</label>
                        <input type="file" name="picture" class="form-control"  >
                    </div>
            
                    <!-- Product Description -->
                    <div class="mb-3 col-6">
                        <label for="productDescription" class="form-label">Description</label>
                        <textarea class="form-control" name="Description"  rows="3" required></textarea>
                    </div>
            
                           
                        <div class="modal-footer">
                    <button type="submit" name="submit" class="btn btn-primary">Add Product</button>
                </form>

                </div>
            </div>
        </div>
    </div>
         
    </div>""")
if len(form) != None:
    submit = form.getvalue("submit")
    if submit != None:
        name = form.getvalue("product")
        brand = form.getvalue("brand")
        category = form.getvalue("category")
        Price = form.getvalue("price")
        warranty = form.getvalue("warranty")
        Color = form.getvalue("Color")
        Type1 = form.getvalue("Type")
        stock = form.getvalue("stock")
        Description = form.getvalue("Description")
        photo = form['picture']
        if photo.filename:
            fn = os.path.basename(photo.filename)
            open("media/" + fn, "wb").write(photo.file.read())
            v = """insert into products (product,brand,category,Price,stock,Description,photo,warranty,Color,Type) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % \
                (name, brand, category, Price, stock, Description, fn, warranty, Color, Type1)
            cur.execute(v)
            con.commit()
            print("""
            <script>
            alert("Submit Successfully..!");
            </script>""")


a = """SELECT * FROM products"""
cur.execute(a)
r = cur.fetchall()
print("""
<style>
.content {
            flex-grow: 1;
            padding: 20px;
            
            transition: margin-left 0.3s ease;
            min-height: calc(100vh - 50px); 
            overflow-x: scroll;
        }

</style>
<div class="content">
<table class="table table-bordered  table-hover">
<h1 align ="center">Products</h1><br>
        <tr>
            <th>id</th>
            <th>Product Name</th>
            <th>Brand Name</th>
            <th>Category</th>
            <th>Price </th>
            <th>Stock Quantity</th>
            <th>Product Image</th>
            <th>Description</th>
            <th>Action</th>
        </tr>""")
for i in r:
    print(f"""
    <tr>
        <td>{i[0]}</td>
        <td>{i[1]}</td>
        <td>{i[2]}</td>
        <td>{i[3]}</td>
        <td>{i[4]}</td>
        <td>{i[5]}</td>
        <td><img src="./media/{i[7]}" height="50px" width="60px"></td>
        <td>{i[6]}</td>
        <td><a href="edit.py?proid={i[0]}" class="btn btn-sm btn-success">
                      Edit
                    </a>
            <form method="POST">
    <input type="hidden" name="product_id" value="{i[0]}">
    <button type="submit" name="action" value="remove" class="btn btn-danger btn-sm delete-btn">
        Delete
    </button>
</form></td>
        </tr></div>""")

if action == "remove" and product_id:
    try:
        cur.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
        con.commit()
        print("<script>alert('Product deleted successfully');</script>")
        print("<script>window.location='your_products_page.py';</script>")  # Redirect to refresh the page
    except Exception as e:
        print(f"<script>alert('Error deleting product: {str(e)}');</script>")



print("""
   
    <div class="container">
                <div class="row">
    
    <script>
        document.getElementById("addProductForm").addEventListener("submit", function(event) {
            event.preventDefault();
            alert("Product added successfully!");
        });
    </script>
    


</body>
</html>""")