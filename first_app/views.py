from django.shortcuts import render, get_object_or_404
from first_app.models import Category, Fruit


SHOP_PRODUCTS = [
    {"name": "Whole Wheat Sandwich Bread", "category": "Bakery", "price": "18.00", "old_price": "24.00", "image": "images/product-thumb-1.png", "rating": "222"},
    {"name": "Whole Grain Oatmeal", "category": "Breakfast", "price": "50.00", "old_price": "54.00", "image": "images/product-thumb-2.png", "rating": "41"},
    {"name": "Sharp Cheddar Cheese Block", "category": "Dairy", "price": "12.00", "old_price": "16.00", "image": "images/product-thumb-3.png", "rating": "98"},
    {"name": "Organic Baby Spinach", "category": "Vegetables", "price": "8.00", "old_price": "10.00", "image": "images/product-thumb-4.png", "rating": "134"},
    {"name": "Fresh Banana Bunch", "category": "Fruits", "price": "4.00", "old_price": "6.00", "image": "images/product-thumb-5.png", "rating": "76"},
    {"name": "Avocado Hass Organic", "category": "Fruits", "price": "15.00", "old_price": "18.00", "image": "images/product-thumb-6.png", "rating": "156"},
    {"name": "Greek Style Yogurt", "category": "Dairy", "price": "7.00", "old_price": "9.00", "image": "images/product-thumb-7.png", "rating": "62"},
    {"name": "Cold Pressed Orange Juice", "category": "Beverages", "price": "10.00", "old_price": "13.00", "image": "images/product-thumb-8.png", "rating": "86"},
    {"name": "Roasted Almond Butter", "category": "Pantry", "price": "21.00", "old_price": "28.00", "image": "images/product-thumb-9.png", "rating": "117"},
    {"name": "Organic Cherry Tomatoes", "category": "Vegetables", "price": "6.00", "old_price": "8.00", "image": "images/product-thumb-10.png", "rating": "53"},
]

BLOG_POSTS = [
    {"title": "How to keep groceries fresh for longer", "date": "22 Aug 2026", "image": "images/post-thumbnail-1.jpg", "excerpt": "Simple storage habits that help fruit, vegetables, bread, and dairy stay fresh without turning your fridge into a tiny guilt museum."},
    {"title": "Five organic pantry staples worth buying", "date": "18 Aug 2026", "image": "images/post-thumbnail-2.jpg", "excerpt": "A practical list of staples that save cooking time and make weeknight meals feel less like a punishment from the universe."},
    {"title": "Quick breakfasts for busy mornings", "date": "12 Aug 2026", "image": "images/post-thumbnail-3.jpg", "excerpt": "Healthy breakfast ideas using oats, yogurt, nuts, fresh fruit, and other things humans claim they will prep on Sunday."},
]

CART_ITEMS = [
    {"name": "Whole Wheat Sandwich Bread", "price": 18, "quantity": 2, "image": "images/product-thumb-1.png"},
    {"name": "Organic Baby Spinach", "price": 8, "quantity": 1, "image": "images/product-thumb-4.png"},
    {"name": "Cold Pressed Orange Juice", "price": 10, "quantity": 3, "image": "images/product-thumb-8.png"},
]


