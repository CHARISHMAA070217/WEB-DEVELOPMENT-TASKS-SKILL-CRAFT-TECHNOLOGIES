                                                  TASK-1
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Responsive Landing Page</title>
  <style>
    /* Reset styles */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Segoe UI', sans-serif;
      line-height: 1.6;
    }

    /* Fixed navigation */
    nav {
      position: fixed;
      top: 0;
      width: 100%;
      background: transparent;
      color: white;
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.3s ease;
      z-index: 1000;
    }

    nav.scrolled {
      background: #ffffff;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      color: #333;
    }

    nav .logo {
      font-size: 1.5rem;
      font-weight: bold;
    }

    nav ul {
      list-style: none;
      display: flex;
      gap: 2rem;
    }

    nav ul li a {
      text-decoration: none;
      color: inherit;
      font-weight: 500;
      transition: color 0.2s ease;
    }

    nav ul li a:hover {
      color: #007BFF;
    }

    /* Responsive */
    @media (max-width: 768px) {
      nav ul {
        display: none;
      }
    }

    /* Page content */
    header {
      background: linear-gradient(to right, #4facfe, #00f2fe);
      height: 100vh;
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 0 1rem;
    }

    section {
      padding: 4rem 2rem;
    }
  </style>
</head>
<body>

  <nav id="navbar">
    <div class="logo">MySite</div>
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Services</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>

  <header>
    <h1>Welcome to My Landing Page</h1>
  </header>

  <section>
    <h2>About Us</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla a lacus ac turpis cursus fermentum.</p>
  </section>

  <section>
    <h2>Our Services</h2>
    <p>We provide high-quality web development and design services for businesses of all sizes.</p>
  </section>

  <section>
    <h2>Contact</h2>
    <p>Get in touch with us for a free consultation and quote for your project.</p>
  </section>

  <script>
    // Change navbar style on scroll
    window.addEventListener('scroll', () => {
      const navbar = document.getElementById('navbar');
      if (window.scrollY > 10) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  </script>

</body>
</html>
