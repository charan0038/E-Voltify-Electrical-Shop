#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os

cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()
form = cgi.FieldStorage()
product_id = form.getvalue("proid")


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


""")
select_query = "SELECT * FROM products WHERE product_id=%s"
cur.execute(select_query, (product_id))
r = cur.fetchall()

for property_details in r:
    print(f"""
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-8"> <!-- Adjust width as needed -->
            <form method="POST" enctype="multipart/form-data" class="p-4 shadow rounded bg-white">
                
                <h2 class="text-center mb-4">Edit Product</h2>

                <div class="mb-3">
                    <label for="productName" class="form-label">Product Name</label>
                    <input type="text" class="form-control" name="product" id="productName" value="{property_details[1]}" required>
                </div>

                <div class="mb-3">
                    <label for="brandName" class="form-label">Brand Name</label>
                    <input type="text" class="form-control" name="brand" id="brandName" value="{property_details[2]}" required>
                </div>

                <div class="mb-3">
                    <label for="productCategory" class="form-label">Category</label>
                    <select class="form-select" name="category" id="productCategory" required>
                        <option value="">Select Category</option>
                        <option value="wiring" { 'selected' if property_details[3] == 'wiring' else '' }>Wiring</option>
                        <option value="fans" { 'selected' if property_details[3] == 'fans' else '' }>Fans</option>
                        <option value="LEDBlubs" { 'selected' if property_details[3] == 'LEDBlubs' else '' }>LED Bulbs</option>
                        <option value="Cables" { 'selected' if property_details[3] == 'Cables' else '' }>Cables</option>
                        <option value="Tools" { 'selected' if property_details[3] == 'Tools' else '' }>Tools</option>
                    </select>
                </div>

                <div class="row">
                    <div class="mb-3 col-md-6">
                        <label for="productPrice" class="form-label">Price</label>
                        <input type="number" name="price" class="form-control" value="{property_details[4]}" required>
                    </div>

                    <div class="mb-3 col-md-6">
                        <label for="productStock" class="form-label">Stock Quantity</label>
                        <input type="number" name="stock" class="form-control" value="{property_details[5]}" required>
                    </div>
                </div>

                <div class="row">
                    <div class="mb-3 col-md-6">
                        <label for="productWarranty" class="form-label">Warranty</label>
                        <input type="number" name="Warranty" class="form-control" value="{property_details[8]}" required>
                    </div>

                    <div class="mb-3 col-md-6">
                        <label for="productColor" class="form-label">Color</label>
                        <input type="text" name="Color" class="form-control" value="{property_details[9]}" required>
                    </div>
                </div>

                <div class="mb-3">
                    <label for="productType" class="form-label">Type</label>
                    <textarea class="form-control" name="Type" rows="3" required>{property_details[10]}</textarea>
                </div>

                <div class="mb-3">
                    <label for="productImage" class="form-label">Product Image</label>
                    <input type="file" name="picture" class="form-control">
                </div>

                <div class="mb-3">
                    <label for="productDescription" class="form-label">Description</label>
                    <textarea class="form-control" name="Description" rows="3" required>{property_details[6]}</textarea>
                </div>

                <div class="text-center">
                    <button type="submit" name="submit" class="btn btn-primary w-100">Update Product</button>
                </div>

            </form>
        </div>
    </div>
</div>
""")

    if "submit" in form:
        # Retrieve updated values from the form
        product_name = form.getvalue("product")
        brand_name = form.getvalue("brand")
        category = form.getvalue("category")
        price = form.getvalue("price")
        stock = form.getvalue("stock")
        warranty = form.getvalue("Warranty")
        color = form.getvalue("Color")
        product_type = form.getvalue("Type")
        description = form.getvalue("Description")

        # File upload handling
        file_item = form["picture"]
        if file_item.filename:
            image_path = "uploads/" + file_item.filename  # Set image storage path
            with open(image_path, "wb") as f:
                f.write(file_item.file.read())
            update_query = """
            UPDATE products SET product=%s, brand=%s, category=%s, price=%s, stock=%s, 
            description=%s, warranty=%s, color=%s, type=%s, image_path=%s WHERE product_id=%s
            """
            data = (
            product_name, brand_name, category, price, stock, description, warranty, color, product_type, image_path,
            product_id)
        else:
            update_query = """
            UPDATE products SET product=%s, brand=%s, category=%s, price=%s, stock=%s, 
            description=%s, warranty=%s, color=%s, type=%s WHERE product_id=%s
            """
            data = (
            product_name, brand_name, category, price, stock, description, warranty, color, product_type, product_id)

        # Execute update query
        cur.execute(update_query, data)
        con.commit()

        print("<script>alert('Product updated successfully!');</script>")
