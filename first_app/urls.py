from django.urls import path
from first_app import views
app_name = "pages"
urlpatterns = [
path("about-us/", views.about, name="about"),
    path("shop/", views.shop, name="shop"),
    path("lab-thuc-hanh/", views.labthuchanh, name="lab-thuc-hanh"),
    path("single-product/", views.single_product, name="single_product"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("blog/", views.blog, name="blog"),
    path("single-post/", views.single_post, name="single_post"),
    path("styles/", views.styles, name="styles"),
    path("contact/", views.contact, name="contact"),
    path("thank-you/", views.thank_you, name="thank_you"),
    path("account/", views.account, name="account"),
    path("404/", views.errol, name="errol"),
    path("errol/", views.errol, name="errol"),
    path("account/", views.account, name="account"),
    path("fruits_veges/", views.fruits_veges, name="fruits_veges"),
    path("breads_sweets/", views.breads_sweets, name="breads_sweets"),
    path("beverages/", views.beverages, name="beverages"),
    path("meat_products/", views.meat_products, name="meat_products"),
    path("breads/", views.breads, name="breads"),
    path("dairy_eggs/", views.dairy_eggs, name="dairy_eggs"),
    path("add-to-cart/", views.add_to_cart, name="add_to_cart"),
    # ===== LAB 01 =====
    path("lab1-bai3/", views.lab1_bai3, name="lab1_bai3"),
    path("lab1-bai4/", views.lab1_bai4, name="lab1_bai4"),

    # ===== LAB 02 =====
    path("lab2-bai1/", views.lab2_bai1, name="lab2_bai1"),
    path("lab2-bai2/", views.lab2_bai2, name="lab2_bai2"),

    # ===== LAB 03 =====
    path("lab3-bai1/", views.lab3_bai1, name="lab3_bai1"),
    path("lab3-bai2/", views.lab3_bai2, name="lab3_bai2"),
    path("lab3-bai3/", views.lab3_bai3, name="lab3_bai3"),

    # ===== LAB 04 =====
    path("lab4-bai1/", views.lab4_bai1, name="lab4_bai1"),
    path("lab4-bai2/", views.lab4_bai2, name="lab4_bai2"),
    path("lab4-bai3/", views.lab4_bai3, name="lab4_bai3"),

    # ===== LAB 05 =====
    path("lab5-bai1/", views.lab5_bai1, name="lab5_bai1"),
    path("lab5-bai2/", views.lab5_bai2, name="lab5_bai2"),
    path("lab5-bai3/", views.lab5_bai3, name="lab5_bai3"),

    # ===== LAB 06 =====
    path("lab6-bai1/", views.lab6_bai1, name="lab6_bai1"),
    path("lab6-bai2/", views.lab6_bai2, name="lab6_bai2"),
    path("lab6-bai3/", views.lab6_bai3, name="lab6_bai3"),

    # ===== LAB 07 =====
    path("lab7-bai1/", views.lab7_bai1, name="lab7_bai1"),
    path("lab7-bai2/", views.lab7_bai2, name="lab7_bai2"),

    # ===== LAB 08 =====
    path("lab8-bai1/", views.lab8_bai1, name="lab8_bai1"),
    path("lab8-bai2/", views.lab8_bai2, name="lab8_bai2"),
    path("lab8-bai3/", views.lab8_bai3, name="lab8_bai3"),
]

# Asset routes cho các lab: giúp ảnh/CSS/JS dùng đường dẫn tương đối hoạt động khi render qua Django.
LAB_ASSET_ROUTES = [
    ("lab1-bai3/", "lab1_bai3"),
    ("lab1-bai4/", "lab1_bai4"),
    ("lab2-bai1/", "lab2_bai1"),
    ("lab2-bai2/", "lab2_bai2"),
    ("lab3-bai1/", "lab3_bai1"),
    ("lab3-bai2/", "lab3_bai2"),
    ("lab3-bai3/", "lab3_bai3"),
    ("lab4-bai1/", "lab4_bai1"),
    ("lab4-bai2/", "lab4_bai2"),
    ("lab4-bai3/", "lab4_bai3"),
    ("lab5-bai1/", "lab5_bai1"),
    ("lab5-bai2/", "lab5_bai2"),
    ("lab5-bai3/", "lab5_bai3"),
    ("lab6-bai1/", "lab6_bai1"),
    ("lab6-bai2/", "lab6_bai2"),
    ("lab6-bai3/", "lab6_bai3"),
    ("lab7-bai1/", "lab7_bai1"),
    ("lab7-bai2/", "lab7_bai2"),
    ("lab8-bai1/", "lab8_bai1"),
    ("lab8-bai2/", "lab8_bai2"),
    ("lab8-bai3/", "lab8_bai3"),
]

urlpatterns += [
    path(f"{url_prefix}<path:asset_path>", views.lab_asset, {"lab_key": lab_key})
    for url_prefix, lab_key in LAB_ASSET_ROUTES
]