CATEGORY_PAGES = {
    "fruits_veges": {
        "title": "Fruits & Veges",
        "subtitle": "Fresh fruit and vegetables selected for daily meals.",
        "image": "images/category-thumb-1.jpg",
        "hero_image": "images/banner-ad-1.jpg",
        "icon": "fresh",
        "products": [
            {"name": "Organic Apples", "price": "6.00", "old_price": "8.00", "image": "images/category-thumb-1.jpg", "badge": "Fresh"},
            {"name": "Baby Spinach", "price": "8.00", "old_price": "10.00", "image": "images/product-thumb-4.png", "badge": "Organic"},
            {"name": "Fresh Banana Bunch", "price": "4.00", "old_price": "6.00", "image": "images/product-thumb-5.png", "badge": "Best seller"},
            {"name": "Avocado Hass", "price": "15.00", "old_price": "18.00", "image": "images/product-thumb-6.png", "badge": "Ripe"},
            {"name": "Cherry Tomatoes", "price": "6.00", "old_price": "8.00", "image": "images/product-thumb-10.png", "badge": "Local"},
        ],
    },
    "breads_sweets": {
        "title": "Breads & Sweets",
        "subtitle": "Soft bread, pastries, and sweet bakery picks for very serious carb decisions.",
        "image": "images/category-thumb-2.jpg",
        "hero_image": "images/banner-ad-2.jpg",
        "icon": "bakery",
        "products": [
            {"name": "Cinnamon Rolls", "price": "12.00", "old_price": "16.00", "image": "images/category-thumb-2.jpg", "badge": "Sweet"},
            {"name": "Whole Wheat Bread", "price": "18.00", "old_price": "24.00", "image": "images/product-thumb-1.png", "badge": "Popular"},
            {"name": "Butter Croissant", "price": "9.00", "old_price": "11.00", "image": "images/product-thumb-11.png", "badge": "Bakery"},
            {"name": "Honey Muffins", "price": "10.00", "old_price": "14.00", "image": "images/product-thumb-12.png", "badge": "New"},
            {"name": "Chocolate Buns", "price": "13.00", "old_price": "17.00", "image": "images/product-thumb-13.png", "badge": "Hot"},
        ],
    },
    "beverages": {
        "title": "Beverages",
        "subtitle": "Juices, tea, milk drinks, and other liquids humans insist on branding as lifestyle.",
        "image": "images/category-thumb-4.jpg",
        "hero_image": "images/banner-newsletter.jpg",
        "icon": "beverages",
        "products": [
            {"name": "Cold Pressed Orange Juice", "price": "10.00", "old_price": "13.00", "image": "images/product-thumb-8.png", "badge": "Fresh"},
            {"name": "Organic Grape Juice", "price": "9.00", "old_price": "12.00", "image": "images/category-thumb-3.jpg", "badge": "Natural"},
            {"name": "Green Tea Bottle", "price": "5.00", "old_price": "7.00", "image": "images/product-thumb-14.png", "badge": "Cool"},
            {"name": "Almond Milk", "price": "8.00", "old_price": "11.00", "image": "images/product-thumb-15.png", "badge": "Dairy free"},
            {"name": "Sparkling Water", "price": "4.00", "old_price": "6.00", "image": "images/product-thumb-16.png", "badge": "Light"},
        ],
    },
    "meat_products": {
        "title": "Meat Products",
        "subtitle": "Fresh meat products packed for easy cooking and fewer dinner excuses.",
        "image": "images/category-thumb-5.jpg",
        "hero_image": "images/banner-ad-3.jpg",
        "icon": "meat",
        "products": [
            {"name": "Fresh Beef Steak", "price": "25.00", "old_price": "32.00", "image": "images/category-thumb-5.jpg", "badge": "Premium"},
            {"name": "Chicken Breast", "price": "18.00", "old_price": "23.00", "image": "images/product-thumb-17.png", "badge": "Lean"},
            {"name": "Pork Tenderloin", "price": "20.00", "old_price": "26.00", "image": "images/product-thumb-18.png", "badge": "Fresh"},
            {"name": "Turkey Slices", "price": "14.00", "old_price": "19.00", "image": "images/product-thumb-19.png", "badge": "Ready"},
            {"name": "Organic Sausage", "price": "16.00", "old_price": "21.00", "image": "images/product-thumb-20.png", "badge": "Grill"},
        ],
    },
    "breads": {
        "title": "Breads",
        "subtitle": "Everyday bread, rolls, and loaves for breakfast, sandwiches, and emergency toast.",
        "image": "images/category-thumb-6.jpg",
        "hero_image": "images/banner-ad-2.jpg",
        "icon": "bakery",
        "products": [
            {"name": "Sourdough Loaf", "price": "11.00", "old_price": "15.00", "image": "images/category-thumb-8.jpg", "badge": "Bakery"},
            {"name": "Whole Wheat Sandwich Bread", "price": "18.00", "old_price": "24.00", "image": "images/product-thumb-1.png", "badge": "Popular"},
            {"name": "Multigrain Bread", "price": "12.00", "old_price": "16.00", "image": "images/product-thumb-21.png", "badge": "Healthy"},
            {"name": "Burger Buns", "price": "7.00", "old_price": "10.00", "image": "images/product-thumb-22.png", "badge": "Soft"},
            {"name": "Garlic Bread", "price": "9.00", "old_price": "13.00", "image": "images/product-thumb-23.png", "badge": "Hot"},
        ],
    },
    "dairy_eggs": {
        "title": "Dairy & Eggs",
        "subtitle": "Eggs, milk, cheese, and dairy essentials that prevent breakfast from becoming a tragedy.",
        "image": "images/category-thumb-7.jpg",
        "hero_image": "images/banner-ad-1.jpg",
        "icon": "dairy",
        "products": [
            {"name": "Organic Eggs", "price": "7.00", "old_price": "10.00", "image": "images/category-thumb-7.jpg", "badge": "Farm"},
            {"name": "Greek Style Yogurt", "price": "7.00", "old_price": "9.00", "image": "images/product-thumb-7.png", "badge": "Creamy"},
            {"name": "Sharp Cheddar Cheese", "price": "12.00", "old_price": "16.00", "image": "images/product-thumb-3.png", "badge": "Dairy"},
            {"name": "Fresh Milk", "price": "5.00", "old_price": "7.00", "image": "images/product-thumb-24.png", "badge": "Fresh"},
            {"name": "Salted Butter", "price": "6.00", "old_price": "8.00", "image": "images/product-thumb-25.png", "badge": "Classic"},
        ],
    },
}

