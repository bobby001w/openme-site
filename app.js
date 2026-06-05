document.addEventListener('DOMContentLoaded',()=>{
  const cfg = window.OpenMeConfig || {};
  // Replace phone and links
  document.querySelectorAll('a[href*="{{PHONE}}"]').forEach(a=>a.href = `tel:${cfg.phone}`);
  document.querySelectorAll('a.phone').forEach(a=>{a.href=`tel:${cfg.phone}`; a.textContent = cfg.phoneDisplay});
  document.querySelectorAll('[href="{{TELEGRAM}}"]').forEach(a=>a.href = cfg.telegram);
  document.querySelectorAll('[href="{{WHATSAPP}}"]').forEach(a=>a.href = cfg.whatsapp);
  document.querySelectorAll('[id^="tg-"]').forEach(a=>a.href = cfg.telegram);
  document.querySelectorAll('[id^="wa-"]').forEach(a=>a.href = cfg.whatsapp);
  // Replace price placeholders
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_DOOR\}\}/g,cfg.prices.door);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_CAR\}\}/g,cfg.prices.car);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_SAFE\}\}/g,cfg.prices.safe);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_GARAGE\}\}/g,cfg.prices.garage);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_REPAIR\}\}/g,cfg.prices.repair);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PRICE_REPLACE\}\}/g,cfg.prices.replace);
  // Phone placeholders
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PHONE_DISPLAY\}\}/g,cfg.phoneDisplay);
  document.body.innerHTML = document.body.innerHTML.replace(/\{\{PHONE\}\}/g,cfg.phone);

  // Burger menu
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.main-nav');
  if(burger && nav){
    burger.addEventListener('click',()=>{nav.classList.toggle('open')});
  }
});
