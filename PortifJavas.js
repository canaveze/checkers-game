document.addEventListener('DOMContentLoaded', function() {
    // Traduções
    const translations = {
        'pt-BR': {
            'home': 'Início',
            'about': 'Sobre',
            'projects': 'Projetos',
            'volunteer': 'Voluntariados',
            'contact': 'Contato',
            'heroTitle': 'Olá, eu sou a <span>Beatriz Canaveze</span>',
            'heroSubtitle': 'Estudante de Engenharia de Computação',
            'heroText': 'Apaixonada por tecnologia, estou sempre em busca de aprender para inovar.',
            'heroButton': 'Ver meus projetos',
            'aboutTitle': 'Sobre <span>Mim</span>',
            'aboutWho': 'Quem sou eu?',
            'aboutText1': 'Estudante de Engenharia de Computação e apaixonada por tecnologia. Gosto de criar soluções práticas que façam a diferença no dia a dia das pessoas. Tenho experiência com desenvolvimento web, Power Platform, Salesforce e projetos de inovação.',
            'aboutText2': 'Estou sempre em busca de aprender mais e aplicar meus conhecimentos de forma criativa e útil.',
            'skillsTitle': 'Minhas Habilidades',
            'projectsTitle': 'Meus <span>Projetos</span>',
            'volunteerTitle': 'Meus <span>Voluntariados</span>',
            'contactTitle': 'Vamos <span>Conversar</span>',
            'contactText': 'Estou sempre aberta a novas oportunidades e colaborações. Se você tem um projeto em mente ou quer bater um papo, me envie uma mensagem!',
            'formName': 'Nome',
            'formEmail': 'Email',
            'formMessage': 'Mensagem',
            'formButton': 'Enviar Mensagem',
            'timelineTitle': 'Histórico de Carreira'
        },
        'en': {
            'home': 'Home',
            'about': 'About',
            'projects': 'Projects',
            'volunteer': 'Volunteering',
            'contact': 'Contact',
            'heroTitle': 'Hello, I am <span>Beatriz Canaveze</span>',
            'heroSubtitle': 'Computer Engineering Student',
            'heroText': 'Passionate about technology, I am always looking to learn in order to innovate.',
            'heroButton': 'View my projects',
            'aboutTitle': 'About <span>Me</span>',
            'aboutWho': 'Who am I?',
            'aboutText1': 'Computer Engineering student and technology enthusiast. I enjoy creating practical solutions that make a difference in people\'s daily lives. I have experience with web development, Power Platform, Salesforce and innovation projects.',
            'aboutText2': 'I\'m always looking to learn more and apply my knowledge in creative and useful ways.',
            'skillsTitle': 'My Skills',
            'projectsTitle': 'My <span>Projects</span>',
            'volunteerTitle': 'My <span>Volunteering</span>',
            'contactTitle': 'Let\'s <span>Talk</span>',
            'contactText': 'I\'m always open to new opportunities and collaborations. If you have a project in mind or just want to chat, send me a message!',
            'formName': 'Name',
            'formEmail': 'Email',
            'formMessage': 'Message',
            'formButton': 'Send Message',
            'timelineTitle': 'Career History'
        }
    };

    // Função para mudar o idioma
    function changeLanguage(lang) {
        // Atualizar botões de idioma
        document.querySelectorAll('.lang-option').forEach(option => {
            option.classList.remove('active');
            if (option.dataset.lang === lang) {
                option.classList.add('active');
            }
        });

        // Atualizar conteúdo
        const content = translations[lang];
        document.querySelector('nav ul li a[href="#home"]').textContent = content['home'];
        document.querySelector('nav ul li a[href="#about"]').textContent = content['about'];
        document.querySelector('nav ul li a[href="#projects"]').textContent = content['projects'];
        document.querySelector('nav ul li a[href="#volunteer"]').textContent = content['volunteer'];
        document.querySelector('nav ul li a[href="#contact"]').textContent = content['contact'];
        
        document.querySelector('.hero-content h1').innerHTML = content['heroTitle'];
        document.querySelector('.hero-content .typewriter').textContent = content['heroSubtitle'];
        document.querySelector('.hero-content p:not(.typewriter)').textContent = content['heroText'];
        document.querySelector('.hero-content .cta-button').textContent = content['heroButton'];
        
        document.querySelector('.about .section-title').innerHTML = content['aboutTitle'];
        document.querySelector('.about-text h3').textContent = content['aboutWho'];
        document.querySelectorAll('.about-text p')[0].textContent = content['aboutText1'];
        document.querySelectorAll('.about-text p')[1].textContent = content['aboutText2'];
        document.querySelector('.about-text h3:nth-of-type(2)').textContent = content['skillsTitle'];
        
        document.querySelector('.projects .section-title').innerHTML = content['projectsTitle'];
        document.querySelector('.volunteer .section-title').innerHTML = content['volunteerTitle'];
        
        document.querySelector('.contact .section-title').innerHTML = content['contactTitle'];
        document.querySelector('.contact p').textContent = content['contactText'];
        document.querySelector('.contact-form label[for="name"]').textContent = content['formName'];
        document.querySelector('.contact-form label[for="email"]').textContent = content['formEmail'];
        document.querySelector('.contact-form label[for="message"]').textContent = content['formMessage'];
        document.querySelector('.contact-form .submit-btn').textContent = content['formButton'];
        
        document.querySelector('.timeline-header h3').textContent = content['timelineTitle'];
    }

    // Event listeners para os botões de idioma
    document.querySelectorAll('.lang-option').forEach(option => {
        option.addEventListener('click', function(e) {
            e.preventDefault();
            const lang = this.dataset.lang;
            changeLanguage(lang);
        });
    });

    // Menu Mobile
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('nav');

    menuToggle.addEventListener('click', () => {
        nav.classList.toggle('active');
        menuToggle.innerHTML = nav.classList.contains('active') ? 
            '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
    });

    // Fechar menu ao clicar em um link
    document.querySelectorAll('nav ul li a').forEach(link => {
        link.addEventListener('click', () => {
            nav.classList.remove('active');
            menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
        });
    });

    // Cursor Personalizado
    const cursor = document.querySelector('.cursor');
    const cursorFollower = document.querySelector('.cursor-follower');

    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
        
        // Atraso para o cursor seguidor
        setTimeout(() => {
            cursorFollower.style.left = e.clientX + 'px';
            cursorFollower.style.top = e.clientY + 'px';
        }, 100);
    });

    // Efeitos de hover no cursor
    document.querySelectorAll('a, button, .skill, .project-card, .volunteer-card').forEach(element => {
        element.addEventListener('mouseenter', () => {
            cursor.style.transform = 'translate(-50%, -50%) scale(1.5)';
            cursorFollower.style.transform = 'translate(-50%, -50%) scale(0.5)';
            cursorFollower.style.backgroundColor = 'rgba(237, 100, 100, 0.3)';
        });
        
        element.addEventListener('mouseleave', () => {
            cursor.style.transform = 'translate(-50%, -50%) scale(1)';
            cursorFollower.style.transform = 'translate(-50%, -50%) scale(1)';
            cursorFollower.style.backgroundColor = 'transparent';
        });
    });

    // Animação de scroll suave
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Efeito de revelação ao scroll
    const revealElements = document.querySelectorAll('.hero-content, .about-content, .projects-grid, .contact-form');

    function revealOnScroll() {
        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementTop < windowHeight - 100) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    }

    // Configuração inicial para elementos reveláveis
    revealElements.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
    });

    window.addEventListener('scroll', revealOnScroll);
    window.addEventListener('load', revealOnScroll);

    // Atualizar ano no footer
    document.getElementById('year').textContent = new Date().getFullYear();

    // Efeito de máquina de escrever - Versão Corrigida
    const typewriterElements = document.querySelectorAll('.typewriter');
    
    typewriterElements.forEach(element => {
        const text = element.textContent.trim();
        element.textContent = '';
        element.style.borderRight = '3px solid var(--primary)';
        
        let i = 0;
        const typing = setInterval(() => {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
            } else {
                clearInterval(typing);
                element.style.borderRight = 'none';
            }
        }, 100);
    });

    // Efeito de flutuação aleatória para os skills
    const skills = document.querySelectorAll('.skill');
    
    skills.forEach(skill => {
        // Posição inicial aleatória
        skill.style.transform = `rotate(${Math.random() * 10 - 5}deg)`;
        
        skill.addEventListener('mouseenter', () => {
            // Animação aleatória no hover
            const rotation = Math.random() * 20 - 10;
            const translation = Math.random() * 10 - 5;
            skill.style.transform = `rotate(${rotation}deg) translateY(${translation}px)`;
            skill.style.backgroundColor = 'var(--secondary)';
        });
        
        skill.addEventListener('mouseleave', () => {
            // Volta à posição inicial
            skill.style.transform = 'rotate(0deg) translateY(0)';
            skill.style.backgroundColor = 'var(--primary)';
        });
    });

    // Formulário de contato (simulação)
    const contactForm = document.querySelector('.contact-form');

    contactForm.addEventListener('submit', (e) => {
        // e.preventDefault(); ← REMOVA ISSO

        // Isso será substituído pelo envio real do FormSubmit
        // alert('Obrigado pela sua mensagem! Entrarei em contato em breve.');
        // contactForm.reset();
    });

    // Timeline de Empregos
    const jobsToggle = document.querySelector('.jobs-toggle');
    const jobsTimeline = document.querySelector('.jobs-timeline');
    const closeTimeline = document.querySelector('.close-timeline');

    if (jobsToggle && jobsTimeline) {
        jobsToggle.addEventListener('click', () => {
            jobsTimeline.classList.add('active');
            jobsToggle.classList.add('hidden'); // Esconde o botão
            document.body.style.overflow = 'hidden';
        });
        
        closeTimeline.addEventListener('click', () => {
            jobsTimeline.classList.remove('active');
            jobsToggle.classList.remove('hidden'); // Mostra o botão
            document.body.style.overflow = '';
        });
        
        // Fechar ao clicar fora
        document.addEventListener('click', (e) => {
            if (!jobsTimeline.contains(e.target) && e.target !== jobsToggle) {
                jobsTimeline.classList.remove('active');
                jobsToggle.classList.remove('hidden'); // Mostra o botão
                document.body.style.overflow = '';
            }
        });
    }
});