CATEGORY_NAV = [
    {"title": "Fruits & Veges", "url_name": "pages:fruits_veges", "image": "images/category-thumb-1.jpg"},
    {"title": "Breads & Sweets", "url_name": "pages:breads_sweets", "image": "images/category-thumb-2.jpg"},
    {"title": "Beverages", "url_name": "pages:beverages", "image": "images/category-thumb-4.jpg"},
    {"title": "Meat Products", "url_name": "pages:meat_products", "image": "images/category-thumb-5.jpg"},
    {"title": "Breads", "url_name": "pages:breads", "image": "images/category-thumb-6.jpg"},
    {"title": "Dairy & Eggs", "url_name": "pages:dairy_eggs", "image": "images/category-thumb-7.jpg"},
]


def _cart_total():
    return sum(item["price"] * item["quantity"] for item in CART_ITEMS)


def index(request):
    return render(request, "index.html", {
        "products": SHOP_PRODUCTS,
        "category_nav": CATEGORY_NAV,
    })


def about(request):
    return render(request, "pages/about.html", {"title": "About Us"})

from django.shortcuts import redirect

def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        name = request.POST.get("name")
        price = float(request.POST.get("price", 0))
        image = request.POST.get("image")
        quantity = int(request.POST.get("quantity", 1))

        cart = request.session.get("cart", {})

        if product_id in cart:
            cart[product_id]["quantity"] += quantity
        else:
            cart[product_id] = {
                "name": name,
                "price": price,
                "image": image,
                "quantity": quantity,
            }

        request.session["cart"] = cart
        request.session.modified = True

    return redirect("pages:cart")
def shop(request):
    accFruit = Fruit.objects.all()
    return render(request, "pages/shop.html", {
        "title": "Shop",
        "products": SHOP_PRODUCTS,
        "accFruit": accFruit,
    })


def single_product(request):
    fruit = Fruit.objects.first()
    related_fruits = Fruit.objects.exclude(pk=fruit.pk)[:4] if fruit else []
    return render(request, "pages/single_product.html", {
        "title": "Single Product",
        "product": SHOP_PRODUCTS[0],
        "fruit": fruit,
        "accFruit": related_fruits,
        "products": SHOP_PRODUCTS[1:5],
    })


