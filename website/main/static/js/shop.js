const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.onmouseenter = Swal.stopTimer;
      toast.onmouseleave = Swal.resumeTimer;
    }
  });

// Function to load cart from localStorage
function loadCart() {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    return cart;
}

// Function to save cart to localStorage
function saveCart(cart) {
    localStorage.setItem("cart", JSON.stringify(cart));
}

// Function to calculate the total price
function calculateTotal(cart) {
    return cart.reduce((total, item) => total + item.price, 0);
}

// Function to display the cart
function displayCart() {
    const cart = loadCart();
    const cartItems = document.getElementById("cartItems");
    const totalPrice = document.getElementById("totalPrice");

    cartItems.innerHTML = ""; // Clear the list
    cart.forEach((item, index) => {
        const li = document.createElement("li");
        li.style.marginTop = '20px';
        li.textContent = `${item.name} - $${item.price}`;
        li.innerHTML += ` <button class="btn btn-primary" onclick="removeFromCart(${index})">Remove</button>`;
        cartItems.appendChild(li);
    });

    totalPrice.textContent = calculateTotal(cart);
}

// Function to add an item to the cart
function addToCart(name, price) {
    const cart = loadCart();
    cart.push({ name, price });
    saveCart(cart);
    displayCart();
    Toast.fire({
    icon: "success",
    title: "Product Added"
    });}

// Function to remove an item from the cart
function removeFromCart(index) {
    const cart = loadCart();
    cart.splice(index, 1); // Remove the item at the specified index
    saveCart(cart);
    displayCart();
}

// Function to clear the cart
function clearCart() {
    localStorage.removeItem("cart");
    displayCart();
}

// Initialize the cart on page load
displayCart();
