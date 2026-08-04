# Best Anime Shop - Modern E-Commerce Website

A premium, modern e-commerce website for anime collectibles with a stunning UI/UX design inspired by top-tier stores like Apple and Nike.

## 🎨 Features

### Design & UI/UX
- **Modern, Clean Design**: Apple/Nike-inspired aesthetic with clean spacing and typography
- **Mobile-First Responsive**: Fully responsive layout that works on all devices
- **Glassmorphism Effects**: Beautiful glass-like UI elements with blur effects
- **Gradient Colors**: Stunning gradient backgrounds and text effects
- **Smooth Animations**: Fade, hover, and slide animations throughout
- **Dark Mode Support**: Toggle between light and dark themes with smooth transitions

### Navigation & Layout
- **Sticky Navigation Bar**: Fixed navbar that stays visible while scrolling
- **Smooth Scrolling**: Seamless navigation between sections
- **Mobile Menu**: Hamburger menu for mobile devices
- **Search Bar**: Expandable search functionality

### Interactive Features
- **Shopping Cart**: Fully functional cart with add/remove items
- **Cart Sidebar**: Slide-out cart panel with item management
- **Notifications**: Toast notifications for cart actions
- **Product Cards**: Hover effects, shadows, and animations
- **Add to Cart**: One-click add to cart with visual feedback

### Sections
- **Hero Section**: Stunning hero with animated background elements
- **Promotion Banner**: Eye-catching discount banner with call-to-action
- **Categories**: Grid of product categories with hover effects
- **Featured Products**: Showcase of top products with pricing
- **Footer**: Modern footer with social links and contact info

## 🛠️ Tech Stack

- **HTML5**: Semantic markup
- **Tailwind CSS**: Utility-first CSS framework (via CDN)
- **JavaScript (Vanilla)**: No frameworks, pure JavaScript
- **Font Awesome 6**: Icon library
- **Google Fonts**: Poppins font family

## 📦 File Structure

```
WEB-DESIGN-PROJECT/
├── index.html              # Main homepage (upgraded)
├── Figure.html            # Figures & Statues page
├── Poster.html             # Posters page
├── Blind Box.html          # Blind Box page
├── Clothing.html           # Clothing page
├── Jewelry.html            # Jewelry page
├── Contact.html            # Contact page
├── img/                    # Product images
├── SCSS/                   # SCSS source files
└── dist/                   # Compiled CSS files
```

## 🚀 How to Use

### Local Development

1. **Clone or download the project**
2. **Open `index.html` in a browser** - No build process required!
3. **Or use a local server** (recommended):
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx serve
   ```
4. **Open your browser to** `http://localhost:8000`

### Features Guide

#### Shopping Cart
- Click the cart icon (🛒) in the navbar to open the cart sidebar
- Click "Add to Cart" on any product to add it
- Cart items show quantity and total price
- Click the trash icon to remove items

#### Dark Mode
- Click the moon/sun icon (🌙/☀️) in the navbar
- Preference is saved in localStorage
- Automatically detects system preference on first visit

#### Search
- Click the search icon (🔍) to expand the search bar
- Type to search (functionality ready for backend integration)

#### Mobile Menu
- On mobile devices, click the hamburger menu (☰)
- Navigation links will appear in a dropdown

## 🎯 Customization

### Colors
Edit the Tailwind config in the `<script>` tag in `index.html`:
```javascript
colors: {
    primary: '#FF6B6B',      // Main brand color
    secondary: '#4ECDC4',    // Secondary accent
    accent: '#FFE66D',       // Highlight color
    dark: '#1a1a2e',         // Dark mode background
    darker: '#16213e',       // Darker shade
}
```

### Products
To add more products, copy the product card HTML structure:
```html
<div class="bg-white dark:bg-darker rounded-2xl overflow-hidden card-hover shadow-lg">
    <div class="relative">
        <img src="img/your-image.jpg" alt="Product Name" class="w-full h-64 object-cover">
        <div class="absolute top-4 right-4">
            <span class="bg-primary text-white px-3 py-1 rounded-full text-sm font-semibold">New</span>
        </div>
    </div>
    <div class="p-6">
        <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-2">Product Name</h3>
        <p class="text-gray-600 dark:text-gray-400 text-sm mb-4">Description</p>
        <div class="flex items-center justify-between">
            <span class="text-2xl font-bold text-primary">$99.99</span>
            <button onclick="addToCart('Product Name', 99.99, 'img/your-image.jpg')" class="btn-gradient text-white px-4 py-2 rounded-lg font-semibold">
                <i class="fas fa-cart-plus"></i>
            </button>
        </div>
    </div>
</div>
```

## 🌐 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📱 Responsive Breakpoints

- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## 🔧 Future Enhancements

- Backend integration for real cart persistence
- Product filtering and search functionality
- User authentication
- Payment gateway integration
- Product reviews and ratings
- Wishlist functionality
- Order tracking

## 📄 License

© 2025 Best Anime Shop. All Rights Reserved.

## 👨‍💻 Developer

Website by Daniel

---

**Note**: This is a frontend-only implementation. For a fully functional e-commerce store, you'll need to integrate with a backend system for payment processing, user authentication, and order management.
