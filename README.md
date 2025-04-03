# Charl Bryan MRT Product Catalog

A modern, responsive product catalog website built with HTML, CSS, and JavaScript. The site is automatically deployed to GitHub Pages.

## Live Demo

Visit the live site at: [https://mrtoronto.github.io/charl-bryan-mrt/](https://mrtoronto.github.io/charl-bryan-mrt/)

## Features

- Responsive design that works on all devices
- Clean and modern UI using Bootstrap 5
- Dynamic product rendering
- Secure HTML escaping for product data
- Automatic deployment via GitHub Actions

## Project Structure

- `index.html` - Main page template
- `generate_pages.py` - Python script for generating static pages
- `.github/workflows/` - GitHub Actions workflow for CI/CD

## Development

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mrtoronto/charl-bryan-mrt.git
   cd charl-bryan-mrt
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Generate static pages:
   ```bash
   python generate_pages.py
   ```

### Deployment

The site is automatically deployed to GitHub Pages whenever changes are pushed to the `main` branch. The deployment process is handled by GitHub Actions as defined in `.github/workflows/build-and-deploy.yml`.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.