def cart(request):
    cart = request.session.get("cart", {})

    cart_items = []
    subtotal = 0

    for product_id, item in cart.items():
        line_total = item["price"] * item["quantity"]
        subtotal += line_total

        cart_items.append({
            "id": product_id,
            "name": item["name"],
            "price": item["price"],
            "image": item["image"],
            "quantity": item["quantity"],
            "line_total": line_total,
        })

    shipping = 5 if subtotal > 0 else 0
    total = subtotal + shipping

    return render(request, "pages/cart.html", {
        "title": "Cart",
        "cart_items": cart_items,
        "subtotal": subtotal,
        "shipping": shipping,
        "total": total,
    })


def checkout(request):
    subtotal = _cart_total()
    return render(request, "pages/checkout.html", {
        "title": "Checkout",
        "cart_items": CART_ITEMS,
        "subtotal": subtotal,
        "shipping": 5,
        "total": subtotal + 5,
    })


def blog(request):
    return render(request, "pages/blog.html", {"title": "Blog", "posts": BLOG_POSTS})


def single_post(request):
    return render(request, "pages/single_post.html", {"title": "Single Post", "post": BLOG_POSTS[0], "posts": BLOG_POSTS[1:]})


def styles(request):
    return render(request, "pages/styles.html", {"title": "Styles"})


def contact(request):
    return render(request, "pages/contact.html", {"title": "Contact"})


def thank_you(request):
    subtotal = _cart_total()
    return render(request, "pages/thank_you.html", {"title": "Thank You", "order_total": subtotal + 5})


def account(request):
    return render(request, "pages/account.html", {"title": "My Account"})


def errol(request, exception=None):
    return render(request, "pages/404.html", {"title": "404 Error"}, status=404)



def _category_context(slug):
    category_info = CATEGORY_PAGES[slug]
    return {
        "title": category_info["title"],
        "category_info": category_info,
        "category_products": category_info["products"],
        "category_nav": CATEGORY_NAV,
    }


def fruits_veges(request):
    return render(request, "fruits_veges.html", _category_context("fruits_veges"))


def breads_sweets(request):
    return render(request, "breads_sweets.html", _category_context("breads_sweets"))


def beverages(request):
    return render(request, "beverages.html", _category_context("beverages"))


def meat_products(request):
    return render(request, "meat_products.html", _category_context("meat_products"))


def breads(request):
    return render(request, "breads.html", _category_context("breads"))


def dairy_eggs(request):
    return render(request, "dairy_eggs.html", _category_context("dairy_eggs"))


# ===== Serve lab assets rendered from templates =====
# Các file lab được đặt trong templates để render HTML, nhưng ảnh/CSS/JS lại
# đang dùng đường dẫn tương đối như "images/...", "css/...", "js/...".
# Khi chạy qua Django, trình duyệt sẽ gọi /pages/labX-baiY/images/... nên cần
# view này phục vụ asset đúng theo thư mục lab tương ứng.
from pathlib import Path
import mimetypes

from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse


LAB_ASSET_BASES = {
    "lab1_bai3": "Lab01/Vi_du",
    "lab1_bai4": "Lab01/Vi_du",
    "lab2_bai1": "Lab02",
    "lab2_bai2": "Lab02",
    "lab3_bai1": "Lab03/Lab03/Vi_du_Lab01",
    "lab3_bai2": "Lab03/Lab03/Vi_du_Lab01",
    "lab3_bai3": "Lab03/Lab03/Vi_du",
    "lab4_bai1": "Lab04/Lab04/Vi_du",
    "lab4_bai2": "Lab04/Lab04/Vi_du",
    "lab4_bai3": "Lab04/Lab04/Vi_du",
    "lab5_bai1": "Lab05/Lab05/Vi_du",
    "lab5_bai2": "Lab05/Lab05/Bai_2",
    "lab5_bai3": "Lab05/Lab05/Bai_2",
    "lab6_bai1": "Lab06/Lab06",
    "lab6_bai2": "Lab06/Lab06/Bai_2_Minh_hoa_layout",
    "lab6_bai3": "Lab06/Lab06/Bai_2_Minh_hoa_layout",
    "lab7_bai1": "Lab07/Vi_du",
    "lab7_bai2": "Lab07/demo_bai_2",
    "lab8_bai1": "Lab08",
    "lab8_bai2": "Lab08",
    "lab8_bai3": "Lab08",
}

