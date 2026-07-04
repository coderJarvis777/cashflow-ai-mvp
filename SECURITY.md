# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to **bq62929@gmail.com**.

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

Please include the requested information listed below (as much as you can provide) to help us better understand the nature and scope of the possible issue:

* Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
* Full paths of source file(s) related to the manifestation of the issue
* The location of the affected source code (tag/branch/commit or direct URL)
* Any special configuration required to reproduce the issue
* Step-by-step instructions to reproduce the issue
* Proof-of-concept or exploit code (if possible)
* Impact of the issue, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

## Preferred Languages

We prefer all communications to be in English.

## Policy

We follow the principle of [Coordinated Vulnerability Disclosure](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure).

We will:
- Acknowledge receipt of your vulnerability report within 48 hours
- Provide an estimated timeline for a fix
- Notify you when the vulnerability is fixed
- Publicly acknowledge your responsible disclosure (unless you prefer to remain anonymous)

We ask that you:
- Give us reasonable time to fix the issue before making it public
- Avoid violating the privacy of other users
- Make a good faith effort to avoid privacy violations, destruction of data, and interruption or degradation of our service
- Only interact with accounts you own or with explicit permission of the account holder

## Security Best Practices for Users

When using CashFlow AI, please follow these security best practices:

1. **Keep your data private**: This application processes sensitive financial data. Always run it in a secure environment.

2. **Use strong API keys**: If you integrate with external services (OpenAI, etc.), use strong, unique API keys and rotate them regularly.

3. **Update regularly**: Keep your dependencies up to date by running `pip install -r requirements.txt` periodically.

4. **Secure your environment**:
   - Use a virtual environment
   - Don't commit `.env` files with real credentials
   - Use environment variables for sensitive data
   - Restrict file permissions on configuration files

5. **Data handling**:
   - The application processes financial data locally
   - No data is sent to external servers unless you explicitly configure integrations
   - Clear your session data when done

## Security Updates

We will announce security updates through:
- GitHub Security Advisories
- Release notes
- Email notifications (for critical vulnerabilities)

## Contact

For any security-related questions, please contact: **bq62929@gmail.com**
