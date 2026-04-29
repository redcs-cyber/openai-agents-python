# Architecture Overview

## Principles

1. API-first ve event-driven tasarım.
2. Güvenlik varsayılanı: least privilege + explicit approvals.
3. Ölçeklenebilirlik: paralel agent execution ve queue-based workloads.
4. Açıklanabilirlik: her otomasyon kararına neden kaydı.

## Logical Components

- **Gateway**: API, auth, tenancy, policy checks.
- **Command Bus**: operasyon komutlarının yönlendirilmesi.
- **Event Bus**: domain event dağıtımı.
- **Agent Runtime**: uzman ajanların koşumu.
- **Causal Graph Store**: varlıklar/olaylar arası nedensel ilişkiler.
- **Analytics & Reporting**: KPI, SLA, anomali raporları.

## Minimal Runtime Flow

1. Kullanıcı veya sistem komutu alınır.
2. Policy gate ile güvenlik/uyum kontrolü yapılır.
3. Komut domain servisinde işlenir ve event üretilir.
4. Event agent mesh tarafından tüketilir.
5. Gerekirse causal retrieval bağlamı hazırlanır.
6. Sonuçlar panel/rapor/uyarı kanallarına dağıtılır.

