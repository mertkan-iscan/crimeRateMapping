const box = document.querySelector('.box');
const loginlink = document.querySelector('.login-link');
const register=document.querySelector('.register-link');
const loginpopup=document.querySelector('.Loginpopup');


register.addEventListener('click', ()=> {box.classList.add('active');});

loginlink.addEventListener('click', ()=>{box.classList.remove('active');});



loginpopup.addEventListener('click', ()=>{box.classList.add('active-popup');});

