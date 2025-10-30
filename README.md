# iinioiscan
# Web Server Discovery

A Python script designed to test multiple domains or subdomains via HTTP and HTTPS, identifying responses, redirects, and status codes.

---

## Usage

You can use the script in **two ways**:

### 1. Using piped input

Accepts standard input (`stdin`) directly from other tools (e.g., `subfinder`, `cat`, etc.):

```bash
subfinder -d example.com | python3 iinioi.py
```


```bash
cat targets.txt | python3 script.py
```

---

### 2. Using a file

Use the `-p` (or `--path`) flag to specify a file containing domains, one per line:

```bash
python3 script.py -p /path/to/file.txt
```

---

## Options

| Flag         | Description                                | Example          |
| ------------ | ------------------------------------------ | ---------------- |
| `-p, --path` | Path to the `.txt` file containing domains | `-p domains.txt` |
| `-u, --url`  | Specify a single domain to test manually   | `-u example.com` |  (yet to be implemented)

---

## Examples

```bash
subfinder -d example.com | python3 script.py
python3 iinioi.py -p subdomains.txt
python3 iinioi.py -u api.example.com
```

---

## Output

Each line prints the tested domain along with its HTTP status code.
Colors are used to indicate the response category:

| Status Code Range | Meaning      | Color |
| ----------------- | ------------ | ----- |
| 200–299           | Success      | 🟢    |
| 300–399           | Redirect     | 🟡    |
| 400–499           | Client Error | 🔴    |
| 500–599           | Server Error | 🟣    |

If a redirect occurs (status 3xx), the output also includes the redirect target URL.
---

## Libraries

- pyfiglet
- requests



## Author

**Maz3ll4**
GitHub: https://github.com/RodManzella/







