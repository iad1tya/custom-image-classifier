# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of Custom Image Classifier seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Please Do Not

- **Do not** open a public GitHub issue for security vulnerabilities
- **Do not** disclose the vulnerability publicly until it has been addressed

### Please Do

1. **Email the maintainers** directly at: [your-security-email@example.com]
2. **Provide detailed information**, including:
   - Type of vulnerability
   - Full paths of source file(s) related to the vulnerability
   - Location of the affected source code (tag/branch/commit or direct URL)
   - Step-by-step instructions to reproduce the issue
   - Proof-of-concept or exploit code (if possible)
   - Impact of the issue, including how an attacker might exploit it

### What to Expect

- **Acknowledgment:** We will acknowledge receipt of your vulnerability report within 48 hours
- **Assessment:** We will assess the vulnerability and determine its impact and severity
- **Timeline:** We aim to provide an initial response within 5 business days
- **Resolution:** We will work to address confirmed vulnerabilities as quickly as possible
- **Disclosure:** Once the vulnerability is fixed, we will:
  - Release a security advisory
  - Credit you in the advisory (if desired)
  - Notify users to update

## Security Update Process

1. Security vulnerability is reported privately
2. Maintainers investigate and confirm the issue
3. A fix is developed and tested
4. A new version is released with the security fix
5. A security advisory is published
6. Users are notified to update

## Known Security Considerations

### File Uploads

- **Maximum file size:** 500MB (configurable in `app.py`)
- **Allowed file types:** PNG, JPG, JPEG, GIF, BMP, ZIP
- **File validation:** Basic extension checking
- **Recommendation:** Deploy behind a reverse proxy with additional file validation

### Model Security

- **Untrusted models:** Do not load model files from untrusted sources
- **Model poisoning:** Trained models can be maliciously crafted
- **Recommendation:** Only use models you have trained yourself or from trusted sources

### API Security

- **Authentication:** Currently not implemented
- **Rate limiting:** Currently not implemented
- **Recommendation:** Deploy behind an API gateway with proper authentication and rate limiting for production use

### Web Interface

- **CSRF protection:** Currently limited
- **XSS protection:** Basic sanitization in place
- **Recommendation:** Use proper authentication and HTTPS in production

## Best Practices for Deployment

### For Development

```python
# In app.py
app.run(debug=True, host='localhost', port=5000)
```

### For Production

1. **Disable Debug Mode**
   ```python
   DEBUG = False  # In config.py
   ```

2. **Use a Production WSGI Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Use HTTPS**
   ```bash
   # Use nginx or Apache as reverse proxy with SSL/TLS
   ```

4. **Add Authentication**
   ```python
   # Implement Flask-Login or similar
   ```

5. **Add Rate Limiting**
   ```python
   # Use Flask-Limiter or similar
   ```

6. **Validate All Inputs**
   ```python
   # Add comprehensive input validation
   ```

7. **Set Secure Headers**
   ```python
   # Use Flask-Talisman or similar
   ```

## Security Checklist for Production

- [ ] Debug mode disabled
- [ ] Using production WSGI server (gunicorn, uWSGI)
- [ ] HTTPS enabled
- [ ] Authentication implemented
- [ ] Rate limiting enabled
- [ ] Input validation comprehensive
- [ ] Secure headers set
- [ ] File upload validation robust
- [ ] Logs monitored regularly
- [ ] Dependencies up to date
- [ ] Security updates applied

## Dependency Security

We use the following tools to keep dependencies secure:

- **Dependabot:** Automated dependency updates
- **Safety:** Python dependency security scanner
- **pip-audit:** Audit Python packages for known vulnerabilities

Run security audit:

```bash
# Install safety
pip install safety

# Run audit
safety check

# Or use pip-audit
pip install pip-audit
pip-audit
```

## Code Security

### Input Validation

All user inputs should be validated:

```python
from werkzeug.utils import secure_filename

# Sanitize filenames
filename = secure_filename(user_provided_filename)

# Validate project names
if not re.match(r'^[a-zA-Z0-9_-]+$', project_name):
    raise ValueError("Invalid project name")
```

### Path Traversal Prevention

```python
import os
from pathlib import Path

# Prevent directory traversal
project_dir = Path('projects') / secure_filename(project_name)
if not project_dir.resolve().is_relative_to(Path('projects').resolve()):
    raise ValueError("Invalid path")
```

### SQL Injection (if using database)

```python
# Use parameterized queries
# Don't use string concatenation for SQL
```

## Third-Party Security

### PyTorch Model Loading

```python
# Be careful loading untrusted models
# torch.load uses pickle which can execute arbitrary code
# Only load models you trust

# Safer alternative (when available):
# Use torch.jit.load for TorchScript models
```

### Dataset Processing

```python
# Validate image files
# Don't trust file extensions
# Use libraries to verify file content
```

## Reporting Other Issues

For non-security issues, please use:
- **Bugs:** [GitHub Issues](https://github.com/iad1tya/custom-image-classifier/issues)
- **Questions:** [GitHub Discussions](https://github.com/iad1tya/custom-image-classifier/discussions)

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/latest/security/)
- [PyTorch Security](https://pytorch.org/docs/stable/notes/security.html)

---

**Thank you for helping keep Custom Image Classifier secure!** 🔒
