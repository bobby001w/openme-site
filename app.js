document.addEventListener('DOMContentLoaded',()=>{
  const cfg = window.OpenMeConfig || {};
  const lang = document.documentElement.lang || 'uk';
  const phoneLabel = lang.startsWith('ru') ? 'Позвонить' : 'Подзвонити';
  const telegramLabel = lang.startsWith('ru') ? 'Telegram' : 'Telegram';
  const whatsappLabel = lang.startsWith('ru') ? 'WhatsApp' : 'WhatsApp';

  // Replace phone and messenger links
  document.querySelectorAll('a[href*="{{PHONE}}"]').forEach(a=>a.href = `tel:${cfg.phone}`);
  document.querySelectorAll('a.phone').forEach(a=>{a.href = `tel:${cfg.phone}`; a.textContent = cfg.phoneDisplay});
  document.querySelectorAll('[href="{{TELEGRAM}}"]').forEach(a=>a.href = cfg.telegram);
  document.querySelectorAll('[href="{{WHATSAPP}}"]').forEach(a=>a.href = cfg.whatsapp);
  document.querySelectorAll('[id^="tg-"]').forEach(a=>a.href = cfg.telegram);
  document.querySelectorAll('[id^="wa-"]').forEach(a=>a.href = cfg.whatsapp);

  // Replace price placeholders
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_DOOR\}\}/g, cfg.prices.door);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_CAR\}\}/g, cfg.prices.car);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_SAFE\}\}/g, cfg.prices.safe);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_GARAGE\}\}/g, cfg.prices.garage);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_REPAIR\}\}/g, cfg.prices.repair);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_REPLACE\}\}/g, cfg.prices.replace);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PHONE_DISPLAY\}\}/g, cfg.phoneDisplay);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PHONE\}\}/g, cfg.phone);

  // Mobile quick-action panel
  if(!document.querySelector('.mobile-bar')){
    const mobileBar = document.createElement('div');
    mobileBar.className = 'mobile-bar';
    mobileBar.innerHTML = `
      <a class="btn btn-primary" href="tel:${cfg.phone}">${phoneLabel}</a>
      <a class="btn btn-ghost" href="${cfg.telegram}">${telegramLabel}</a>
      <a class="btn btn-ghost" href="${cfg.whatsapp}">${whatsappLabel}</a>
    `;
    document.body.appendChild(mobileBar);
  }

  // Burger menu toggle
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.main-nav');
  if(burger && nav){
    burger.addEventListener('click',()=>{
      nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', String(nav.classList.contains('open')));
    });
  }
});
