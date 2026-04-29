# Organizasyona Yükleme (GitHub)

Bu doküman, `openazv-goods-ecosystem` klasörünü bağımsız bir repo olarak organizasyon hesabına taşıma adımlarını içerir.

## 1) Yeni repo oluştur

GitHub organization içinde boş bir repo oluştur:

- Önerilen ad: `openazv-goods-ecosystem`
- Visibility: Private (ilk aşama)
- Initialize seçeneklerini kapat (README/.gitignore/license ekletme)

## 2) Lokal klasörü bağımsız git deposu yap

```bash
cd openazv-goods-ecosystem
git init
git add .
git commit -m "Initial scaffold for OpenAZV Goods Ecosystem"
```

## 3) Organization remote ekle ve push et

```bash
git remote add origin git@github.com:<ORG_NAME>/openazv-goods-ecosystem.git
git branch -M main
git push -u origin main
```

## 4) Koruma ve operasyon ayarları

- Branch protection: `main`
- Required reviews: minimum 1
- Required status checks: lint/test/doc validation
- Secrets: provider API key’leri only in Actions secrets

## 5) Sonraki adımlar

- CI pipeline ekleyin (`lint`, `schema-validate`, `docs-check`).
- `specs/` altına versioned event schema dosyaları ekleyin.
- `agent-catalog` için owner/team ve SLA alanları ekleyin.
