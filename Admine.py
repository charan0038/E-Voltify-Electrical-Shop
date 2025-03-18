#!C:/Users/admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="spma")
cur = con.cursor()
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
    <!-- Bootstrap 5 JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="./style.css">
    <link href="https://cdn.lineicons.com/5.0/lineicons.css" rel="stylesheet">
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
            <main class="content px-3 py-4">
                <div class="container-fluid">
                    <div class="mb-3">
                        <!-- <h3 class="fw-bold fs-4 mb-3"> Admin Dashboard </h3> -->
                        <div class="row">
                            <div class="col-12 col-md-4 ">
                                <div class="card border-0" id="tea">
                                    <div class="card-body py-4">
                                        <h5 class="mb-2 fw-bold">
                                            Total Products
                                        </h5>
                                        <p class="mb-2 fw-bold">
                                            147
                                        </p>
                                        <div class="mb-0">
                                            <span class="badge text-success me-2">
                                                +9.0%
                                            </span>
                                            <span class=" fw-bold">
                                                Since Last Month
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 col-md-4 ">
                                <div class="card  border-0" id="tea">
                                    <div class="card-body py-4">
                                        <h5 class="mb-2 fw-bold">
                                            Total Sales
                                        </h5>
                                        <p class="mb-2 fw-bold">
                                            10245
                                        </p>
                                        <div class="mb-0">
                                            <span class="badge text-success me-2">
                                                +9.0%
                                            </span>
                                            <span class="fw-bold">
                                                Since Last Month
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 col-md-4 ">
                                <div class="card border-0" id="tea">
                                    <div class="card-body py-4">
                                        <h5 class="mb-2 fw-bold">
                                            Memebers Progress
                                        </h5>
                                        <p class="mb-2 fw-bold">
                                            100
                                        </p>
                                        <div class="mb-0">
                                            <span class="badge text-success me-2">
                                                +9.0%
                                            </span>
                                            <span class="fw-bold">
                                                Since Last Month
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                    
                    </div>
                </div>
            </footer>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>
    <script src="scritp.js"></script>
</body>

</html>""")