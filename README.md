# Portofolio Django — Khikam

## Cara Menjalankan

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Migrasi database
python manage.py migrate

# 3. Jalankan server
python manage.py runserver
```

Buka browser → http://127.0.0.1:8000

## Struktur Proyek

```
portofolio/          ← folder project Django
main/
  templates/main/
    base.html        ← navbar + layout utama
    home.html
    about.html
    skills.html
    services.html
    blogs.html
    contact.html
  static/
    css/             ← semua file CSS
    images/          ← main.jpeg (foto profil)
  views.py           ← logic semua halaman
  urls.py            ← routing
```

## URL Pages

| URL           | Halaman   |
|---------------|-----------|
| /             | Home      |
| /about/       | About     |
| /skills/      | Skills    |
| /services/    | Services  |
| /blogs/       | Blogs     |
| /contact/     | Contact   |