LAB_ASSET_FALLBACK_BASES = [
    "Lab01/Vi_du",
    "Lab02/Vi_du_Lab01",
    "Lab03/Lab03/Vi_du",
    "Lab03/Lab03/Vi_du_Lab01",
    "Lab04/Lab04/Vi_du",
    "Lab05/Lab05/Vi_du",
    "Lab05/Lab05/Bai_2",
    "Lab06/Lab06",
    "Lab06/Lab06/Bai_2_Minh_hoa_layout",
    "Lab06/Lab06/Vi_du",
    "Lab07/Vi_du",
    "Lab07/demo_bai_2",
    "Lab08",
    "Lab08/Vi_du_1",
    "Lab08/Vi_du_2",
]

LAB_ASSET_ALIASES = {
    # Một số file HTML mẫu dùng đường dẫn demo không có thật. Ánh xạ về file có sẵn.
    "path/to/fork-awesome/css/fork-awesome.min.css": [
        "css/font-awesome.min.css",
    ],
    # Lab04 có trang gọi main.css, trong khi file thật nằm trong styles/main.css.
    "main.css": [
        "styles/main.css",
    ],
}


def _case_insensitive_child(parent: Path, child_name: str):
    if not parent.is_dir():
        return None
    child_name_lower = child_name.lower()
    for item in parent.iterdir():
        if item.name.lower() == child_name_lower:
            return item
    return None


def _resolve_lab_asset(base_dir: Path, relative_path: str):
    # Chặn path traversal để tránh đọc file ngoài thư mục lab được phép.
    cleaned = relative_path.replace("\\", "/").lstrip("/")
    parts = [part for part in cleaned.split("/") if part not in ("", ".")]
    if any(part == ".." for part in parts):
        return None

    candidate = base_dir.joinpath(*parts)
    try:
        candidate.resolve().relative_to(base_dir.resolve())
    except ValueError:
        return None
    if candidate.is_file():
        return candidate

    # Windows không phân biệt hoa/thường, Linux thì có. Sinh viên thì thường gặp cả hai.
    current = base_dir
    for part in parts:
        current = _case_insensitive_child(current, part)
        if current is None:
            break
    if current is not None and current.is_file():
        return current

    return None


def lab_asset(request, lab_key, asset_path):
    templates_root = Path(settings.BASE_DIR) / "templates"
    base_names = []
    base_name = LAB_ASSET_BASES.get(lab_key)
    if base_name:
        base_names.append(base_name)
    base_names.extend(name for name in LAB_ASSET_FALLBACK_BASES if name not in base_names)

    normalized_asset_path = asset_path.replace("\\", "/").lstrip("/")
    paths_to_try = [asset_path]
    paths_to_try.extend(LAB_ASSET_ALIASES.get(normalized_asset_path, []))

    # CSS font-awesome được route qua path demo nên font sẽ bị gọi theo
    # path/to/fork-awesome/fonts/...; ánh xạ về fonts/... thật.
    if normalized_asset_path.startswith("path/to/fork-awesome/fonts/"):
        paths_to_try.append("fonts/" + normalized_asset_path.rsplit("/", 1)[-1])

    # Một vài CSS viết url(images/...) dù file CSS nằm trong thư mục styles/ hoặc css/.
    # Trình duyệt vì thế gọi styles/images/... hoặc css/images/...; thử bỏ tiền tố đó.
    if normalized_asset_path.startswith("styles/images/"):
        paths_to_try.append(normalized_asset_path.replace("styles/images/", "images/", 1))
    if normalized_asset_path.startswith("css/images/"):
        paths_to_try.append(normalized_asset_path.replace("css/images/", "images/", 1))
    if normalized_asset_path.startswith("css/fonts/"):
        paths_to_try.append(normalized_asset_path.replace("css/fonts/", "fonts/", 1))

    for relative_path in paths_to_try:
        for base_name in base_names:
            found = _resolve_lab_asset(templates_root / base_name, relative_path)
            if found:
                content_type, _ = mimetypes.guess_type(found.name)
                return FileResponse(open(found, "rb"), content_type=content_type or "application/octet-stream")

    # Nếu chỉ thiếu CSS biểu tượng demo, trả file rỗng để trang không báo lỗi 404 vô ích.
    if normalized_asset_path.endswith("fork-awesome.min.css"):
        return HttpResponse("", content_type="text/css")

    # Một số thư viện CSS có tham chiếu icon phụ nhưng gói nộp bài không kèm file.
    # Trả ảnh trong suốt để layout không vỡ khi thiếu các icon phụ này.
    if normalized_asset_path.lower().endswith((".png", ".gif")):
        transparent_png = (
            b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"
            b"\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
            b"\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4"
            b"\x00\x00\x00\x00IEND\xaeB`\x82"
        )
        return HttpResponse(transparent_png, content_type="image/png")

    raise Http404("Không tìm thấy tài nguyên lab")

