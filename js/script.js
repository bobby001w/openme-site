// Плавна прокрутка для навігації
document.addEventListener('DOMContentLoaded', function() {
    // Ініціалізація всіх функцій після завантаження DOM
    
    initializeSmoothScroll();
    initializeScrollSpy();
    initializePhoneMask();
    initializeFormHandler();
    initializePhoneNumbers(); // Додано нову функцію
});

// Плавна прокрутка
function initializeSmoothScroll() {
    document.querySelectorAll('nav a, .btn[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            if (this.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    const offsetTop = targetElement.offsetTop - 70;
                    
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
}

// Відстеження активної секції при прокрутці
function initializeScrollSpy() {
    window.addEventListener('scroll', function() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('nav a[href^="#"]');
        
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            const sectionHeight = section.clientHeight;
            
            if (window.pageYOffset >= sectionTop && 
                window.pageYOffset < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href === '#' + current) {
                link.classList.add('active');
            }
        });
    });
}

// Функція для показу сповіщень
function showNotification(message, isError = false) {
    const notification = document.getElementById('notification');
    
    // Створюємо сповіщення, якщо його немає
    if (!notification) {
        createNotificationElement();
    }
    
    const notificationElement = document.getElementById('notification');
    notificationElement.textContent = message;
    
    if (isError) {
        notificationElement.classList.add('error');
    } else {
        notificationElement.classList.remove('error');
    }
    
    notificationElement.classList.add('show');
    
    setTimeout(() => {
        notificationElement.classList.remove('show');
    }, 5000);
}

// Створення елементу сповіщення, якщо його немає
function createNotificationElement() {
    const notification = document.createElement('div');
    notification.id = 'notification';
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        background: #2ecc71;
        color: white;
        border-radius: 5px;
        z-index: 1000;
        transform: translateX(150%);
        transition: transform 0.3s ease;
        max-width: 300px;
    `;
    
    notification.classList.add('show');
    document.body.appendChild(notification);
}

// Маска для телефонного номера
function initializePhoneMask() {
    const phoneInput = document.querySelector('input[name="phone"]');
    
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            
            if (value.length > 0) {
                // Формат: +38 (XXX) XXX-XX-XX
                if (value.length <= 3) {
                    value = '+38 (' + value;
                } else if (value.length <= 6) {
                    value = '+38 (' + value.substring(3, 6) + ') ' + value.substring(6);
                } else if (value.length <= 9) {
                    value = '+38 (' + value.substring(3, 6) + ') ' + value.substring(6, 9) + '-' + value.substring(9);
                } else {
                    value = '+38 (' + value.substring(3, 6) + ') ' + value.substring(6, 9) + '-' + value.substring(9, 11) + '-' + value.substring(11, 13);
                }
            }
            
            e.target.value = value;
        });
    }
}

// Обробка форми
function initializeFormHandler() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const form = e.target;
            const formData = new FormData(form);
            const submitBtn = form.querySelector('button[type="submit"]');
            const loading = document.getElementById('formLoading');
            
            // Перевірка обов'язкових полів
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#e74c3c';
                } else {
                    field.style.borderColor = '';
                }
            });
            
            if (!isValid) {
                showNotification('Будь ласка, заповніть всі обов\'язкові поля', true);
                return;
            }
            
            // Показуємо індикатор завантаження
            if (submitBtn) submitBtn.style.display = 'none';
            if (loading) loading.style.display = 'block';
            
            try {
                const response = await fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Accept': 'application/json'
                    }
                });
                
                if (response.ok) {
                    showNotification('Дякуємо за заявку! Ми зв\'яжемося з вами найближчим часом.');
                    form.reset();
                } else {
                    throw new Error('Помилка при відправці форми');
                }
            } catch (error) {
                console.error('Помилка:', error);
                showNotification('Сталася помилка. Спробуйте ще раз пізніше.', true);
            } finally {
                // Ховаємо індикатор завантаження
                if (submitBtn) submitBtn.style.display = 'block';
                if (loading) loading.style.display = 'none';
            }
        });
    }
}

// НОВА ФУНКЦІЯ: Ініціалізація телефонних номерів
function initializePhoneNumbers() {
    // Робимо номери телефонів клікабельними
    const phoneNumbers = document.querySelectorAll('.phone-number');
    phoneNumbers.forEach(number => {
        number.style.cursor = 'pointer';
        number.addEventListener('click', function() {
            const phone = this.textContent.trim().replace(/\s/g, '');
            window.location.href = `tel:${phone}`;
        });
    });

    // Обробник кнопки "Замовити виклик"
    const callButton = document.querySelector('.call-button');
    if (callButton) {
        callButton.addEventListener('click', function() {
            // Тут можна додати логіку для форми замовлення виклику
            showNotification('Замовлення виклику! Ми вам передзвонимо.');
        });
    }
}

// Додаткова функція для закриття сповіщення при кліку
document.addEventListener('click', function(e) {
    if (e.target.id === 'notification') {
        e.target.classList.remove('show');
    }
});

// Оптимізація продуктивності при скролі
let scrollTimeout;
window.addEventListener('scroll', function() {
    if (scrollTimeout) {
        clearTimeout(scrollTimeout);
    }
    
    scrollTimeout = setTimeout(function() {
        // Код, який виконується після завершення скролу
    }, 100);
});
