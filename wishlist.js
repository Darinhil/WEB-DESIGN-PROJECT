const WISHLIST_STORAGE_KEY = 'bestAnimeShopWishlist';

function getWishlistItems() {
    try {
        const saved = localStorage.getItem(WISHLIST_STORAGE_KEY);
        return saved ? JSON.parse(saved) : [];
    } catch (error) {
        console.error('Failed to load wishlist', error);
        return [];
    }
}

function saveWishlistItems(items) {
    localStorage.setItem(WISHLIST_STORAGE_KEY, JSON.stringify(items));
}

function updateWishlistCount() {
    const countEl = document.getElementById('wishlist-count');
    if (!countEl) return;
    const items = getWishlistItems();
    const count = items.length;
    countEl.textContent = count;
    countEl.style.display = count > 0 ? 'flex' : 'none';
}

function isInWishlist(name) {
    return getWishlistItems().some(item => item.name === name);
}

function addToWishlist(name, price, image) {
    const items = getWishlistItems();
    if (!items.some(item => item.name === name)) {
        items.push({ name, price, image });
        saveWishlistItems(items);
        updateWishlistCount();
        updateWishlistButtons();
        showWishlistNotification(`${name} added to wishlist!`, 'success');
    }
}

function removeFromWishlist(name) {
    const items = getWishlistItems().filter(item => item.name !== name);
    saveWishlistItems(items);
    updateWishlistCount();
    updateWishlistButtons();
    showWishlistNotification(`${name} removed from wishlist`, 'info');
}

function toggleWishlist(name, price, image) {
    if (isInWishlist(name)) {
        removeFromWishlist(name);
    } else {
        addToWishlist(name, price, image);
    }
}

function updateWishlistButtons() {
    document.querySelectorAll('[data-wishlist-name]').forEach(button => {
        const itemName = button.dataset.wishlistName;
        if (isInWishlist(itemName)) {
            button.classList.add('text-red-500');
            button.classList.remove('text-gray-600');
            button.innerHTML = '<i class="fas fa-heart"></i>';
            button.title = 'Remove from wishlist';
        } else {
            button.classList.remove('text-red-500');
            button.classList.add('text-gray-600');
            button.innerHTML = '<i class="far fa-heart"></i>';
            button.title = 'Add to wishlist';
        }
    });
}

function showWishlistNotification(message, type = 'success') {
    if (typeof showNotification === 'function') {
        showNotification(message, type);
        return;
    }

    const container = document.getElementById('notification-container');
    if (!container) {
        return;
    }

    const notification = document.createElement('div');
    const bgColor = type === 'success' ? 'bg-green-500' : type === 'error' ? 'bg-red-500' : 'bg-blue-500';
    notification.className = `notification ${bgColor} text-white px-6 py-3 rounded-lg shadow-lg flex items-center space-x-2`;
    notification.innerHTML = `<i class="fas ${type === 'success' ? 'fa-check-circle' : type === 'error' ? 'fa-exclamation-circle' : 'fa-info-circle'}"></i><span>${message}</span>`;
    container.appendChild(notification);

    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateX(100%)';
        notification.style.transition = 'all 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

function injectWishlistButtons() {
    document.querySelectorAll('button[onclick^="addToCart"]').forEach(addBtn => {
        const card = addBtn.closest('.card-hover, .product-card') || addBtn.parentElement;
        if (!card || card.querySelector('[data-wishlist-name]')) {
            return;
        }

        const titleEl = card.querySelector('h3, h4, .product-name');
        const name = titleEl?.textContent?.trim();
        if (!name) {
            return;
        }

        const priceEl = Array.from(card.querySelectorAll('span, p')).find(el => /^\s*\$\d/.test(el.textContent));
        const price = priceEl ? parseFloat(priceEl.textContent.replace(/[^0-9.]/g, '')) : 0;
        const image = card.querySelector('img')?.getAttribute('src') || '';

        const wishlistButton = document.createElement('button');
        wishlistButton.type = 'button';
        wishlistButton.dataset.wishlistName = name;
        wishlistButton.className = 'text-gray-600 hover:text-red-500 transition-colors';
        wishlistButton.title = 'Add to wishlist';
        wishlistButton.innerHTML = '<i class="far fa-heart"></i>';
        wishlistButton.addEventListener('click', event => {
            event.stopPropagation();
            toggleWishlist(name, price, image);
        });

        const wrapper = document.createElement('div');
        wrapper.className = 'flex items-center gap-2';
        addBtn.parentElement.insertBefore(wrapper, addBtn);
        wrapper.appendChild(wishlistButton);
        wrapper.appendChild(addBtn);
    });
}

function renderWishlistPage() {
    const target = document.getElementById('wishlist-items');
    if (!target) return;

    const items = getWishlistItems();
    target.innerHTML = '';

    if (!items.length) {
        target.innerHTML = '<p class="text-gray-600 dark:text-gray-300">Your wishlist is empty. Browse products and add your favorites.</p>';
        return;
    }

    items.forEach(item => {
        const card = document.createElement('div');
        card.className = 'bg-white dark:bg-darker rounded-2xl overflow-hidden shadow-lg';
        card.innerHTML = `
            <div class="relative">
                <img src="${item.image}" alt="${item.name}" class="w-full h-64 object-cover">
            </div>
            <div class="p-6">
                <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-2">${item.name}</h3>
                <div class="flex items-center justify-between">
                    <span class="text-2xl font-bold text-primary">$${Number(item.price).toFixed(2)}</span>
                    <button onclick="removeFromWishlist('${item.name.replace(/'/g, "\\'")}')" class="bg-red-500 text-white px-4 py-2 rounded-lg font-semibold hover:bg-red-600 transition-colors">
                        Remove
                    </button>
                </div>
            </div>
        `;
        target.appendChild(card);
    });
}

function initializeWishlist() {
    updateWishlistCount();
    updateWishlistButtons();
    renderWishlistPage();
    injectWishlistButtons();
}

document.addEventListener('DOMContentLoaded', initializeWishlist);