def labthuchanh(request):
    return render(request, "lab-thuc-hanh.html")
def lab1_bai3(request):
    return render(request, "Lab01/Vi_du/lab1_bai3.html")


def lab1_bai4(request):
    return render(request, "Lab01/Vi_du/lab1_bai4.html")


# ===== LAB 02 =====
def lab2_bai1(request):
    return render(request, "Lab02/lab02_bai2.html")


def lab2_bai2(request):
    return render(request, "Lab02/lab02_khung_table.html")


# ===== LAB 03 =====
def lab3_bai1(request):
    return render(request, "Lab03/Lab03/Vi_du_Lab01/lab03_bai1.html")


def lab3_bai2(request):
    return render(request, "Lab03/Lab03/Vi_du_Lab01/lab03_bai2.html")


def lab3_bai3(request):
    return render(request, "Lab03/Lab03/Vi_du/index.html")


# ===== LAB 04 =====
def lab4_bai1(request):
    return render(request, "Lab04/Lab04/Vi_du/lab04_bai1.html")


def lab4_bai2(request):
    return render(request, "Lab04/Lab04/Vi_du/lab04_bai2.html")


def lab4_bai3(request):
    return render(request, "Lab04/Lab04/Vi_du/lab04_bai3.html")


# ===== LAB 05 =====
def lab5_bai1(request):
    return render(request, "Lab05/Lab05/Vi_du/index.html")


def lab5_bai2(request):
    return render(request, "Lab05/Lab05/Bai_2/index.html")


def lab5_bai3(request):
    return render(request, "Lab05/Lab05/Bai_2/lab05_menu.html")


# ===== LAB 06 =====
def lab6_bai1(request):
    return render(request, "Lab06/Lab06/lab06_menu_responsive.html")


def lab6_bai2(request):
    return render(request, "Lab06/Lab06/Bai_2_Minh_hoa_layout/lab06_bai2.html")


def lab6_bai3(request):
    return render(request, "Lab06/Lab06/Bai_2_Minh_hoa_layout/lab06_bai3.html")


# ===== LAB 07 =====
def lab7_bai1(request):
    return render(request, "Lab07/Vi_du/index.html")


def lab7_bai2(request):
    return render(request, "Lab07/demo_bai_2/index.html")


# ===== LAB 08 =====
def lab8_bai1(request):
    return render(request, "Lab08/lab08_slider.html")


def lab8_bai2(request):
    return render(request, "Lab08/lab08_slider_auto.html")


def lab8_bai3(request):
    return render(request, "Lab08/lab08_json.html")
def category(request):
    accCategory = Category.objects.all()
    dic = {
        "title": "Category",
        "accCategory": accCategory,
    }
    return render(request, "category.html", dic)


def fruit(request):
    accFruit = Fruit.objects.all()
    dic = {
        "title": "Fruit",
        "accFruit": accFruit,
    }
    return render(request, "fruit.html", dic)


def fruit_detail(request, pk):
    accFruit = Fruit.objects.exclude(pk=pk)[:4]
    fruit = get_object_or_404(Fruit, pk=pk)
    dic = {
        "title": "Fruit",
        "fruit": fruit,
        "accFruit": accFruit,
    }
    return render(request, "fruit_detail.html", dic)
