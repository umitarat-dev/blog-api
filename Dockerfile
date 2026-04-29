# Hafif ve güncel bir Python imajı seçiyoruz
FROM python:3.12-slim

# Python'un logları anlık basmasını ve bytecode üretmemesini sağlarız
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Çalışma klasörünü belirliyoruz
WORKDIR /app

# Önce bağımlılıkları kuruyoruz (Cache avantajı için)
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Proje dosyalarını kopyalıyoruz
COPY . /app/

# Statik dosyaları topluyoruz (Railway deployment sırasında önemlidir)
# ENV_NAME=prod sayesinde prod ayarlarını kullanır
RUN ENV_NAME=prod python manage.py collectstatic --noinput

# Gunicorn ile uygulamayı ayağa kaldırıyoruz
# Railway PORT değişkenini otomatik atar
CMD ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:8000"]