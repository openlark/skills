# CSS Layout and Interaction Patterns

## Layout Patterns

### Flexbox Centering

```css
.center {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

### Two-Column Layout (Fixed Sidebar, Fluid Main)

```css
.two-column {
  display: flex;
}

.sidebar { width: 250px; flex-shrink: 0; }
.main { flex: 1; }
```

### Sticky Footer

```css
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main { flex: 1; }
footer { flex-shrink: 0; }
```

### Responsive Grid

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}
```

## Common Components

### Navigation Bar

```html
<nav class="nav">
  <a href="#" class="nav__logo">Logo</a>
  <ul class="nav__list">
    <li><a href="#" class="nav__link">Home</a></li>
    <li><a href="#" class="nav__link">Products</a></li>
  </ul>
  <button class="nav__toggle" aria-label="Menu">
    <span></span>
  </button>
</nav>
```

```css
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 2rem;
  background: #fff;
  border-bottom: 1px solid #eee;
}

.nav__list {
  display: flex;
  gap: 2rem;
  list-style: none;
}

.nav__link {
  text-decoration: none;
  color: inherit;
  transition: color 0.2s;
}

.nav__link:hover { color: var(--primary); }

/* Mobile hamburger menu */
.nav__toggle { display: none; }

@media (max-width: 768px) {
  .nav__list { display: none; }
  .nav__toggle { display: block; }
}
```

### Button

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: 500;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn--primary {
  background: var(--primary);
  color: white;
}

.btn--primary:hover {
  background: var(--primary-dark);
  transform: translateY(-1px);
}

.btn--outline {
  background: transparent;
  border: 2px solid var(--primary);
  color: var(--primary);
}

.btn--outline:hover {
  background: var(--primary);
  color: white;
}
```

### Card

```css
.card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  overflow: hidden;
  transition: box-shadow 0.2s, transform 0.2s;
}

.card:hover {
  box-shadow: 0 8px 16px rgba(0,0,0,0.15);
  transform: translateY(-2px);
}
```

### Form Input

```css
.input {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.input:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}
```

## Interaction Effects

### Hover Animation

```css
.link {
  position: relative;
  text-decoration: none;
}

.link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary);
  transition: width 0.3s;
}

.link:hover::after {
  width: 100%;
}
```

### Modal

```html
<div class="modal" id="modal">
  <div class="modal__overlay"></div>
  <div class="modal__content">
    <button class="modal__close">&times;</button>
    <!-- Content -->
  </div>
</div>
```

```css
.modal {
  position: fixed;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s, visibility 0.3s;
}

.modal.active {
  opacity: 1;
  visibility: visible;
}

.modal__overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.5);
}

.modal__content {
  position: relative;
  background: white;
  border-radius: 12px;
  padding: 2rem;
  max-width: 500px;
  transform: scale(0.9);
  transition: transform 0.3s;
}

.modal.active .modal__content {
  transform: scale(1);
}
```

```javascript
const modal = document.getElementById('modal');
const closeBtn = modal.querySelector('.modal__close');

closeBtn.addEventListener('click', () => modal.classList.remove('active'));
modal.querySelector('.modal__overlay').addEventListener('click', () => 
  modal.classList.remove('active')
);
```

### Hamburger Menu

```javascript
const toggle = document.querySelector('.nav__toggle');
const menu = document.querySelector('.nav__list');

toggle.addEventListener('click', () => {
  menu.classList.toggle('active');
  toggle.classList.toggle('active');
});
```

```css
.nav__toggle span,
.nav__toggle span::before,
.nav__toggle span::after {
  display: block;
  width: 24px;
  height: 2px;
  background: #333;
  transition: transform 0.3s;
}

.nav__toggle span {
  position: relative;
}

.nav__toggle span::before,
.nav__toggle span::after {
  content: '';
  position: absolute;
  left: 0;
}

.nav__toggle span::before { top: -8px; }
.nav__toggle span::after { top: 8px; }

.nav__toggle.active span { background: transparent; }
.nav__toggle.active span::before { transform: rotate(45deg); top: 0; }
.nav__toggle.active span::after { transform: rotate(-45deg); top: 0; }
```

## Animations

### Fade In

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.fade-in {
  animation: fadeIn 0.5s ease-out;
}
```

### Slide Up

```css
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.slide-up {
  animation: slideUp 0.5s ease-out;
}
```

### Scroll Trigger

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animate');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.animate-on-scroll').forEach(el => {
  observer.observe(el);
});
```