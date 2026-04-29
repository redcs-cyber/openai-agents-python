# OpenAZV Goods Ecosystem

OpenAZV Goods Ecosystem, çok ajanlı bir ticaret/operasyon omurgasıdır. Amaç; ürün kataloğu, sipariş, stok, ödeme, lojistik, CRM ve içerik/pazarlama akışlarını tek bir açık ekosistem altında birleştirmektir.

## Vizyon

- **NeuroCausal Retrieval** ile “hangi verinin neden gerekli olduğunu” açıklayan çok adımlı bağlam çıkarımı.
- **Agent Mesh** ile uzman ajanların paralel iş yürütmesi.
- **Event-first Platform** ile her aksiyonun izlenebilir, denetlenebilir ve otomasyona uygun olması.
- **OpenAZV Standard** ile üçüncü taraf geliştiricilerin kolayca entegre olabilmesi.

## Ekosistem Katmanları

1. **Core Data Layer**
   - Product, Inventory, Order, Customer, Billing, Shipment domain modelleri.
   - Olay günlüğü (event log) ve nedensel ilişki grafı.

2. **Orchestration Layer**
   - Görev yönlendirme, paralel agent çalıştırma, retry/circuit breaker/rate limit.
   - İnsan onayı gereken akışlar için policy gate.

3. **Intelligence Layer**
   - Klasik semantic retrieval + nedensel retrieval hibriti.
   - “A olduysa B/C etkisi nedir?” analiz akışları.

4. **Integration Layer**
   - ERP/CRM/e-ticaret, ödeme, kargo, e-posta, WhatsApp, çağrı ve MCP entegrasyonları.

5. **Experience Layer**
   - Operasyon paneli, yönetici özetleri, görev akışları, alarm merkezi.

## Başlangıç Paketleri

- `openazv-core`: Domain modelleri ve temel servis kontratları.
- `openazv-agent-mesh`: Uzman ajan tanımları ve paralel görev yürütme altyapısı.
- `openazv-causal-rag`: Nedensel bağlam zinciri ve multi-hop retrieval bileşenleri.
- `openazv-connectors`: Harici sistem konektörleri.
- `openazv-observability`: Audit log, metrik, tracing ve olay geçmişi.

## Yol Haritası

### Faz 1 — Foundation
- Domain model standardizasyonu.
- Event şema sözlüğü.
- En kritik 10 ajan için görev sözleşmeleri.

### Faz 2 — Operations
- Siparişten teslimata uçtan uca otomasyon.
- Kritik olay alarmı + telefon/mesaj escalation.
- CRM ve finans özet raporları.

### Faz 3 — Intelligence
- NeuroCausal RAG vNext.
- Kural tabanlı + öğrenen öncelik motoru.
- Karar defteri (decision log) ve geri-besleme döngüsü.

## Depo Yapısı Önerisi

```text
openazv-goods-ecosystem/
  README.md
  docs/
    architecture.md
    operating-model.md
  specs/
    domain-events.md
    agent-catalog.md
```

## Lisans ve Katkı

- Öneri: Apache-2.0
- Katkı modeli: RFC + küçük, odaklı PR'lar



## Organizasyona Yükleme

Depoyu organization hesabına bağımsız bir repository olarak taşımak için adım adım rehber:

- `docs/organization-upload.md`


## Stack Envanteri ve Hızlı Başlatma

İçerikte adı geçen servis/kütüphane/AI bileşenlerinin başlangıç envanteri ve kurulum script’i:

- `bootstrap/stack-catalog.yaml`
- `bootstrap/requirements-starter.txt`
- `bootstrap/start.sh`
- `bootstrap/README.md`


## Enterprise Runtime (BT Mühendisi Seviyesi)

Bu repo artık production-grade bir uygulama iskeleti içerir:

- FastAPI runtime (`src/openazv_goods_ecosystem/app.py`)
- Settings katmanı (`src/openazv_goods_ecosystem/settings.py`)
- Sağlık uçları (`/health`, `/ready`)
- Otomatik testler (`tests/test_health.py`)
- CI pipeline (`.github/workflows/openazv-goods-ecosystem-ci.yml`)

### Çalıştırma

```bash
cd openazv-goods-ecosystem
make install
make test
make run
```
